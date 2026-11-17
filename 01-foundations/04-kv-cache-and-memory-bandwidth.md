# 4. KV Cache và Nút thắt Băng thông Bộ nhớ

## 4.1 KV Cache là gì?
Khi LLM sinh văn bản, để sinh ra token thứ 100, mô hình cần tính toán Attention với 99 token đứng trước đó. Thay vì tính lại các vector Key ($K$) và Value ($V$) của 99 token cũ từ đầu ở mỗi bước, hệ thống sẽ lưu chúng vào bộ nhớ đệm gọi là **KV Cache**.

- **Lợi ích:** Giảm độ phức tạp tính toán từ $O(N^2)$ xuống $O(N)$ ở mỗi bước sinh từ.
- **Chi phí:** KV Cache tiêu tốn bộ nhớ tỷ lệ thuận với **độ dài ngữ cảnh (`num_ctx`)** và kích thước mô hình. Nếu mở context 32,768 hoặc 131,072 tokens, riêng KV Cache có thể ngốn thêm 6GB–12GB RAM.

## 4.2 Tối ưu KV Cache với Flash Attention và KV Quantization
1. **Flash Attention (`OLLAMA_FLASH_ATTENTION=1`):** Thuật toán chia nhỏ ma trận Attention thành các khối vừa với bộ nhớ đệm tốc độ cao (SRAM/Cache) của GPU, giúp giảm mạnh việc đọc/ghi ra RAM và giảm bộ nhớ tiêu thụ khi ngữ cảnh dài.
2. **Nén KV Cache (`OLLAMA_KV_CACHE_TYPE=q8_0`):** Nén dữ liệu lưu trong KV Cache từ 16-bit xuống 8-bit, tiết kiệm ~40% dung lượng RAM cho context dài mà hầu như không ảnh hưởng độ chính xác.

## 4.3 Tại sao Băng thông Bộ nhớ (Memory Bandwidth) quyết định tốc độ?
Ở giai đoạn sinh chữ (**Decode**), phép nhân ma trận với vector chỉ thực hiện rất ít phép tính trên mỗi byte dữ liệu đọc vào. Do đó, tốc độ nhả chữ (tokens/giây) tuân theo công thức ước lượng:

$$\text{Tokens/giây} \approx \frac{\text{Băng thông bộ nhớ thực tế (GB/s)}}{\text{Dung lượng trọng số model (GB)}}$$

- Trên **ThinkBook 14 G8+**, RAM **LPDDR5x-7500 MT/s** kênh đôi (128-bit) có băng thông lý thuyết **120 GB/s** (thực tế đạt ~85–95 GB/s).
- Với model **14B Q4_K_M** nặng ~8.5 GB, tốc độ lý thuyết tối đa sẽ rơi vào khoảng $95 / 8.5 \approx 11\text{ – }18\text{ tokens/giây}$.
