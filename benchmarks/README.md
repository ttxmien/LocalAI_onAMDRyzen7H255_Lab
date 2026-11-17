# 📊 Benchmark (ThinkBook 14 G8+ 21VR)

Ghi lại kết quả thực nghiệm khi thay đổi các thông số phần cứng/phần mềm để theo dõi quá trình tối ưu hóa:

| Ngày | Model | Quant | Backend | UMA VRAM (BIOS) | Flash Attn | Tốc độ (tokens/s) | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mẫu | `qwen2.5-coder:14b` | `Q4_K_M` | Vulkan | 8GB | ON | ~15.5 t/s | Chế độ Performance (`Fn+Q`) |
| Mẫu | `qwen3:30b-a3b` | `Q4_K_M` | Vulkan | 8GB | ON | ~24.0 t/s | Chiếm ~19GB RAM, phản hồi cực nhanh |
