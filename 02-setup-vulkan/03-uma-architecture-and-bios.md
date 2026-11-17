# 3. Kiến trúc UMA (Unified Memory Architecture) & Tinh chỉnh BIOS

## 3.1 Cách hoạt động của bộ nhớ trên AMD Ryzen 7 H 255
Khác với máy tính dùng card rời có VRAM GDDR6 tách biệt, chip AMD Ryzen sử dụng **kiến trúc bộ nhớ hợp nhất (UMA)**:
- CPU (8 nhân Zen 4) và iGPU (Radeon 780M) cùng truy cập chung vào một vùng RAM vật lý **32GB LPDDR5x-7500**.
- **Lợi thế:** Không tốn thời gian copy dữ liệu qua lại qua khe PCIe giữa RAM hệ thống và VRAM; dung lượng bộ nhớ dành cho AI cực kỳ lớn.

## 3.2 Dedicated VRAM (UMA Frame Buffer) vs. Shared GPU Memory
Trong Windows Task Manager, bộ nhớ của Radeon 780M chia làm 2 phần:
1. **Dedicated GPU Memory (VRAM cấp cứng trong BIOS):** Vùng nhớ được dành riêng cố định cho GPU ngay khi khởi động máy (mặc định thường là 512MB hoặc 2GB). Hệ điều hành Windows không được phép lấy vùng này để chạy ứng dụng khác.
2. **Shared GPU Memory (VRAM chia sẻ động):** Windows cho phép GPU mượn tối đa **50% tổng dung lượng RAM hệ thống** (tức 16GB trên máy 32GB).

## 3.3 Tại sao nên chỉnh UMA Frame Buffer Size lên 8GB trong BIOS?
- Khi cộng **8GB Dedicated VRAM** + **12GB Shared Memory**, các trình quản lý GPU (như Vulkan driver và Ollama) sẽ nhận diện tổng dung lượng bộ nhớ khả dụng lên tới **20GB+** một cách ổn định, tránh tình trạng Ollama tưởng nhầm máy chỉ có 2GB VRAM và đẩy toàn bộ model sang chạy bằng CPU chậm chạp.
- Với 32GB RAM, sau khi cấp cứng 8GB cho GPU, Windows vẫn còn nguyên **24GB RAM** — quá dư dả để chạy mượt IDE, Docker và trình duyệt.
