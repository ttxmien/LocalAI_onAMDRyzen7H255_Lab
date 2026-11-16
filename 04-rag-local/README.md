# 🧠 Phase 4: Xây dựng hệ thống RAG (Retrieval-Augmented Generation) Offline

## 1. Tại sao cần RAG cho công việc kỹ thuật?
LLM không biết các tài liệu nội bộ, log lỗi hệ thống hay kiến trúc dự án riêng của bạn. Thay vì fine-tune tốn kém, **RAG** giải quyết bài toán bằng 3 bước:
1. **Indexing (Lập chỉ mục):** Cắt nhỏ tài liệu thành các đoạn (*chunks*), dùng mô hình **Embedding** biến mỗi đoạn thành một vector số học và lưu vào Vector Database (**ChromaDB**).
2. **Retrieval (Truy xuất):** Khi bạn đặt câu hỏi, câu hỏi cũng được biến thành vector và tìm ra top $K$ đoạn tài liệu có độ tương đồng cao nhất (*Cosine Similarity*).
3. **Generation (Sinh câu trả lời):** Ghép các đoạn tài liệu tìm được vào Prompt và yêu cầu Local LLM (`qwen2.5-coder:14b` hoặc `gemma3:12b`) trả lời dựa trên dữ liệu đó.

---

## 2. Tải Embedding Model chạy cục bộ
Ollama hỗ trợ chạy trực tiếp các mô hình Embedding siêu nhẹ và chính xác:
```powershell
ollama pull nomic-embed-text
```

---

## 🧪 Bài tập thực hành Phase 4
Chạy hệ thống hỏi đáp tài liệu kỹ thuật & phân tích log hoàn toàn offline:
```bash
python 04-rag-local/simple_rag.py
```
