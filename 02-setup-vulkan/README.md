# 📚 Phase 2: Local Inference & AMD Optimization (Cài đặt Vulkan & Benchmark)

## 1. Tối ưu hóa iGPU AMD Radeon 780M trên Windows 11
Mặc định, các framework AI thường ưu tiên tối ưu cho CUDA của NVIDIA. Tuy nhiên, trên laptop AMD chạy Windows, bạn có thể ép toàn bộ tải suy luận dồn 100% vào iGPU Radeon 780M mà không cần dùng đến Linux hay thư viện ROCm phức tạp:

1. **Cấu hình BIOS (UMA Frame Buffer):** Khởi động máy, nhấn `F2` vào BIOS $\rightarrow$ tìm mục **UMA Frame Buffer Size** và chỉnh thành `8G` (cấp cứng 8GB VRAM tối thiểu cho iGPU, phần còn lại 24GB vẫn linh hoạt chia sẻ động).
2. **Kích hoạt Backend Vulkan:** Ollama hỗ trợ tăng tốc phần cứng thông qua **Vulkan Compute** (tích hợp sẵn trong Driver AMD Adrenalin).
3. **Thiết lập biến môi trường tối ưu:** Chạy PowerShell với quyền Administrator để kích hoạt cờ tăng tốc Vulkan và nén KV Cache:
   ```powershell
   .\scripts\setup_amd_env.ps1
   ```

---

## 2. Kiểm tra hiệu năng thực tế phần cứng
Sau khi cấu hình, luôn phải kiểm tra xem model đã chạy hoàn toàn trên GPU hay chưa:

- Mở Terminal và chạy model thử nghiệm:
  ```powershell
  ollama run qwen2.5-coder:7b
  ```
- Mở một cửa sổ Terminal khác và gõ lệnh kiểm tra trạng thái offload của Ollama:
  ```powershell
  ollama ps
  ```
  *(Nếu cột `PROCESSOR` hiển thị **100% GPU**, nghĩa là toàn bộ mô hình đã được nạp thành công vào Radeon 780M qua cổng Vulkan).*

---

## 🧪 Thực hành Phase 2
Chạy script Python đo đạc thông lượng thực tế (`tokens/sec`) và thời gian phản hồi đầu tiên (`TTFT`) trên chiếc ThinkBook của bạn:

```bash
python 02-setup-vulkan/benchmark_ollama.py
```