# 2. Tokenization (Mã hóa văn bản thành Token)

## 2.1 Token là gì?
LLM không đọc trực tiếp văn bản dạng chuỗi ký tự mà đọc các con số nguyên gọi là **Token ID**. Một token có thể là:
- Một từ hoàn chỉnh (ví dụ: `apple` $ightarrow$ 1 token).
- Một phần của từ / subword (ví dụ: `unbelievable` $ightarrow$ `un` + `believ` + `able`).
- Ký tự đơn lẻ, dấu câu, khoảng trắng hoặc emoji.

## 2.2 Các thuật toán Tokenization phổ biến
- **BPE (Byte-Pair Encoding):** Bắt đầu từ các ký tự/byte cơ bản và gộp dần các cặp xuất hiện thường xuyên nhất trong tập huấn luyện. Được dùng bởi GPT, Llama 3, Qwen.
- **SentencePiece / Unigram:** Xử lý trực tiếp trên luồng ký tự thô mà không cần tách từ trước bằng dấu cách, rất hiệu quả với các ngôn ngữ không dùng dấu cách phân tách từ rõ ràng.

## 2.3 Tại sao kích thước bộ từ vựng (Vocabulary Size) lại quan trọng?
- **Qwen2.5 / Qwen3** có bộ từ vựng lớn (~151,643 tokens) và hỗ trợ tiếng Việt, code, ký tự đặc biệt rất tốt.
- **Ý nghĩa thực tế khi chạy Local AI:**
  - Nếu tokenizer tối ưu tốt cho tiếng Việt, 100 chữ tiếng Việt chỉ tốn khoảng **130–150 tokens**.
  - Nếu tokenizer kém tối ưu (như các đời Llama 2 cũ), 100 chữ tiếng Việt có thể tốn tới **250–300 tokens**, làm tiêu tốn gấp đôi KV Cache và giảm một nửa tốc độ sinh câu trả lời.
