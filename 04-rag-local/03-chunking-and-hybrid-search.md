# 3. Chiến lược Chunking và Tìm kiếm lai (Hybrid Search)

## 3.1 Tại sao phải chia nhỏ văn bản (Chunking)?
1. Mỗi Embedding model có giới hạn độ dài đầu vào (ví dụ `nomic-embed-text` tối đa 8192 tokens, các model cũ chỉ 512 tokens).
2. Nếu nhúng cả một file tài liệu dài 50 trang thành 1 vector duy nhất, thông tin chi tiết sẽ bị "pha loãng", làm giảm độ chính xác khi truy xuất.

### Các kỹ thuật Chunking phổ biến:
- **Fixed-size with Overlap (Chia theo kích thước cố định có gối đầu):** Cắt mỗi đoạn khoảng `500 – 1000 ký tự` (hoặc tokens) và cho phép **gối đầu (overlap) 10–15%** giữa hai đoạn liên tiếp để tránh cắt đứt ngang một câu hoặc một ý quan trọng.
- **Recursive Character / Markdown-aware Splitting:** Ưu tiên cắt theo ranh giới tự nhiên như tiêu đề (`#`, `##`), đoạn văn (`\n\n`), rồi mới tới câu (`.`), giúp bảo toàn cấu trúc logic của tài liệu kỹ thuật.

## 3.2 Hybrid Search (Tìm kiếm lai: Vector + BM25) và Re-ranking
Tìm kiếm Vector thuần túy rất giỏi hiểu ngữ nghĩa tổng quát, nhưng lại **yếu khi tìm mã lỗi chính xác** (ví dụ: mã DTC `0xB7F321`, tên hàm `SP25ProviderGNSSProxySDaT`).
- **Giải pháp Hybrid Search:** Kết hợp song song:
  1. **Dense Retrieval (Vector Search):** Bắt ý nghĩa ngữ cảnh.
  2. **Sparse Retrieval (BM25 / Keyword Search):** Bắt chính xác từ khóa, mã lỗi, tên biến.
- **Re-ranking (Xếp hạng lại):** Dùng một mô hình **Cross-Encoder** nhỏ (như `bge-reranker`) chấm điểm lại top 10 kết quả tìm được để chọn ra top 3 đoạn chính xác nhất đưa vào prompt cho LLM.
