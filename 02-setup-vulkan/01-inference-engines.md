# 1. Các Inference Engine cho Local LLM

## 1.1 `llama.cpp` — Nền tảng cốt lõi
- Viết bằng C/C++ thuần túy, không phụ thuộc các thư viện nặng nề như PyTorch hay CUDA runtime.
- Hỗ trợ đa dạng backend phần cứng: CPU (AVX2/AVX-512), CUDA (NVIDIA), Metal (Apple Silicon), **Vulkan** và ROCm (AMD).
- Là lõi xử lý đứng sau cả Ollama và LM Studio.

## 1.2 Ollama — Chuẩn mực cho Developer & Tự động hóa
- Đóng gói `llama.cpp` thành một dịch vụ chạy nền (daemon) gọn nhẹ kèm trình quản lý model qua CLI (`ollama pull`, `ollama run`, `ollama ps`).
- Tự động cung cấp REST API chuẩn OpenAI tại cổng `11434`, giúp kết nối tức thì với VS Code, Python scripts, LangChain, LlamaIndex.
- Cho phép cấu hình sâu thông qua biến môi trường hệ điều hành (`OLLAMA_VULKAN`, `OLLAMA_KV_CACHE_TYPE`, v.v.).

## 1.3 LM Studio — Công cụ trực quan & Thử nghiệm nhanh
- Cung cấp giao diện đồ họa (GUI) thân thiện, tích hợp kho tìm kiếm trực tiếp từ Hugging Face.
- Hiển thị trực quan mức tiêu thụ RAM/VRAM, tốc độ `tokens/sec`, thời gian đến token đầu tiên (`TTFT`).
- Cho phép chuyển đổi nóng (hot-swap) giữa các runtime (Vulkan, ROCm, CPU) và tinh chỉnh từng tham số như `GPU Offload Layers`, `Flash Attention`, `Context Length` bằng thanh trượt.
