# 📚 Phase 1: Nền tảng Lý thuyết Local LLM

## 1. Tại sao chạy được mô hình hàng chục tỷ tham số trên Laptop?
Một mô hình ngôn ngữ lớn (LLM) thực chất là một tập hợp khổng lồ các ma trận số thực (trọng số - *weights*).
- **FP16 (16-bit floating point):** Mỗi tham số tốn **2 Bytes**.
  - Ví dụ: Model 14B (14 tỷ tham số) ở FP16 tốn $14 \times 2 = 28\text{ GB}$ bộ nhớ — gần như chiếm trọn 32GB RAM của máy, không còn chỗ cho hệ điều hành hay ngữ cảnh (Context).
- **Quantization (Lượng tử hóa - 4-bit / 5-bit / 8-bit):**
  - Chuyển đổi trọng số từ số thực 16-bit sang số nguyên 4-bit (`Q4_K_M`) hoặc 5-bit (`Q5_K_M`).
  - Mỗi tham số `Q4_K_M` chỉ tốn trung bình **~0.55 - 0.6 Bytes**.
  - Model 14B lúc này chỉ chiếm khoảng **8.5GB – 9.5GB RAM**, giữ lại >96% độ thông minh so với bản gốc!

---

## 2. Hai giai đoạn khi LLM trả lời (Prefill vs Decode)
Điều này giúp trả lời tại sao máy nhanh hay chậm:
1. **Prefill (Đọc & hiểu prompt đầu vào):** Xử lý song song tất cả các token bạn nhập vào cùng lúc. Giai đoạn này phụ thuộc vào **sức mạnh tính toán thô (FLOPS)** của nhân GPU/CPU.
2. **Decode (Sinh từng chữ trả lời):** Sinh tuần tự từng token một. Mỗi lần sinh ra **1 token**, GPU phải đọc toàn bộ trọng số của model (ví dụ 9GB) từ RAM đi qua bus bộ nhớ. Giai đoạn này bị giới hạn bởi **băng thông bộ nhớ (Memory Bandwidth)**.

---

## 3. Dense Model vs MoE (Mixture of Experts)
- **Dense Model (Mô hình đặc - ví dụ Qwen2.5-14B):** Mỗi token đi qua đều kích hoạt toàn bộ 14 tỷ tham số.
- **MoE Model (Hỗn hợp chuyên gia - ví dụ Qwen3-30B-A3B):** Tổng bộ nhớ chứa 30 tỷ tham số (tốn ~18.5GB RAM), nhưng với mỗi token, bộ định tuyến (Router) chỉ kích hoạt **3 tỷ tham số** phù hợp nhất.
  - *Kết quả trên ThinkBook 32GB RAM:* Máy đủ RAM để chứa cả 30B tham số, trong khi GPU chỉ phải tính toán 3B tham số -> **Tốc độ siêu nhanh mà kiến thức cực rộng!**

---

## 🧪 Thực hành Phase 1
Chạy script tính toán bộ nhớ tiêu thụ (bao gồm cả KV Cache theo độ dài ngữ cảnh) để tự ước lượng trước khi tải bất kỳ model nào:
```bash
python 01-foundations/memory_calculator.py
```
