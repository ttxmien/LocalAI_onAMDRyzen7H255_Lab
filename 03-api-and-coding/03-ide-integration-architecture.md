# 3. Kiến trúc tích hợp Trợ lý Lập trình AI vào VS Code

## 3.1 Phân tách vai trò Model cho hai tác vụ khác nhau
Trong môi trường lập trình thực tế (như extension **Continue** hoặc **Cline** trên VS Code), nhu cầu sử dụng AI chia làm 2 luồng hoàn toàn khác biệt:

1. **Tab Autocomplete (Gợi ý code tự động khi đang gõ phím):**
   - **Đặc thù:** Cần độ trễ cực thấp (**dưới 400ms**), ngữ cảnh ngắn (vài chục dòng xung quanh vị trí con trỏ chuột).
   - **Giải pháp:** Sử dụng model nhỏ gọn, tốc độ siêu nhanh như **`qwen2.5-coder:7b`** (hoặc `3b` / `1.5b`) với kỹ thuật **FIM (Fill-In-the-Middle)** — cho phép mô hình nhìn đồng thời phần code phía trên (`prefix`) và phía dưới (`suffix`) con trỏ để điền đoạn code còn thiếu ở giữa.

2. **Chat, Refactor & Agentic Coding (Hỏi đáp, sửa lỗi nhiều file):**
   - **Đặc thù:** Cần khả năng suy luận sâu, hiểu kiến trúc dự án và đọc được nhiều file ngữ cảnh cùng lúc, chấp nhận chờ vài giây.
   - **Giải pháp:** Sử dụng model lớn như **`qwen2.5-coder:14b`** với `num_ctx=8192` hoặc `16384`.

## 3.2 Quản lý bộ nhớ khi chạy song song 2 model
Nếu chạy đồng thời cả 2 model trên máy 32GB RAM:
- `qwen2.5-coder:14b` (`Q4_K_M`) chiếm ~9.5 GB.
- `qwen2.5-coder:7b` (`Q4_K_M`) chiếm ~4.7 GB.
- Tổng cộng ~14.2 GB RAM — hoàn toàn nằm gọn trong vùng an toàn của máy 32GB RAM mà không cần phải nạp/xả (swap) model liên tục.
