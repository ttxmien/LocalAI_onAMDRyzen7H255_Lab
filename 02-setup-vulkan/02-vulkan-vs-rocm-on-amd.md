# 2. Vulkan vs. ROCm trên iGPU AMD Radeon 780M

## 2.1 ROCm (Radeon Open Compute) là gì?
- Là nền tảng tính toán GPU mã nguồn mở của AMD tương tự CUDA của NVIDIA.
- **Hạn chế trên Laptop Windows:** ROCm được thiết kế chủ yếu cho dòng card đồ họa rời (Radeon RX 7900/7800 XT) và card trung tâm dữ liệu (Instinct) trên hệ điều hành **Linux**. Trên Windows và đặc biệt là card tích hợp **Radeon 780M (gfx1103)**, việc cài đặt ROCm thường gặp lỗi thiếu thư viện HIP hoặc không nhận diện chính xác kiến trúc phần cứng.

## 2.2 Vulkan Compute — Lựa chọn tối ưu trên Windows
- **Vulkan** là API đồ họa và tính toán song song đa nền tảng thế hệ mới, được tích hợp sẵn trong bộ driver tiêu chuẩn **AMD Software: Adrenalin Edition** trên Windows 11.
- Backend Vulkan của `llama.cpp` / Ollama biên dịch các shader tính toán ma trận trực tiếp xuống 12 nhân RDNA 3 của Radeon 780M mà không cần cài thêm bất kỳ SDK phức tạp nào.
- **Ưu điểm vượt trội:**
  1. Hoạt động ổn định ngay lập tức sau khi bật `OLLAMA_VULKAN=1`.
  2. Tận dụng liền mạch toàn bộ vùng nhớ chia sẻ (Shared Memory) lên tới 24GB–28GB từ thanh RAM 32GB của hệ thống.
  3. Tốc độ suy luận (Decode) tương đương hoặc nhanh hơn ROCm trên các tác vụ kích thước batch nhỏ (single-user chat/coding).
