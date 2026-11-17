# 📚 Phase 1: Foundations (Kiến trúc, Lượng tử hóa & Định mức Bộ nhớ)

## 1. Bản chất phần cứng & Cấu trúc Mô hình Ngôn ngữ lớn (LLM)
Khi chạy LLM trên laptop cá nhân (như ThinkBook 14 G8+ với 32GB RAM LPDDR5x), bạn không dùng card rời mà tận dụng **Shared Unified Memory** (RAM hệ thống làm VRAM cho iGPU Radeon 780M). Việc hiểu sâu các khái niệm cốt lõi giúp bạn chọn đúng model mà không lo tràn RAM (OOM):

1. **Decoder-only Transformer & Self-Attention:** Mọi LLM hiện đại đều dùng kiến trúc này. Cơ chế **Grouped-Query Attention (GQA)** trên các dòng model mới (như Qwen2.5/Qwen3) cực kỳ quan trọng vì nó giúp giảm tải dung lượng KV Cache, cho phép giữ cửa sổ ngữ cảnh dài hơn mà không làm nghẽn băng thông bộ nhớ.
2. **Quantization (Lượng tử hóa GGUF):** Chuyển đổi trọng số từ chuẩn FP16 (2 bytes/tham số) xuống `Q4_K_M` (~0.58 bytes/tham số) hoặc `Q5_K_M` (~0.68 bytes/tham số). Định dạng GGUF hỗ trợ công nghệ `mmap`, cho phép nạp model từ ổ NVMe lên RAM tức thì mà không cần load toàn bộ vào RAM hệ thống trước.
3. **Memory-Bandwidth Bottleneck:** Giai đoạn sinh chữ (Decode) của LLM không bị giới hạn bởi sức mạnh tính toán của chip (FLOPS) mà bị bóp nghẹt bởi tốc độ truyền tải dữ liệu qua bus RAM. Bus LPDDR5x-7500 MT/s trên ThinkBook đạt băng thông thực tế ~85–95 GB/s — là chìa khóa để chạy mượt các model cỡ 14B.

---

## 2. Công thức tính toán dung lượng RAM thực tế
Trước khi tải bất kỳ model nào, hãy tính tổng RAM cần cấp phát theo công thức chuẩn:

$$\text{Total RAM} = (\text{Số tỷ tham số } \times \text{Số bytes theo mức lượng tử}) + \text{Dung lượng KV Cache} + \text{Buffer hệ thống (~1GB)}$$

---

## 🧪 Thực hành Phase 1
Viết và chạy script Python `memory_calculator.py` để tự động tính toán và kiểm tra định mức bộ nhớ cho các model trên máy 32GB RAM:

```bash
python 01-foundations/memory_calculator.py