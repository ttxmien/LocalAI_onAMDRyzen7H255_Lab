# 3. Model Context Protocol (MCP)

## 3.1 MCP là gì và giải quyết bài toán gì?
Trước đây, mỗi ứng dụng AI (VS Code, Claude Desktop, ứng dụng Python tự viết) lại có một cách kết nối riêng với từng nguồn dữ liệu (GitHub, Jira, PostgreSQL, Filesystem). Nếu có $M$ ứng dụng AI và $N$ công cụ, bạn phải viết $M \times N$ bộ kết nối khác nhau.

**Model Context Protocol (MCP)** là một giao thức mở chuẩn hóa cách các ứng dụng AI (MCP Hosts/Clients) giao tiếp với các nguồn dữ liệu và công cụ bên ngoài (MCP Servers) — được ví như **"cổng USB-C cho các ứng dụng AI"**.

## 3.2 Kiến trúc 3 thành phần của MCP
1. **MCP Host:** Ứng dụng AI trực tiếp tương tác với người dùng (ví dụ: VS Code với Cline/Continue, hoặc ứng dụng Python Agent của bạn).
2. **MCP Client:** Thành phần nằm bên trong Host, duy trì kết nối 1-1 với các MCP Server qua giao thức JSON-RPC 2.0 (thông qua `stdio` cho local process hoặc `SSE/HTTP` cho remote service).
3. **MCP Server:** Chương trình độc lập cung cấp 3 loại tài nguyên chuẩn hóa:
   - **Tools:** Các hàm thực thi hành động (truy vấn SQL, tạo ticket Jira, đọc file log).
   - **Resources:** Dữ liệu chỉ đọc cung cấp ngữ cảnh (tài liệu cấu hình, schema database).
   - **Prompts:** Các mẫu prompt chuẩn hóa sẵn cho từng quy trình nghiệp vụ.
