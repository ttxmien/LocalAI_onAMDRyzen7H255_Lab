# 5. Kiến trúc Dense Model vs. MoE (Mixture of Experts)

## 5.1 Dense Model (Mô hình đặc)
Trong kiến trúc truyền thống (như Qwen2.5-14B, Gemma-3-12B):
- Toàn bộ các tham số trong mạng Feed-Forward Network (FFN) đều được kích hoạt cho **mọi token** đầu vào.
- **Ưu điểm:** Kiến trúc đơn giản, ổn định, dễ tối ưu.
- **Nhược điểm:** Model càng lớn (ví dụ 32B) thì lượng dữ liệu phải đọc qua bus bộ nhớ cho mỗi token càng khổng lồ, khiến tốc độ sinh chữ trên iGPU bị chậm.

## 5.2 MoE (Mixture of Experts — Hỗn hợp Chuyên gia)
Trong kiến trúc MoE (như **Qwen3-30B-A3B**, Mixtral):
- Lớp FFN được chia thành nhiều mạng con độc lập gọi là các **Experts** (ví dụ: 128 experts).
- Một mạng nhỏ gọi là **Router (Gating Network)** sẽ phân tích từng token và chỉ chọn ra **Top-K experts** (ví dụ: 8 experts, tương đương **3B tham số hoạt động**) để xử lý token đó.

## 5.3 Tại sao MoE là "vũ khí bí mật" cho Laptop 32GB RAM?
Xét mô hình **Qwen3-30B-A3B**:
- **Tổng tham số (Total Parameters):** 30.5 tỷ tham số $ightarrow$ Cần **~18.5 GB RAM** để lưu trữ toàn bộ kiến thức. Các laptop 16GB RAM hoặc GPU rời 8GB/16GB VRAM không thể chứa nổi.
- **Tham số kích hoạt (Active Parameters):** Chỉ **3.3 tỷ tham số** mỗi token $ightarrow$ Mỗi bước sinh chữ GPU chỉ cần đọc ~2 GB trọng số qua bus bộ nhớ.
- **Kết quả:** ThinkBook 32GB RAM của bạn vừa đủ sức chứa toàn bộ kho kiến thức 30B, vừa đạt tốc độ phản hồi nhanh ngang ngửa một model 3B–4B!
