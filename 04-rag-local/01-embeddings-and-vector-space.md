# 1. Mô hình Embedding và Không gian Vector

## 1.1 Tại sao tìm kiếm từ khóa truyền thống không đủ?
Tìm kiếm từ khóa truyền thống (như `Ctrl+F` hoặc SQL `LIKE`) chỉ khớp chính xác mặt chữ. Nếu tài liệu viết *"Lỗi mất tín hiệu vệ tinh GNSS"* nhưng người dùng hỏi *"Tại sao hệ thống định vị không bắt được tọa độ?"*, tìm kiếm từ khóa sẽ thất bại hoàn toàn.

## 1.2 Text Embeddings (Nhúng văn bản) là gì?
**Embedding Model** (ví dụ: `nomic-embed-text`, `bge-m3`) là một mạng nơ-ron chuyên biệt biến đổi một đoạn văn bản có độ dài bất kỳ thành một **vector số thực có số chiều cố định** (ví dụ: mảng gồm 768 hoặc 1024 con số).
- Các đoạn văn bản có **ý nghĩa tương đồng** sẽ nằm gần nhau trong không gian vector đa chiều, ngay cả khi chúng sử dụng từ vựng khác nhau.

## 1.3 Đo lường độ tương đồng (Cosine Similarity)
Để biết câu hỏi của người dùng ($\vec{A}$) giống với đoạn tài liệu nào ($\vec{B}$) nhất, hệ thống tính **Cosine Similarity** (góc giữa hai vector):

$$\text{Cosine Similarity}(\vec{A}, \vec{B}) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|}$$

- Giá trị tiến gần tới **`1.0`**: Hai đoạn văn có cùng ngữ nghĩa.
- Giá trị gần **`0.0`**: Hai đoạn văn không liên quan đến nhau.
