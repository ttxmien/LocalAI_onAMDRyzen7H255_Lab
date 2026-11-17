# 2. Cơ sở dữ liệu Vector (ChromaDB & FAISS)

## 2.1 Vector Database làm gì?
Khi kho tài liệu của bạn có hàng chục nghìn đoạn văn bản, việc tính Cosine Similarity tuần tự từng vector sẽ rất chậm. Vector Database sử dụng các thuật toán lập chỉ mục đặc biệt như **HNSW (Hierarchical Navigable Small World)** để tìm kiếm láng giềng gần nhất xấp xỉ (**ANN - Approximate Nearest Neighbors**) chỉ trong vài mili-giây.

## 2.2 So sánh ChromaDB và FAISS cho Local RAG

| Tiêu chí | ChromaDB | FAISS (Facebook AI Similarity Search) |
| :--- | :--- | :--- |
| **Bản chất** | Cơ sở dữ liệu Vector hoàn chỉnh (lưu trữ cả vector, văn bản gốc và metadata). | Thư viện lõi C++/Python chuyên về tìm kiếm vector tốc độ cực cao. |
| **Lọc theo Metadata** | Hỗ trợ mạnh mẽ (ví dụ: chỉ tìm trong tài liệu thuộc `project="BMW"` và `year=2026`). | Không hỗ trợ sẵn, phải tự code thêm lớp lọc bên ngoài. |
| **Lưu trữ bền vững** | Tự động lưu xuống ổ cứng qua SQLite + Parquet chỉ với 1 dòng cấu hình. | Phải tự gọi lệnh `faiss.write_index()` và lưu kèm file mapping văn bản riêng. |
| **Phù hợp với** | Xây dựng ứng dụng RAG hoàn chỉnh, quản lý tài liệu nội bộ, chatbot. | Nghiên cứu thuật toán, xử lý tập dữ liệu cực lớn trên RAM. |
