# 3. Quantization (Lượng tử hóa) và Định dạng GGUF

## 3.1 Quantization là gì?
Trọng số gốc của LLM thường được huấn luyện ở độ chính xác **FP16** hoặc **BF16** (16-bit floating point — tốn 2 Bytes cho mỗi tham số).
**Quantization** là kỹ thuật nén các số thực 16-bit này xuống các kiểu dữ liệu ít bit hơn (8-bit, 5-bit, 4-bit, thậm chí 3-bit) để giảm dung lượng bộ nhớ và tăng tốc độ truyền tải dữ liệu qua bus bộ nhớ.

## 3.2 Giải mã ký hiệu mức nén trong GGUF (K-Quants)
Trong hệ sinh thái `llama.cpp` / Ollama, bạn sẽ thường gặp các ký hiệu như `Q4_K_M`, `Q5_K_M`, `Q8_0`:
- **`Q4`, `Q5`, `Q8`:** Số bit trung bình trên mỗi tham số (4-bit, 5-bit, 8-bit).
- **`_K`:** Sử dụng kỹ thuật *K-Quant* — chia trọng số thành các khối (blocks) nhỏ và áp dụng hệ số tỷ lệ (scale) khác nhau cho từng khối để giữ độ chính xác cao hơn nén tuyến tính thông thường.
- **`_S` / `_M` / `_L` (Small / Medium / Large):** Chỉ mức phân bổ độ chính xác cho các lớp quan trọng (như lớp Attention và Feed-Forward đầu/cuối). Ví dụ: `Q4_K_M` nén phần lớn lớp ở 4-bit nhưng giữ một số lớp nhạy cảm ở 6-bit để bảo toàn chất lượng.

## 3.3 Bảng so sánh lựa chọn mức nén

| Mức nén | Byte / Tham số | Dung lượng model 14B | Chất lượng so với FP16 | Khuyến nghị sử dụng |
| :--- | :--- | :--- | :--- | :--- |
| **FP16** | 2.00 B | ~28.0 GB | 100% (Gốc) | Không dùng chạy local trên laptop 32GB |
| **Q8_0** | ~1.05 B | ~14.7 GB | ~99.9% | Dùng cho model 7B–8B khi dư RAM |
| **Q5_K_M** | ~0.68 B | ~9.5 GB | ~98.5% | Lý tưởng cho viết code & suy luận logic |
| **Q4_K_M** | ~0.58 B | ~8.2 GB | ~96.5% | Điểm cân bằng vàng giữa tốc độ và trí thông minh |

## 3.4 Định dạng tệp GGUF
**GGUF (GPT-Generated Unified Format)** là chuẩn đóng gói model của `llama.cpp`:
- Gộp toàn bộ metadata (kiến trúc, tokenizer, prompt template) và trọng số đã nén vào **một file duy nhất**.
- Hỗ trợ kỹ thuật **`mmap` (Memory Mapping)**: ánh xạ trực tiếp file từ ổ cứng NVMe vào không gian địa chỉ bộ nhớ, giúp khởi động model chỉ trong vài giây.
- Cho phép chia lớp linh hoạt (**Layer Offloading**): đẩy một phần hoặc toàn bộ các lớp mạng nơ-ron lên GPU (Radeon 780M), phần còn lại chạy trên CPU.
