# 🧠 ThinkBook Local AI Lab (Ryzen 7 H 255 / 32GB / Radeon 780M)

Lưu trữ tài liệu, lộ trình học tập từ lý thuyết đến thực hành, script tối ưu phần cứng và các dự án ứng dụng **Local LLM / AI Engineering** được thiết kế và tinh chỉnh riêng cho cấu hình **Lenovo ThinkBook 14 G8+ (21VR)**:
- **CPU:** AMD Ryzen 7 H 255 (8 nhân / 16 luồng, Zen 4)
- **RAM:** 32GB LPDDR5x 7500MT/s (Shared Unified Memory)
- **GPU:** AMD Radeon 780M (12 nhân RDNA 3 — tăng tốc qua Vulkan / ROCm)
- **Storage:** 1TB NVMe SSD

---

## 🎯 Mục tiêu
1. Kiến thức nền tảng về LLM, Quantization (GGUF), Context Window, KV Cache và kiến trúc Inference trên iGPU AMD.
2. Cấu hình môi trường chạy Local AI tối ưu nhất trên Windows (tận dụng 32GB RAM tốc độ cao & Vulkan backend).
3. Tích hợp AI cục bộ vào quy trình lập trình (VS Code) và tự động hóa tác vụ kỹ thuật / DevOps (phân tích log, sinh script, CI/CD).
4. Xây dựng hệ thống **RAG (Retrieval-Augmented Generation)** đọc tài liệu kỹ thuật nội bộ hoàn toàn offline.
5. Phát triển **Local AI Agent** có khả năng gọi công cụ (Function Calling / Tool Use).

---

## 🗺️ Lộ trình Học tập & Thực hành (5 Giai đoạn)

| Giai đoạn | Thư mục | Nội dung Lý thuyết | Bài tập Thực hành | Thời lượng gợi ý |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | `01-foundations/` | Kiến trúc Transformer, Tokenization, Quantization (`Q4_K_M`, `Q8_0`), VRAM vs Bandwidth, MoE vs Dense. | Tính toán dung lượng bộ nhớ & benchmark lý thuyết cho Radeon 780M. | Ngày 1 – 2 |
| **Phase 2** | `02-setup-vulkan/` | Inference Engines (`llama.cpp`, Ollama, LM Studio), Vulkan vs ROCm trên AMD iGPU, UMA Frame Buffer. | Cài đặt Ollama/LM Studio, tinh chỉnh BIOS & biến môi trường Vulkan, chạy model 14B & 30B-A3B. | Ngày 3 – 4 |
| **Phase 3** | `03-api-and-coding/` | Local REST API (chuẩn OpenAI), Streaming, System Prompt, Temperature, Context Length (`num_ctx`). | Gọi API bằng Python, tích hợp trợ lý code cục bộ vào VS Code (Continue/Cline). | Ngày 5 – 7 |
| **Phase 4** | `04-rag-local/` | Embeddings, Vector Database (ChromaDB/FAISS), Chunking strategies, Cosine Similarity. | Xây dựng chatbot hỏi đáp tài liệu kỹ thuật/log nội bộ 100% offline. | Ngày 8 – 11 |
| **Phase 5** | `05-agents-devops/` | Tool Calling (Function Calling), ReAct Pattern, Structured Outputs (JSON Schema). | Tạo AI Agent tự động đọc file log hệ thống, kiểm tra tài nguyên và xuất báo cáo. | Ngày 12 – 15 |

---

## 🚀 Quick Start

1. **Clone và mở thư mục dự án:**
   ```bash
   git clone https://github.com/ttxmien/LocalAI_onAMDRyzen7H255_Lab.git
   cd LocalAI_onAMDRyzen7H255_Lab
   ```
2. **Tạo môi trường Python ảo:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Chạy script kiểm tra phần cứng & tối ưu môi trường Windows cho AMD:**
   Mở PowerShell với quyền Administrator và chạy:
   ```powershell
   .\scripts\setup_amd_env.ps1
   ```
4. **Follow theo từng thư mục từ `01-foundations` đến `05-agents-devops`.**

---

## 📊 Tham khảo các model "Chân ái" cho ThinkBook 14 G8+ (32GB RAM)

- **Lập trình & DevOps chính:** `qwen2.5-coder:14b` (`Q4_K_M` ~9GB)
- **Autocomplete siêu tốc trong VS Code:** `qwen2.5-coder:7b` (`Q8_0` ~8.1GB)
- **Chat đa năng & Tiếng Việt tự nhiên:** `gemma3:12b` (`Q4_K_M` ~8.5GB)
- **Suy luận logic sâu (Reasoning):** `deepseek-r1:14b` hoặc `qwen3:14b`
- **Hiệu năng tối đa (MoE - 30B tổng, 3B kích hoạt):** `qwen3:30b-a3b` (~18.5GB RAM, tốc độ nhanh như 4B)
