<div align="center">
  <a href="README.md"><b>English</b></a> | 
  <a href="README.vi.md"><b>Tiếng Việt</b></a>
</div>

---

# 🧠 Local AI Lab — AMD Ryzen 7 H 255 / 32GB RAM / Radeon 780M

> A practical AI Engineering playground for Local LLMs, RAG systems, AI Agents, and developer productivity workflows running entirely offline on consumer AMD hardware.

![Hardware](https://img.shields.io/badge/Hardware-ThinkBook_14_G8%2B_(21VR)-blue?style=flat-square)
![CPU](https://img.shields.io/badge/CPU-Ryzen_7_H_255-red?style=flat-square)
![GPU](https://img.shields.io/badge/iGPU-Radeon_780M_(Vulkan)-orange?style=flat-square)
![RAM](https://img.shields.io/badge/RAM-32GB_LPDDR5x_7500MT%2Fs-green?style=flat-square)

This repository documents a structured learning roadmap, hardware tuning scripts, benchmark results, and hands-on projects for **Local LLM & AI Engineering**, specifically tailored for **Lenovo ThinkBook 14 G8+ (21VR)**:

| Component | Specification | AI Workload Role |
| :--- | :--- | :--- |
| **CPU** | AMD Ryzen 7 H 255 (8C / 16T, Zen 4) | Preprocessing, chunking, orchestration, and hybrid fallback |
| **RAM** | 32GB LPDDR5x 7500 MT/s | High-bandwidth Shared Unified Memory (supports up to 30B MoE models) |
| **GPU** | AMD Radeon 780M (RDNA 3, 12 CUs) | Primary inference engine via Vulkan backend (`100% GPU` offload) |
| **Storage** | 1TB NVMe SSD | Fast model weight loading (GGUF) and local Vector DB persistence |
| **OS** | Windows 11 Pro | Native Ollama + Vulkan / WSL2 development environment |

---

## 🎯 Objectives

Build foundational knowledge and production-grade engineering skills to run local AI systems for daily software development, automotive diagnostics, and DevOps workflows:

- **LLM Internals:** Master Transformer mechanics, quantization (`Q4_K_M`, `Q8_0`), KV Cache, and memory-bandwidth bottlenecks on iGPUs.
- **AMD Inference Tuning:** Configure Vulkan acceleration, Flash Attention, and BIOS UMA Frame Buffer on Radeon 780M.
- **IDE Integration:** Deploy a zero-cost, offline AI coding assistant in VS Code (chat, refactoring, and fast autocomplete).
- **Offline Technical RAG:** Build retrieval pipelines over PDFs, architecture docs, Jira exports, and RCA reports.
- **Autonomous AI Agents:** Implement Tool Calling (Function Calling) and ReAct workflows for log analysis (GNSS/DLT/CI-CD) and system automation.

---

## 🏗️ End-State Architecture

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
 • Code Generation         • Technical Specs          • Tool Calling
 • Refactoring             • Jira & RCA Exports       • GNSS / DLT Logs
 • Unit Tests              • Internal Guides          • Build & CI/CD Fix
```

---

## 🗺️ Learning Roadmap (15-Day Sprint)

| Phase | Directory | Core Theory | Hands-On Labs | Key Deliverables | Timeline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1**<br>Foundations | `01-foundations/` | Transformers, Tokenization, Quantization (GGUF), KV Cache, Memory Bandwidth, Dense vs. MoE | Calculate RAM/VRAM footprints, compare `Q4_K_M` vs. `Q8_0`, analyze theoretical throughput on 780M | Quantization Cheat Sheet & Memory Calculator | Days 1–2 |
| **Phase 2**<br>AMD Inference | `02-setup-vulkan/` | Inference Engines (`llama.cpp`, Ollama, LM Studio), Vulkan vs. ROCm, UMA Architecture | Install Ollama & LM Studio, tune BIOS UMA buffer, benchmark 7B, 14B, and 30B-A3B models | Stable Vulkan-accelerated inference setup | Days 3–4 |
| **Phase 3**<br>APIs & Coding | `03-api-and-coding/` | OpenAI REST API, Streaming, System Prompts, Temperature, Context Length (`num_ctx`) | Build Python streaming clients, configure Continue/Cline in VS Code for chat & autocomplete | Offline Local Coding Assistant | Days 5–7 |
| **Phase 4**<br>Local RAG | `04-rag-local/` | Embeddings, ChromaDB, FAISS, Chunking Strategies, Hybrid Search (BM25 + Vector) | Ingest PDFs, Markdown, and Jira exports to build a citation-backed Q&A assistant | Offline Technical RAG System | Days 8–11 |
| **Phase 5**<br>AI Agents | `05-agents-devops/` | Function Calling, Tool Use, ReAct Loop, Structured Outputs (JSON Schema), MCP | Build agents to inspect system health, parse GNSS/build logs, and generate RCA reports | Autonomous DevOps & Log Agent | Days 12–15 |

---

## 📁 Repository Structure

```text
LocalAI_onAMDRyzen7H255_Lab/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/                       # Hardware tuning guides & architecture notes
├── scripts/                    # PowerShell environment & hardware verification scripts
├── 01-foundations/             # Theory notes, quantization worksheets & memory scripts
├── 02-setup-vulkan/            # Ollama/LM Studio configs & throughput benchmarks
├── 03-api-and-coding/          # OpenAI-compatible Python clients & VS Code configs
├── 04-rag-local/               # Embedding pipelines, ChromaDB/FAISS & ingestion labs
├── 05-agents-devops/           # Tool-calling schemas, log parsers & DevOps agents
├── benchmarks/                 # Logged performance metrics across model updates
└── playground/                 # Experimental scripts and scratchpads
```

---

## 🚀 Quick Start

### 1. Clone & Setup Python Environment

```powershell
git clone https://github.com/ttxmien/LocalAI_onAMDRyzen7H255_Lab.git
cd LocalAI_onAMDRyzen7H255_Lab

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Install Ollama & Pull Recommended Models

```powershell
winget install Ollama.Ollama
ollama --version

# Pull core models optimized for 32GB Unified Memory
ollama pull qwen2.5-coder:14b    # Primary coding & DevOps model (~9.0 GB)
ollama pull qwen2.5-coder:7b     # Ultra-fast IDE autocomplete (~4.7 GB)
ollama pull gemma3:12b           # General chat & Vietnamese fluency (~8.1 GB)
ollama pull qwen3:30b-a3b        # High-intelligence MoE model (~18.5 GB)
ollama pull nomic-embed-text     # Local embedding model for RAG (~274 MB)
```

### 3. Configure AMD Vulkan Environment

Run PowerShell as **Administrator** to set Vulkan and KV Cache optimization flags (`OLLAMA_VULKAN=1`, `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`):

```powershell
.\scripts\setup_amd_env.ps1
```

*(Restart Ollama from the system tray after running the script, then verify GPU offload with `ollama ps` while generating a response).*

---

## ⚙️ AMD Radeon 780M Optimization Guide

- **BIOS Tuning:** Enter BIOS (`F2` at boot) $\rightarrow$ `Configuration` $\rightarrow$ Set **UMA Frame Buffer Size** to `8G` (reserves dedicated VRAM while leaving 24GB for Windows/Docker) or keep `Auto` for dynamic allocation.
- **Power Profile:** Press `Fn + Q` to switch ThinkBook to **Performance Mode** during heavy inference or benchmarking.
- **Verify Vulkan & GPU Offload:**

```powershell
vulkaninfo --summary   # Confirm AMD Radeon 780M Vulkan 1.3 support
ollama ps              # Confirm PROCESSOR shows "100% GPU"
```

---

## 🤖 Recommended Model Matrix (32GB RAM Sweet Spot)

| Use Case | Model | Quantization | Est. Memory | Why It Fits This Hardware |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Coding & DevOps** | `qwen2.5-coder:14b` | `Q4_K_M` | ~9.5 GB | Best balance of code accuracy, YAML/C++/Python mastery, and speed |
| **IDE Autocomplete** | `qwen2.5-coder:7b` | `Q8_0` | ~8.2 GB | Near-lossless precision with sub-second inline completion latency |
| **Multilingual / VN Chat** | `gemma3:12b` | `Q4_K_M` | ~8.5 GB | Natural Vietnamese phrasing and strong summarization quality |
| **Deep Reasoning** | `qwen3:14b` / `deepseek-r1:14b` | `Q4_K_M` | ~9.2 GB | Step-by-step chain-of-thought for complex debugging and algorithms |
| **Max Intelligence (MoE)** | `qwen3:30b-a3b` | `Q4_K_M` | ~19.0 GB | 30B total parameters (fits in 32GB RAM) with only 3B active per token |
| **RAG Embeddings** | `nomic-embed-text` | `F16` | ~0.3 GB | Fast, accurate semantic embeddings for local document retrieval |

---

## 📊 Benchmark Results

> *Tracked on Windows 11 Pro (Performance Mode `Fn+Q`, `OLLAMA_VULKAN=1`, `num_ctx=8192`). Update with actual runs.*

| Model | Quant | Context | Peak RAM | Prompt Eval (t/s) | Generation (t/s) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `qwen2.5-coder:7b` | `Q8_0` | 8192 | ~8.5 GB | *TBD* | *TBD* | IDE Autocomplete |
| `qwen2.5-coder:14b` | `Q4_K_M` | 8192 | ~9.8 GB | *TBD* | *TBD* | Main coding & agent model |
| `gemma3:12b` | `Q4_K_M` | 8192 | ~8.8 GB | *TBD* | *TBD* | General Q&A |
| `qwen3:14b` | `Q4_K_M` | 8192 | ~9.6 GB | *TBD* | *TBD* | Reasoning tasks |
| `qwen3:30b-a3b` | `Q4_K_M` | 8192 | ~19.2 GB | *TBD* | *TBD* | MoE high-throughput test |

---

## 🛠️ Capstone Projects

1. **Local Coding Assistant:** Offline VS Code copilot (Continue/Cline) for code explanation, refactoring, commit messages, and unit test generation.
2. **Offline Technical Q&A (RAG):** Semantic search and grounded Q&A over PDFs, Markdown specs, and architecture documents using ChromaDB + `nomic-embed-text`.
3. **GNSS & Diagnostic Log Analyzer:** Automated parser and LLM summarizer for DLT logs, UBX traces, PCAP captures, and SQLite databases to accelerate root-cause analysis (RCA).
4. **Build & CI/CD Failure Assistant:** Parses compiler/linker errors and pipeline logs to pinpoint root causes and propose actionable fixes.
5. **Automotive Knowledge Assistant:** RAG pipeline indexing Jira ticket exports, RCA documents, and internal system guides for rapid debugging and onboarding.
6. **Local DevOps Copilot:** Tool-calling agent capable of inspecting system metrics, reviewing deployment logs, and generating troubleshooting runbooks.

---

## 📚 Curated Learning Resources

- **LLM Foundations:** *Hands-On Large Language Models* (Alammar & Grootendorst), *Build a Large Language Model (From Scratch)* (Raschka), Stanford CS25.
- **RAG & Retrieval:** ChromaDB Docs, FAISS Wiki, LlamaIndex & LangChain Retrieval Guides (Chunking, Hybrid Search, Re-ranking).
- **Agents & Protocols:** Anthropic *Building Effective Agents*, OpenAI Function Calling Docs, Model Context Protocol (MCP) Specification.
- **Inference Runtimes:** `llama.cpp`, Ollama, LM Studio, ONNX Runtime / DirectML.

---

## ✅ Progress Tracker

- [ ] **Phase 1 — Foundations:** Complete theory notes, quantization cheat sheet, and memory calculator.
- [ ] **Phase 2 — Local Inference:** Configure Vulkan backend, tune BIOS UMA buffer, and log baseline benchmarks.
- [ ] **Phase 3 — APIs & Coding:** Build streaming Python client and integrate Ollama with VS Code.
- [ ] **Phase 4 — Local RAG:** Build ChromaDB ingestion pipeline and offline technical Q&A chatbot.
- [ ] **Phase 5 — AI Agents:** Implement Function Calling / MCP tools for log analysis and DevOps automation.