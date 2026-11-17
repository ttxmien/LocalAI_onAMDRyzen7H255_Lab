# 2. Cơ chế Streaming và Các tham số Sinh văn bản

## 2.1 Streaming Response (SSE - Server-Sent Events)
- **Non-streaming (`stream=False`):** Client phải chờ model sinh xong toàn bộ câu trả lời (có thể mất 15–30 giây) mới nhận được cục dữ liệu JSON hoàn chỉnh. Tạo cảm giác ứng dụng bị treo.
- **Streaming (`stream=True`):** Server gửi từng token ngay khi vừa tính toán xong thông qua giao thức HTTP Server-Sent Events (SSE). Người dùng thấy chữ hiện ra ngay lập tức sau ~0.5 giây, cải thiện vượt bậc trải nghiệm tương tác (UX).

## 2.2 Các siêu tham số (Hyperparameters) điều khiển đầu ra

| Tham số | Khoảng giá trị | Tác động đến hành vi của LLM | Giá trị khuyên dùng |
| :--- | :--- | :--- | :--- |
| **`temperature`** | `0.0` – `2.0` | Kiểm soát độ ngẫu nhiên khi chọn token tiếp theo. Càng gần `0`, mô hình càng chọn từ có xác suất cao nhất (nhất quán, chính xác). Càng cao, câu trả lời càng sáng tạo nhưng dễ bịa đặt (hallucination). | `0.1 – 0.2` cho lập trình, phân tích log, RAG.<br>`0.7` cho viết lách, brainstorming. |
| **`top_p`** | `0.0` – `1.0` | *Nucleus Sampling*: Chỉ xét tập hợp các token nhỏ nhất có tổng xác suất tích lũy đạt `top_p` (ví dụ `0.9` = 90%), loại bỏ các từ vô nghĩa ở đuôi phân phối. | `0.9` (giữ mặc định khi đã chỉnh `temperature`). |
| **`num_ctx`** | `2048` – `32768+` | Kích thước cửa sổ ngữ cảnh tối đa (tính bằng token) cho cả Input + Output. Tăng quá cao sẽ ngốn nhiều RAM và làm chậm tốc độ xử lý. | `4096` hoặc `8192` cho tác vụ hằng ngày trên Radeon 780M. |
| **`repeat_penalty`** | `1.0` – `1.5` | Phạt các token đã xuất hiện để tránh tình trạng model bị lặp lại một cụm từ vô tận. | `1.05 – 1.1` |
