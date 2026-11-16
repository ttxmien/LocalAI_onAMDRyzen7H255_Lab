# 🤖 Phase 5: Xây dựng Local AI Agent cho DevOps & Tự động hóa

## 1. Khác biệt giữa Chatbot và AI Agent
- **Chatbot:** Chỉ nhận văn bản và trả về văn bản.
- **AI Agent:** Được trang bị **Tools (Công cụ)** (ví dụ: đọc file log, kiểm tra RAM/CPU, chạy lệnh kiểm tra container, truy vấn API) và có khả năng tự quyết định khi nào cần gọi công cụ nào theo vòng lặp **ReAct (Reason + Act)** để hoàn thành mục tiêu.

---

## 2. Cấu trúc Function Calling cục bộ
Các mô hình hiện đại như **Qwen2.5-Coder-14B** và **Qwen3-14B** hỗ trợ rất tốt **Native Tool Calling** qua Ollama API. Mô hình sẽ trả về một cấu trúc JSON chỉ định tên hàm và tham số cần gọi, code Python của bạn sẽ thực thi hàm đó và trả kết quả lại cho mô hình tổng hợp.

---

## 🧪 Bài tập thực hành Phase 5
Chạy một DevOps Health-Check Agent cục bộ có khả năng tự kiểm tra tài nguyên thực tế trên chiếc ThinkBook của bạn và phân tích log giả lập:
```bash
python 05-agents-devops/devops_agent.py
```
