# 💻 Phase 3: Tích hợp Local API & Trợ lý Lập trình VS Code

## 1. Kết nối Local LLM vào VS Code (Thay thế GitHub Copilot miễn phí)
Bạn có thể biến VS Code thành môi trường lập trình có AI hỗ trợ 100% offline:
1. Mở **VS Code** -> vào mục Extensions (`Ctrl + Shift + X`).
2. Cài đặt extension **Continue** (hoặc **Cline** nếu muốn AI tự động sửa nhiều file và chạy lệnh terminal).
3. Mở file cấu hình `config.yaml` của Continue (`~/.continue/config.yaml`) và dán cấu hình sau:

```yaml
name: ThinkBook Local AI
version: 1.0.0
schema: v1

models:
  - name: Qwen 2.5 Coder 14B (Chat & Refactor)
    provider: ollama
    model: qwen2.5-coder:14b
    roles:
      - chat
      - edit
      - apply

  - name: Qwen 2.5 Coder 7B (Autocomplete)
    provider: ollama
    model: qwen2.5-coder:7b
    roles:
      - autocomplete
```

---

## 2. Giao tiếp với Local LLM qua chuẩn OpenAI SDK
Ollama cung cấp sẵn endpoint tương thích 100% với thư viện `openai` tại `http://localhost:11434/v1`. Điều này giúp bạn viết code một lần và có thể chuyển đổi linh hoạt giữa Local LLM và Cloud API (GPT/Claude) chỉ bằng cách đổi `base_url`.

## 🧪 Bài tập thực hành Phase 3
Chạy ví dụ streaming response & code review tự động bằng Python:
```bash
python 03-api-and-coding/local_client.py
```
