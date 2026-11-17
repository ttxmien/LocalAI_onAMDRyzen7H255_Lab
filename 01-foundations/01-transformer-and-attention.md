# 1. Kiến trúc Transformer và Cơ chế Attention

## 1.1 Tổng quan kiến trúc Transformer
Hầu hết các mô hình ngôn ngữ lớn (LLM) hiện đại (như Qwen, Llama, Gemma) đều dựa trên kiến trúc **Decoder-only Transformer**. Thay vì xử lý tuần tự từng từ như mạng nơ-ron hồi quy (RNN/LSTM), Transformer xử lý đồng thời toàn bộ chuỗi đầu vào nhờ cơ chế **Self-Attention**.

## 1.2 Cơ chế Self-Attention (Tự chú ý)
Self-Attention cho phép mô hình đánh giá mức độ liên quan giữa mỗi token với tất cả các token khác trong cùng một câu, bất kể khoảng cách xa hay gần.
- **Query ($Q$):** Đại diện cho thông tin mà token hiện tại đang tìm kiếm.
- **Key ($K$):** Đại diện cho "nhãn" hoặc đặc trưng của các token khác để so khớp với Query.
- **Value ($V$):** Nội dung thực tế của token sẽ được trích xuất nếu khớp.

Công thức tính Scaled Dot-Product Attention:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Trong đó $d_k$ là số chiều của vector Key, dùng để chuẩn hóa tích vô hướng nhằm tránh giá trị quá lớn làm bão hòa hàm softmax.

## 1.3 Multi-Head Attention & Grouped-Query Attention (GQA)
- **Multi-Head Attention (MHA):** Chia $Q, K, V$ thành nhiều "đầu" (heads) độc lập để mô hình học được nhiều mối quan hệ ngữ nghĩa khác nhau cùng lúc (ngữ pháp, ngữ cảnh, tham chiếu đại từ).
- **Grouped-Query Attention (GQA):** Kỹ thuật tối ưu được dùng trên các model hiện đại (Qwen2.5, Llama 3). Nhiều đầu Query dùng chung một cặp Key-Value, giúp **giảm đáng kể dung lượng KV Cache** và tăng tốc độ sinh chữ trên phần cứng có băng thông bộ nhớ giới hạn như iGPU Radeon 780M.

## 1.4 Quy trình hoạt động 2 giai đoạn của LLM
1. **Prefill (Xử lý Prompt):** Tính toán song song toàn bộ token đầu vào để tạo ma trận $K, V$ ban đầu. Giai đoạn này bị giới hạn bởi **sức mạnh tính toán thô (FLOPS)** của GPU.
2. **Decode (Sinh từng token):** Sinh tuần tự từng token một (Autoregressive). Mỗi bước phải đọc lại toàn bộ trọng số mô hình và KV Cache từ bộ nhớ. Giai đoạn này bị giới hạn bởi **băng thông bộ nhớ (Memory Bandwidth)**.
