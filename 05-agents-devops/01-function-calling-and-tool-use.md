# 1. Cơ chế Function Calling (Tool Use)

## 1.1 Bản chất của Tool Calling
Bản thân LLM chỉ là một bộ máy sinh văn bản — nó **không thể** tự truy cập Internet, không thể tự đọc file trên ổ cứng `D:\` và không thể chạy lệnh PowerShell.
**Function Calling** là cơ chế cho phép bạn định nghĩa trước một danh sách các hàm (Tools) kèm mô tả tham số dưới dạng **JSON Schema** và gửi kèm trong System Prompt.

## 1.2 Luồng thực thi 4 bước của Function Calling
1. **Khai báo (Schema Definition):** Ứng dụng gửi câu hỏi của người dùng kèm danh sách mô tả các công cụ hiện có (ví dụ: `read_log_file(path)`, `check_ram_usage()`) cho LLM.
2. **Quyết định & Sinh JSON (Tool Selection):** LLM phân tích câu hỏi; nếu thấy cần dữ liệu thực tế, thay vì trả lời bằng văn bản thông thường, nó trả về một chuỗi JSON có cấu trúc:
   ```json
   {"name": "read_log_file", "arguments": {"path": "/var/log/gnss.log"}}
   ```
3. **Thực thi phía Client (Local Execution):** Code Python của bạn bắt lấy chuỗi JSON này, gọi hàm thực tế trên máy tính để lấy dữ liệu thật (ví dụ nội dung file log).
4. **Tổng hợp kết quả (Synthesis):** Gửi kết quả trả về từ hàm ngược lại cho LLM để mô hình phân tích và viết câu trả lời hoàn chỉnh cho người dùng.
