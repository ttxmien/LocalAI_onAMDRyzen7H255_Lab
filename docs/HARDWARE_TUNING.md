# ⚙️ Hướng dẫn Tối ưu Phần cứng ThinkBook 14 G8+ (21VR) cho Local AI

## 1. Hiểu đúng về kiến trúc bộ nhớ trên Ryzen 7 H 255
- Máy của bạn **không có NPU** (nhân AI rời), nhưng sở hữu **iGPU AMD Radeon 780M (12 CUs RDNA 3)** kết hợp với **32GB RAM LPDDR5x 7500MT/s**.
- **Tại sao băng thông RAM lại quan trọng nhất?**
  Tốc độ sinh chữ (Token Generation / Decode) của LLM bị giới hạn bởi tốc độ đọc trọng số từ bộ nhớ vào nhân tính toán (*Memory-Bandwidth Bound*). RAM LPDDR5x-7500 của ThinkBook 14 G8+ đạt băng thông lý thuyết ~120 GB/s — nhanh gấp đôi các laptop dùng DDR5-5600 thường, giúp Radeon 780M đạt tốc độ ~15–22 tokens/giây với model 14B.

---

## 2. Tinh chỉnh BIOS (Tăng UMA Frame Buffer Size)
Mặc định, Windows chỉ cấp cứng 512MB hoặc 2GB VRAM cho Radeon 780M, phần còn lại cấp động (Shared Memory). Một số framework AI kiểm tra VRAM tĩnh trước khi load model và sẽ báo lỗi thiếu bộ nhớ nếu thấy VRAM cứng quá thấp.

**Các bước chỉnh trong BIOS:**
1. Tắt hoàn toàn máy (hoặc Restart).
2. Khi logo Lenovo vừa hiện lên, nhấn liên tục phím **`F2`** (hoặc `Fn + F2`) để vào BIOS.
3. Chuyển sang tab **`Configuration`** (hoặc vào *More Settings* -> *Configuration*).
4. Tìm mục **`UMA Frame Buffer Size`** (mặc định thường là `Auto` hoặc `2G`).
5. Đổi thành **`4G`** hoặc **`8G`** (Khuyến nghị **`8G`** vì máy bạn có tới 32GB RAM, vẫn còn dư 24GB cho Windows và Docker/VS Code).
6. Nhấn **`F10`** -> chọn **`Yes`** để lưu và khởi động lại.

---

## 3. Tối ưu Windows Power Plan & AMD Adrenalin Driver
1. **Cập nhật Driver GPU mới nhất:** Cài đặt phần mềm **AMD Software: Adrenalin Edition** để đảm bảo hỗ trợ đầy đủ tập lệnh **Vulkan 1.3** mới nhất.
2. **Chế độ nguồn khi chạy AI nặng:**
   - Nhấn tổ hợp phím **`Fn + Q`** trên bàn phím ThinkBook để chuyển sang chế độ **Performance (Hiệu năng cao)** khi chạy benchmark hoặc xử lý tác vụ lớn.
   - Khi dùng pin di động, chuyển về **Intelligent Cooling / Balance** và ưu tiên dùng các model 7B–8B.

---

## 4. Cấu hình biến môi trường cho Ollama (Bật Vulkan)
Trên card tích hợp Radeon 780M, backend **Vulkan** ổn định và tương thích tốt hơn ROCm trên Windows.
Bạn có thể chạy file `scripts/setup_amd_env.ps1` trong repo này để tự động thiết lập:
- `OLLAMA_VULKAN=1`: Ép Ollama sử dụng Vulkan GPU acceleration.
- `OLLAMA_FLASH_ATTENTION=1`: Giảm tiêu thụ VRAM khi xử lý ngữ cảnh dài (Context dài).
- `OLLAMA_KV_CACHE_TYPE=q8_0`: Nén KV Cache xuống 8-bit, tiết kiệm ~40% bộ nhớ khi đọc file code/log dài mà không giảm chất lượng.
- `OLLAMA_MAX_LOADED_MODELS=1`: Chỉ giữ 1 model trong RAM tại một thời điểm để tránh tràn bộ nhớ.
