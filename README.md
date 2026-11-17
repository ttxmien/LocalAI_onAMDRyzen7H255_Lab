# 🧠 Local AI Lab (Ryzen 7H 255 / 32GB / Radeon 780M)

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

## 📊 Một số model "Chân ái" cho ThinkBook 14 G8+ (32GB RAM)

- **Lập trình & DevOps chính:** `qwen2.5-coder:14b` (`Q4_K_M` ~9GB)
- **Autocomplete siêu tốc trong VS Code:** `qwen2.5-coder:7b` (`Q8_0` ~8.1GB)
- **Chat đa năng & Tiếng Việt tự nhiên:** `gemma3:12b` (`Q4_K_M` ~8.5GB)
- **Suy luận logic sâu (Reasoning):** `deepseek-r1:14b` hoặc `qwen3:14b`
- **Hiệu năng tối đa (MoE - 30B tổng, 3B kích hoạt):** `qwen3:30b-a3b` (~18.5GB RAM, tốc độ nhanh như 4B)







# 🧠 Local AI Lab (Ryzen 7 H 255 / 32GB RAM / Radeon 780M)

> A practical AI Engineering playground for Local LLMs, RAG systems, AI Agents, and developer productivity workflows running entirely on consumer AMD hardware.

Lưu trữ tài liệu, lộ trình học tập, benchmark, script tối ưu phần cứng và các dự án thực hành về **Local LLM / AI Engineering** được thiết kế riêng cho:

**Lenovo ThinkBook 14 G8+ (21VR)**

| Component | Specification |
|------------|------------|
| CPU | AMD Ryzen 7 H 255 (8C / 16T, Zen 4) |
| RAM | 32GB LPDDR5X 7500 MT/s |
| GPU | AMD Radeon 780M (RDNA3, 12 CUs) |
| Storage | 1TB NVMe SSD |
| OS | Windows 11 Pro |

---

# 🎯 Objectives

Mục tiêu của repository này là xây dựng nền tảng kiến thức và kinh nghiệm thực chiến để phát triển các hệ thống AI cục bộ phục vụ công việc kỹ thuật hàng ngày.

### Sau khi hoàn thành toàn bộ roadmap, bạn sẽ có khả năng:

✅ Hiểu cách hoạt động của Large Language Models (LLMs)

✅ Triển khai và tối ưu Local LLM trên AMD iGPU

✅ Tích hợp AI vào VS Code và quy trình phát triển phần mềm

✅ Xây dựng hệ thống RAG đọc tài liệu nội bộ hoàn toàn offline

✅ Tạo AI Agent có khả năng Tool Calling

✅ Tự động phân tích log, sinh script, hỗ trợ DevOps

✅ Xây dựng trợ lý kỹ thuật cá nhân chạy hoàn toàn cục bộ

---

# 🏗️ End-State Architecture

Mục tiêu cuối cùng của lab này là xây dựng hệ sinh thái AI cục bộ như sau:

```text
                          ┌─────────────────┐
                          │    VS Code      │
                          │ Continue / Cline│
                          └────────┬────────┘
                                   │
                     OpenAI Compatible API
                                   │
                                   ▼

                        ┌───────────────────┐
                        │      Ollama       │
                        │ Qwen / Gemma / R1 │
                        └─────────┬─────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼

    Coding Assistant       RAG Knowledge Base      AI Agent

        │                     │                    │

        ▼                     ▼                    ▼

 Source Code          Technical Documents      Tool Calling

 Jira Tickets         PDF / Markdown           Scripts

 Build Logs           RCA Reports              DevOps Tasks

 GNSS Logs            Internal Guides          System Tasks
```

---

# 🗺️ Learning Roadmap

| Phase | Directory | Theory | Hands-On | Deliverables | Timeline |
|---------|---------|---------|---------|---------|---------|
| **Phase 1**<br>Foundations | `01-foundations/` | Transformer, Attention, Tokens, Context Window, Quantization, GGUF, KV Cache, Memory Bandwidth, Dense vs MoE | Tính toán RAM requirement, so sánh Q4_K_M vs Q8_0, phân tích hiệu năng lý thuyết trên Radeon 780M | LLM Notes, Quantization Cheat Sheet, Memory Planning Worksheet | Day 1-2 |
| **Phase 2**<br>Local Inference & AMD Optimization | `02-setup-vulkan/` | Ollama, llama.cpp, LM Studio, Vulkan, ROCm, UMA Architecture, Context Window Internals | Cài đặt Ollama & LM Studio, cấu hình Vulkan, tối ưu BIOS UMA, benchmark 7B/14B/30B-A3B | Hệ thống Local LLM chạy ổn định trên Radeon 780M | Day 3-4 |
| **Phase 3**<br>APIs & AI Coding Assistant | `03-api-and-coding/` | OpenAI API, Chat Completion, Streaming, System Prompt, Temperature, Context Engineering | Viết chatbot Python, tích hợp VS Code (Continue/Cline/Roo), xây coding assistant | Local Coding Assistant chạy hoàn toàn offline | Day 5-7 |
| **Phase 4**<br>Local RAG Systems | `04-rag-local/` | Embeddings, ChromaDB, FAISS, Chunking, BM25, Hybrid Search, Evaluation Metrics | Xây dựng chatbot đọc PDF, Markdown, Jira Export, tài liệu nội bộ | Local Technical RAG Assistant | Day 8-11 |
| **Phase 5**<br>AI Agents & Automation | `05-agents-devops/` | Function Calling, Tool Use, ReAct, MCP, Structured Output, Agent Memory | Tạo Agent đọc log, chạy script, phân tích lỗi build, sinh báo cáo | DevOps Agent, Technical Assistant | Day 12-15 |

---

# 📁 Repository Structure

```text
LocalAI_onAMDRyzen7H255_Lab/

├── README.md
│
├── 01-foundations/
│   ├── notes/
│   ├── worksheets/
│   └── exercises/
│
├── 02-setup-vulkan/
│   ├── installation/
│   ├── tuning/
│   └── benchmarks/
│
├── 03-api-and-coding/
│   ├── openai-api/
│   ├── vscode/
│   └── assistants/
│
├── 04-rag-local/
│   ├── embeddings/
│   ├── chromadb/
│   ├── faiss/
│   ├── ingestion/
│   └── projects/
│
├── 05-agents-devops/
│   ├── tools/
│   ├── workflows/
│   └── projects/
│
├── benchmarks/
│
├── docs/
│
├── playground/
│
├── resources/
│
└── scripts/
```

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/ttxmien/LocalAI_onAMDRyzen7H255_Lab.git

cd LocalAI_onAMDRyzen7H255_Lab
```

---

## 2. Create Virtual Environment

```powershell
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 3. Install Ollama

Using Winget:

```powershell
winget install Ollama.Ollama
```

Verify installation:

```powershell
ollama --version
```

---

## 4. Download Recommended Models

```powershell
ollama pull qwen2.5-coder:14b

ollama pull qwen2.5-coder:7b

ollama pull gemma3:12b

ollama pull qwen3:30b-a3b

ollama pull nomic-embed-text
```

---

## 5. Verify Ollama

```powershell
ollama run qwen2.5-coder:7b
```

Expected:

```text
>>> Write hello world in Python
```

---

## 6. Optimize AMD Environment

Run PowerShell as Administrator:

```powershell
.\scripts\setup_amd_env.ps1
```

The script should:

- Verify Vulkan installation
- Verify Ollama
- Verify model availability
- Check RAM availability
- Export recommended environment variables

---

# ⚙️ AMD Radeon 780M Optimization

## Recommended BIOS Configuration

```text
UMA Frame Buffer = 8GB
```

Alternative:

```text
UMA Frame Buffer = Auto
```

for maximum system flexibility.

---

## Recommended Environment Variables

```powershell
setx OLLAMA_VULKAN 1

setx OLLAMA_KV_CACHE_TYPE q8_0
```

Reboot afterward.

---

## Verify Vulkan

```powershell
vulkaninfo
```

Expected output includes:

```text
AMD Radeon 780M
Vulkan API
```

---

## Verify Ollama GPU Usage

```powershell
ollama ps
```

Expected:

```text
PROCESSOR
100% GPU
```

or hybrid CPU/GPU usage depending on model size.

---

# 📊 Benchmark Results

> Repository benchmark table. Fill in real results while progressing.

| Model | Quant | Context | RAM Usage | Tokens/sec | Notes |
|---------|---------|---------|---------|---------|---------|
| qwen2.5-coder:7b | Q8_0 | 8K | TBD | TBD | Fast coding |
| qwen2.5-coder:14b | Q4_K_M | 8K | TBD | TBD | Main coding model |
| gemma3:12b | Q4_K_M | 8K | TBD | TBD | Vietnamese chat |
| qwen3:14b | Q4_K_M | 8K | TBD | TBD | Reasoning |
| qwen3:30b-a3b | Q4_K_M | 8K | TBD | TBD | MoE |

---

# 🤖 Recommended Models

## Coding & DevOps

```text
qwen2.5-coder:14b
```

Best balance between:

- Quality
- Speed
- Memory Usage

---

## Fast Autocomplete

```text
qwen2.5-coder:7b
```

Ideal for:

- Continue
- Cline
- Roo Code

---

## Vietnamese Chat

```text
gemma3:12b
```

Natural conversational Vietnamese.

---

## Reasoning

```text
deepseek-r1:14b
```

or

```text
qwen3:14b
```

for complex problem solving.

---

## RAG Applications

```text
qwen3:8b
```

or

```text
gemma3:12b
```

Good balance for document Q&A.

---

## AI Agents

```text
qwen3:14b
```

Strong tool-calling performance.

---

## Maximum Performance on 32GB RAM

```text
qwen3:30b-a3b
```

MoE architecture.

Advantages:

- Large effective capacity
- Lower runtime cost
- Excellent quality-to-speed ratio

---

# 🛠️ Real Projects

## Project 1 — Local Coding Assistant

### Features

- Code explanation
- Code generation
- Refactoring suggestions
- Commit message generation
- Unit test generation

### Stack

- Ollama
- Qwen2.5-Coder
- Continue
- VS Code

---

## Project 2 — Offline Technical Q&A

### Features

- Ask questions over PDFs
- Search internal documentation
- Explain architecture documents

### Stack

- ChromaDB
- Ollama
- nomic-embed-text

---

## Project 3 — GNSS Log Analyzer

### Input

- DLT logs
- UBX logs
- PCAP files
- SQLite databases

### Output

- Timeline analysis
- Root-cause clues
- HTML reports
- AI-generated summaries

---

## Project 4 — Build Failure Assistant

### Input

```text
Compiler Output
CI/CD Logs
Linker Errors
```

### Output

```text
Root Cause
Suggested Fix
Executive Summary
```

---

## Project 5 — Automotive RAG Assistant

### Features

- Search Jira exports
- Search RCA documents
- Search technical reports
- Search architecture documents

### Use Cases

- Faster onboarding
- Faster debugging
- Knowledge retrieval

---

## Project 6 — Local DevOps Copilot

### Capabilities

- Analyze pipeline failures
- Review deployment logs
- Generate troubleshooting reports
- Create action plans

---

# 📚 Learning Resources

## LLM Fundamentals

### Books

- Hands-On Large Language Models
- Build a Large Language Model From Scratch
- Designing Machine Learning Systems

### Courses

- Stanford CS25
- DeepLearning.AI LLM Courses

---

## RAG

### Documentation

- ChromaDB
- FAISS
- LlamaIndex
- LangChain

### Topics

- Chunking
- Retrieval
- Re-ranking
- Evaluation

---

## AI Agents

### References

- Anthropic Agent Guide
- OpenAI Function Calling
- MCP Specification

### Topics

- Tool Use
- ReAct
- Planning
- Memory

---

## Inference Engines

- Ollama
- llama.cpp
- LM Studio
- vLLM

---

# ✅ Progress Tracker

## Phase 1 — Foundations

- [ ] Complete theory
- [ ] Complete exercises
- [ ] Publish notes

## Phase 2 — Local Inference

- [ ] Install Ollama
- [ ] Configure Vulkan
- [ ] Run benchmarks

## Phase 3 — APIs & Coding Assistant

- [ ] OpenAI API examples
- [ ] VS Code integration
- [ ] Coding assistant project

## Phase 4 — RAG

- [ ] ChromaDB
- [ ] Embeddings
- [ ] RAG chatbot

## Phase 5 — AI Agents

- [ ] Tool Calling
- [ ] MCP
- [ ] Agent project

---

# 📌 Personal Notes

This repository is intended as a long-term learning and experimentation space covering:

```text
Local LLM
    ↓
Coding Assistant
    ↓
RAG
    ↓
AI Agents
    ↓
AI Engineering
```

with a strong focus on:

- AMD consumer hardware
- Fully offline workflows
- Practical software engineering use cases
- Technical documentation retrieval
- Log analysis and troubleshooting
- Automotive software development scenarios

---

# 🏁 End Goal

By completing this repository, the end result should be a fully local AI ecosystem capable of serving as:

✅ Local Coding Assistant

✅ Offline Technical RAG

✅ AI Agent with Tool Calling

✅ DevOps Copilot

✅ GNSS / Automotive Engineering Assistant

✅ Personal Knowledge Management System

All running entirely on:

**AMD Ryzen 7 H 255 + Radeon 780M + 32GB LPDDR5X RAM**

without relying on cloud AI services and while remaining extensible to real-world AI Engineering workloads.
