<div align="center">
  <a href="README.md"><b>English</b></a> | 
  <a href="README.vi.md"><b>Tiếng Việt</b></a>
</div>

---

# 🧠 Local AI Lab — AMD Ryzen 7 H 255 / 32GB RAM / Radeon 780M

> Không gian thực hành AI Engineering dành cho Local LLM, hệ thống RAG, AI Agent và các quy trình tối ưu năng suất lập trình, chạy hoàn toàn offline trên phần cứng AMD phổ thông.

![Hardware](https://img.shields.io/badge/Hardware-ThinkBook_14_G8%2B_(21VR)-blue?style=flat-square)
![CPU](https://img.shields.io/badge/CPU-Ryzen_7_H_255-red?style=flat-square)
![GPU](https://img.shields.io/badge/iGPU-Radeon_780M_(Vulkan)-orange?style=flat-square)
![RAM](https://img.shields.io/badge/RAM-32GB_LPDDR5x_7500MT%2Fs-green?style=flat-square)

Repository này lưu trữ lộ trình học tập bài bản, các script tối ưu phần cứng, kết quả benchmark và các dự án thực hành về **Local LLM & AI Engineering**, được thiết kế riêng cho **Lenovo ThinkBook 14 G8+ (21VR)**:

| Thành phần | Thông số kỹ thuật | Vai trò xử lý AI |
| :--- | :--- | :--- |
| **CPU** | AMD Ryzen 7 H 255 (8C / 16T, Zen 4) | Tiền xử lý dữ liệu, chunking, điều phối luồng và chạy dự phòng (hybrid fallback) |
| **RAM** | 32GB LPDDR5x 7500 MT/s | Bộ nhớ chung (Shared Unified Memory) băng thông cao (gánh được tới các model MoE 30B) |
| **GPU** | AMD Radeon 780M (RDNA 3, 12 CUs) | Nhân tăng tốc suy luận (inference) chính qua Vulkan backend (`100% GPU` offload) |
| **Storage** | 1TB NVMe SSD | Nạp trọng số model (GGUF) tốc độ cao và lưu trữ Vector DB cục bộ |
| **OS** | Windows 11 Pro | Môi trường phát triển Ollama + Vulkan gốc / WSL2 |

---

## 🎯 Mục tiêu

Xây dựng nền tảng kiến thức vững chắc và kỹ năng thực chiến để triển khai các hệ thống AI cục bộ phục vụ công việc phát triển phần mềm, chẩn đoán hệ thống Automotive và quy trình DevOps hằng ngày:

- **Bản chất LLM (LLM Internals):** Nắm vững cơ chế Transformer, Quantization (`Q4_K_M`, `Q8_0`), KV Cache và nút thắt băng thông bộ nhớ (memory-bandwidth bottlenecks) trên iGPU.
- **Tối ưu suy luận trên AMD:** Cấu hình tăng tốc Vulkan, Flash Attention và chỉnh dung lượng UMA Frame Buffer trong BIOS cho Radeon 780M.
- **Tích hợp IDE:** Triển khai trợ lý lập trình AI miễn phí, chạy offline ngay trong VS Code (chat, refactor code và autocomplete tốc độ cao).
- **Technical RAG Offline:** Xây dựng luồng truy xuất dữ liệu từ file PDF, tài liệu kiến trúc, dữ liệu xuất từ Jira và báo cáo phân tích nguyên nhân gốc (RCA).
- **AI Agent tự hành:** Ứng dụng Tool Calling (Function Calling) và vòng lặp ReAct để tự động phân tích log (GNSS/DLT/CI-CD) và tự động hóa tác vụ hệ thống.

---

## 🏗️ Kiến trúc mục tiêu (End-State Architecture)

```text
                       ┌─────────────────────────┐
                       │         VS Code         │
                       │ Continue / Cline / Roo  │
                       └────────────┬────────────┘
                                    │ OpenAI-Compatible API
                                    ▼
                       ┌─────────────────────────┐
                       │     Ollama (Vulkan)     │
                       │ Qwen2.5 / Gemma3 / Qwen3│
                       └────────────┬────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
┌─────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│ Coding Assistant│       │  Local RAG Base  │       │  DevOps / Log    │
│                 │       │ (ChromaDB/FAISS) │       │     AI Agent     │
└────────┬────────┘       └────────┬─────────┘       └────────┬─────────┘
         │                         │                          │
         ▼                         ▼                          ▼
 • Sinh code (Code Gen)    • Tài liệu kỹ thuật        • Tool Calling
 • Refactoring             • Dữ liệu Jira & RCA       • Log GNSS / DLT
 • Viết Unit Test          • Hướng dẫn nội bộ         • Sửa lỗi Build & CI/CD
```

---

## 🗺️ Lộ trình học tập (Sprint 15 ngày)

| Giai đoạn | Thư mục | Lý thuyết cốt lõi | Thực hành (Hands-On) | Kết quả đạt được | Thời gian |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1**<br>Nền tảng | `01-foundations/` | Transformers, Tokenization, Quantization (GGUF), KV Cache, Memory Bandwidth, Dense vs. MoE | Tính toán mức chiếm dụng RAM/VRAM, so sánh `Q4_K_M` với `Q8_0`, phân tích thông lượng lý thuyết trên 780M | Quantization Cheat Sheet & công cụ tính bộ nhớ | Ngày 1–2 |
| **Phase 2**<br>Suy luận trên AMD | `02-setup-vulkan/` | Inference Engines (`llama.cpp`, Ollama, LM Studio), Vulkan vs. ROCm, kiến trúc UMA | Cài đặt Ollama & LM Studio, tinh chỉnh BIOS UMA buffer, benchmark các model 7B, 14B và 30B-A3B | Môi trường suy luận tăng tốc Vulkan ổn định | Ngày 3–4 |
| **Phase 3**<br>API & Lập trình | `03-api-and-coding/` | OpenAI REST API, Streaming, System Prompts, Temperature, Context Length (`num_ctx`) | Viết client Python hỗ trợ streaming, cấu hình Continue/Cline trong VS Code cho chat & autocomplete | Trợ lý lập trình cục bộ chạy offline | Ngày 5–7 |
| **Phase 4**<br>Local RAG | `04-rag-local/` | Embeddings, ChromaDB, FAISS, chiến lược Chunking, Hybrid Search (BM25 + Vector) | Nạp dữ liệu PDF, Markdown và file xuất Jira để xây dựng trợ lý hỏi đáp có trích dẫn nguồn | Hệ thống Technical RAG Offline | Ngày 8–11 |
| **Phase 5**<br>AI Agents | `05-agents-devops/` | Function Calling, Tool Use, vòng lặp ReAct, Structured Outputs (JSON Schema), MCP | Xây dựng Agent kiểm tra sức khỏe hệ thống, phân tích log GNSS/build và xuất báo cáo RCA | DevOps & Log Agent tự hành | Ngày 12–15 |

---

## 📁 Cấu trúc Repository

```text
LocalAI_onAMDRyzen7H255_Lab/
├── README.md
├── README.vi.md
├── requirements.txt
├── .gitignore
├── docs/                       # Tài liệu hướng dẫn tối ưu phần cứng & ghi chú kiến trúc
├── scripts/                    # Script PowerShell thiết lập môi trường & kiểm tra phần cứng
├── 01-foundations/             # Ghi chú lý thuyết, bài tập quantization & script tính bộ nhớ
├── 02-setup-vulkan/            # Cấu hình Ollama/LM Studio & script đo tốc độ (benchmark)
├── 03-api-and-coding/          # Python client chuẩn OpenAI & file cấu hình VS Code
├── 04-rag-local/               # Luồng tạo embedding, ChromaDB/FAISS & bài lab nạp dữ liệu
├── 05-agents-devops/           # Schema gọi hàm (tool-calling), trình đọc log & DevOps agent
├── benchmarks/                 # Nhật ký ghi lại thông số hiệu năng qua các bản cập nhật model
└── playground/                 # Nơi thử nghiệm script và nháp ý tưởng
```

---

## 🚀 Bắt đầu nhanh (Quick Start)

### 1. Clone & thiết lập môi trường Python

```powershell
git clone https://github.com/ttxmien/LocalAI_onAMDRyzen7H255_Lab.git
cd LocalAI_onAMDRyzen7H255_Lab

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Cài đặt Ollama & tải các model khuyến nghị

```powershell
winget install Ollama.Ollama
ollama --version

# Tải các model cốt lõi tối ưu cho 32GB Unified Memory
ollama pull qwen2.5-coder:14b    # Model chính cho lập trình & DevOps (~9.0 GB)
ollama pull qwen2.5-coder:7b     # Autocomplete siêu tốc trong IDE (~4.7 GB)
ollama pull gemma3:12b           # Chat đa năng & tiếng Việt tự nhiên (~8.1 GB)
ollama pull qwen3:30b-a3b        # Model MoE thông minh cao (~18.5 GB)
ollama pull nomic-embed-text     # Model embedding cục bộ cho RAG (~274 MB)
```

### 3. Cấu hình môi trường AMD Vulkan

Mở PowerShell với quyền **Administrator** để thiết lập các biến tối ưu cho Vulkan và KV Cache (`OLLAMA_VULKAN=1`, `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`):

```powershell
.\scripts\setup_amd_env.ps1
```

*(Khởi động lại Ollama từ khay hệ thống sau khi chạy script, sau đó kiểm tra mức độ gánh tải của GPU bằng lệnh `ollama ps` trong lúc model đang trả lời).*

---

## ⚙️ Hướng dẫn tối ưu AMD Radeon 780M

- **Tinh chỉnh BIOS:** Vào BIOS (nhấn `F2` lúc khởi động) $\rightarrow$ `Configuration` $\rightarrow$ Chỉnh **UMA Frame Buffer Size** thành `8G` (cấp cứng 8GB VRAM trong khi vẫn chừa lại 24GB cho Windows/Docker) hoặc để `Auto` để hệ thống tự điều phối linh hoạt.
- **Chế độ nguồn:** Nhấn `Fn + Q` để chuyển ThinkBook sang **Performance Mode** khi chạy suy luận nặng hoặc đo benchmark.
- **Kiểm tra Vulkan & GPU Offload:**

```powershell
vulkaninfo --summary   # Xác nhận hỗ trợ AMD Radeon 780M Vulkan 1.3
ollama ps              # Xác nhận cột PROCESSOR hiển thị "100% GPU"
```

---

## 🤖 Ma trận Model khuyến nghị (Điểm ngọt cho 32GB RAM)

| Nhu cầu sử dụng | Model | Mức nén (Quant) | Bộ nhớ ước tính | Lý do phù hợp với phần cứng này |
| :--- | :--- | :--- | :--- | :--- |
| **Lập trình & DevOps chính** | `qwen2.5-coder:14b` | `Q4_K_M` | ~9.5 GB | Cân bằng tốt nhất giữa độ chính xác code (YAML/C++/Python) và tốc độ |
| **Autocomplete trong IDE** | `qwen2.5-coder:7b` | `Q8_0` | ~8.2 GB | Độ chính xác gần như nguyên bản với độ trễ gợi ý code dưới 1 giây |
| **Chat đa năng / Tiếng Việt** | `gemma3:12b` | `Q4_K_M` | ~8.5 GB | Diễn đạt tiếng Việt tự nhiên và tóm tắt văn bản rất tốt |
| **Suy luận logic sâu** | `qwen3:14b` / `deepseek-r1:14b` | `Q4_K_M` | ~9.2 GB | Suy luận từng bước (chain-of-thought) cho debug phức tạp và giải thuật |
| **Thông minh tối đa (MoE)** | `qwen3:30b-a3b` | `Q4_K_M` | ~19.0 GB | Tổng 30B tham số (nằm gọn trong 32GB RAM) nhưng chỉ kích hoạt 3B mỗi token |
| **Tạo Vector (RAG Embeddings)** | `nomic-embed-text` | `F16` | ~0.3 GB | Tạo embedding ngữ nghĩa nhanh và chính xác cho truy xuất tài liệu cục bộ |

---

## 📊 Kết quả Benchmark

> *Đo trên Windows 11 Pro (Chế độ Performance `Fn+Q`, `OLLAMA_VULKAN=1`, `num_ctx=8192`). Cập nhật số liệu thực tế sau khi chạy.*

| Model | Quant | Context | Peak RAM | Đọc Prompt (t/s) | Sinh chữ (t/s) | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `qwen2.5-coder:7b` | `Q8_0` | 8192 | ~8.5 GB | *TBD* | *TBD* | Autocomplete trong IDE |
| `qwen2.5-coder:14b` | `Q4_K_M` | 8192 | ~9.8 GB | *TBD* | *TBD* | Model chính cho code & agent |
| `gemma3:12b` | `Q4_K_M` | 8192 | ~8.8 GB | *TBD* | *TBD* | Hỏi đáp đa năng |
| `qwen3:14b` | `Q4_K_M` | 8192 | ~9.6 GB | *TBD* | *TBD* | Tác vụ suy luận sâu |
| `qwen3:30b-a3b` | `Q4_K_M` | 8192 | ~19.2 GB | *TBD* | *TBD* | Kiểm thử MoE thông lượng cao |

---

## 🛠️ Các dự án thực tế (Capstone Projects)

1. **Local Coding Assistant:** Trợ lý lập trình offline trong VS Code (Continue/Cline) hỗ trợ giải thích code, refactor, viết commit message và sinh unit test.
2. **Offline Technical Q&A (RAG):** Tìm kiếm ngữ nghĩa và hỏi đáp bám sát tài liệu trên file PDF, tài liệu đặc tả Markdown và tài liệu kiến trúc bằng ChromaDB + `nomic-embed-text`.
3. **GNSS & Diagnostic Log Analyzer:** Trình phân tích tự động và tóm tắt bằng LLM cho log DLT, dữ liệu UBX, gói tin PCAP và cơ sở dữ liệu SQLite để đẩy nhanh quá trình tìm nguyên nhân gốc (RCA).
4. **Build & CI/CD Failure Assistant:** Phân tích lỗi biên dịch/linker và log pipeline để chỉ ra nguyên nhân gốc và đề xuất hướng khắc phục cụ thể.
5. **Automotive Knowledge Assistant:** Hệ thống RAG lập chỉ mục dữ liệu xuất từ Jira, báo cáo RCA và tài liệu hướng dẫn hệ thống nội bộ giúp tra cứu và debug nhanh hơn.
6. **Local DevOps Copilot:** Agent có khả năng gọi công cụ (tool-calling) để kiểm tra thông số hệ thống, đọc log triển khai và tạo tài liệu hướng dẫn xử lý sự cố (runbook).

---

## 📚 Tài nguyên học tập chọn lọc

- **Nền tảng LLM:** *Hands-On Large Language Models* (Alammar & Grootendorst), *Build a Large Language Model (From Scratch)* (Raschka), Stanford CS25.
- **RAG & Truy xuất dữ liệu:** Tài liệu ChromaDB, FAISS Wiki, hướng dẫn Retrieval của LlamaIndex & LangChain (Chunking, Hybrid Search, Re-ranking).
- **Agents & Giao thức:** *Building Effective Agents* của Anthropic, tài liệu OpenAI Function Calling, đặc tả Model Context Protocol (MCP).
- **Inference Runtimes:** `llama.cpp`, Ollama, LM Studio, ONNX Runtime / DirectML.

---

## ✅ Theo dõi tiến độ (Progress Tracker)

- [ ] **Phase 1 — Nền tảng:** Hoàn thành ghi chú lý thuyết, bảng tra cứu quantization và công cụ tính bộ nhớ.
- [ ] **Phase 2 — Suy luận cục bộ:** Cấu hình Vulkan backend, tinh chỉnh BIOS UMA buffer và ghi lại kết quả benchmark cơ sở.
- [ ] **Phase 3 — API & Lập trình:** Xây dựng Python client hỗ trợ streaming và tích hợp Ollama vào VS Code.
- [ ] **Phase 4 — Local RAG:** Xây dựng luồng nạp dữ liệu ChromaDB và chatbot hỏi đáp tài liệu kỹ thuật offline.
- [ ] **Phase 5 — AI Agents:** Triển khai Function Calling / MCP tools để phân tích log và tự động hóa tác vụ DevOps.