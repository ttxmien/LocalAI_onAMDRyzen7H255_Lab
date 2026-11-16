# 🛠️ Phase 2: Cài đặt & Tối ưu Vulkan trên AMD Radeon 780M

## 1. Cài đặt Ollama trên Windows
1. Tải bản cài đặt chính thức từ [ollama.com/download](https://ollama.com/download).
2. Chạy script tối ưu biến môi trường AMD Vulkan (từ thư mục gốc repo):
   ```powershell
   .\scripts\setup_amd_env.ps1
   ```
3. **Quan trọng:** Chuột phải vào biểu tượng Ollama dưới khay hệ thống (System Tray) -> chọn **Quit Ollama**, sau đó mở lại **Ollama** từ Start Menu để nhận các biến môi trường Vulkan mới.

---

## 2. Tải bộ 3 Model chuẩn cho ThinkBook 14 G8+
Mở Terminal (PowerShell) và tải các model sau:

```powershell
# 1. Model lập trình & DevOps chủ lực (14B)
ollama pull qwen2.5-coder:14b

# 2. Model chat đa năng & tiếng Việt mượt (12B)
ollama pull gemma3:12b

# 3. Model MoE hiệu năng cao (30B tổng, 3B kích hoạt)
ollama pull qwen3:30b-a3b
```

---

## 3. Kiểm tra xem GPU Radeon 780M đã gánh tải chưa
Trong khi cho model trả lời một câu hỏi dài, mở một cửa sổ Terminal khác và gõ:
```powershell
ollama ps
```
Nếu cột `PROCESSOR` hiển thị **`100% GPU`** (hoặc `85%/15% GPU/CPU`), xin chúc mừng — Radeon 780M của bạn đang hoạt động hết công suất!

---

## 🧪 Bài tập thực hành Phase 2: Đo tốc độ thực tế (Benchmark)
Chạy script đo tốc độ sinh chữ (*tokens/giây*) và thời gian phản hồi đầu tiên (*TTFT - Time To First Token*) trên máy của bạn:
```bash
python 02-setup-vulkan/benchmark_ollama.py
```
