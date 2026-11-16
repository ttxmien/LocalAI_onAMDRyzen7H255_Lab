import time
import requests
from rich.console import Console
from rich.table import Table

console = Console()
OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = (
    "Hãy viết một script Python hoàn chỉnh sử dụng thư viện asyncio để kiểm tra trạng thái "
    "HTTP của danh sách 10 URL đồng thời, có xử lý timeout, retry 2 lần và xuất kết quả ra JSON. "
    "Giải thích ngắn gọn cách hoạt động."
)

def benchmark_model(model_name: str):
    console.print(f"[cyan]Đang test model:[/cyan] [bold]{model_name}[/bold] ...")
    payload = {
        "model": model_name,
        "prompt": PROMPT,
        "stream": False,
        "options": {
            "num_ctx": 4096,
            "temperature": 0.2
        }
    }
    
    start_time = time.time()
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=300)
        resp.raise_for_status()
        data = resp.json()
        
        total_time = round(time.time() - start_time, 2)
        eval_count = data.get("eval_count", 0)
        eval_duration_sec = data.get("eval_duration", 1) / 1e9
        prompt_eval_sec = data.get("prompt_eval_duration", 1) / 1e9
        
        tokens_per_sec = round(eval_count / eval_duration_sec, 2) if eval_duration_sec > 0 else 0
        
        return {
            "model": model_name,
            "status": "OK",
            "tokens": eval_count,
            "ttft": round(prompt_eval_sec, 2),
            "tps": tokens_per_sec,
            "total": total_time
        }
    except Exception as e:
        return {
            "model": model_name,
            "status": f"Lỗi: {str(e)[:40]}",
            "tokens": 0,
            "ttft": 0,
            "tps": 0,
            "total": 0
        }

def main():
    # Kiểm tra các model đã cài trên máy
    try:
        tags = requests.get("http://localhost:11434/api/tags", timeout=5).json()
        installed_models = [m["name"] for m in tags.get("models", [])]
    except Exception:
        console.print("[bold red]Không kết nối được tới Ollama (localhost:11434). Hãy chắc chắn Ollama đang chạy![/bold red]")
        return

    if not installed_models:
        console.print("[yellow]Chưa có model nào được tải. Hãy chạy 'ollama pull qwen2.5-coder:14b' trước.[/yellow]")
        return

    results = []
    for m in installed_models:
        results.append(benchmark_model(m))

    table = Table(title="Kết quả Benchmark Local LLM trên ThinkBook 14 G8+")
    table.add_column("Model", style="cyan")
    table.add_column("Trạng thái", style="green")
    table.add_column("Thời gian đọc Prompt (s)", justify="right")
    table.add_column("Tốc độ sinh chữ (tokens/s)", style="bold yellow", justify="right")
    table.add_column("Tổng thời gian (s)", justify="right")

    for r in results:
        table.add_row(
            r["model"],
            r["status"],
            str(r["ttft"]),
            f"{r['tps']} t/s",
            str(r["total"])
        )

    console.print("\n", table)

if __name__ == "__main__":
    main()
