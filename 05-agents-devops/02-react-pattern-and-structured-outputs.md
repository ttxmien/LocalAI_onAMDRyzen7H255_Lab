# 2. Vòng lặp ReAct và Structured Outputs

## 2.1 Kiến trúc ReAct (Reason + Act)
Thay vì chỉ gọi một công cụ duy nhất rồi dừng lại, **ReAct** biến LLM thành một tác nhân tự hành có khả năng suy luận nhiều bước liên tiếp cho đến khi giải quyết xong vấn đề:

1. **Thought (Suy nghĩ):** *"Hệ thống đang báo lỗi kết nối GNSS. Tôi cần kiểm tra xem service `gnss-manager` có đang chạy không."*
2. **Action (Hành động):** Gọi tool `check_service_status("gnss-manager")`.
3. **Observation (Quan sát kết quả):** Tool trả về `"Status: Crashed (Exit code 139)"`.
4. **Thought (Suy nghĩ tiếp):** *"Service bị crash với mã 139 (Segmentation Fault). Tôi cần đọc 50 dòng cuối của log để tìm nguyên nhân."*
5. **Action (Hành động):** Gọi tool `read_logs("gnss-manager", lines=50)`.
6. **Final Answer (Kết luận):** Tổng hợp nguyên nhân gốc rễ và đề xuất giải pháp.

## 2.2 Structured Outputs (Đầu ra có cấu trúc JSON Schema)
Khi tích hợp AI vào các pipeline tự động hóa (CI/CD, xuất báo cáo tự động), văn bản tự do rất khó xử lý bằng code.
- **Structured Outputs** (được hỗ trợ qua thư viện `Pydantic` và `grammar-constrained sampling` trong `llama.cpp`/Ollama) ép buộc bộ giải mã của LLM **chỉ được phép sinh ra các token tuân thủ 100% cấu trúc JSON Schema** đã định nghĩa trước — loại bỏ hoàn toàn lỗi sai cú pháp JSON hoặc thiếu trường dữ liệu.
