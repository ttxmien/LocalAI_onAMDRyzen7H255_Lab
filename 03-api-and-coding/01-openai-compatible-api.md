# 1. Giao tiếp Local LLM qua OpenAI-Compatible REST API

## 1.1 Chuẩn hóa giao tiếp API
Thay vì mỗi inference engine tự định nghĩa một định dạng request/response riêng, hệ sinh thái Local AI hiện nay đều hỗ trợ **chuẩn API tương thích OpenAI** (tại đường dẫn `http://localhost:11434/v1` đối với Ollama).

- **Lợi ích:** Mã nguồn ứng dụng của bạn không bị khóa chặt (vendor lock-in) vào một nhà cung cấp. Chỉ cần thay đổi 2 tham số `base_url` và `api_key`, bạn có thể chuyển đổi qua lại giữa Local LLM (Qwen/Gemma) và Cloud LLM (GPT/Claude) mà không cần sửa logic xử lý.

## 1.2 Cấu trúc thông điệp Chat Completions
Một request gửi tới endpoint `/v1/chat/completions` bao gồm danh sách các `messages` với 3 vai trò (roles) chính:
1. **`system`:** Thiết lập nhân cách, quy tắc ứng xử, định dạng đầu ra và giới hạn phạm vi kiến thức cho mô hình.
2. **`user`:** Câu hỏi, đoạn code hoặc dữ liệu đầu vào từ người dùng.
3. **`assistant`:** Câu trả lời trước đó của mô hình (dùng để duy trì lịch sử hội thoại đa lượt — multi-turn conversation).

> **Lưu ý quan trọng:** Các REST API của LLM là **Stateless (không lưu trạng thái)**. Để AI nhớ được ngữ cảnh cuộc trò chuyện, ứng dụng của bạn phải gửi lại toàn bộ lịch sử mảng `messages` trong mỗi lần gọi API tiếp theo.
