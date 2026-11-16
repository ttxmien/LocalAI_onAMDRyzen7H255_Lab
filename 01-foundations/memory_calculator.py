from rich.console import Console
from rich.table import Table

console = Console()

QUANT_BYTES_PER_PARAM = {
    "FP16 (16-bit)": 2.0,
    "Q8_0 (8-bit)": 1.05,
    "Q6_K (6-bit)": 0.80,
    "Q5_K_M (5-bit)": 0.68,
    "Q4_K_M (4-bit - Khuyên dùng)": 0.58,
    "Q3_K_M (3-bit)": 0.48,
}

def estimate_memory_gb(params_billion: float, bytes_per_param: float, context_length: int = 8192) -> float:
    weights_gb = params_billion * bytes_per_param
    # Ước lượng KV Cache (với Flash Attention + Q8 KV Cache)
    kv_cache_gb = (params_billion / 7.0) * (context_length / 8192.0) * 0.6
    overhead_gb = 0.8
    return round(weights_gb + kv_cache_gb + overhead_gb, 2)

def main():
    console.print("[bold cyan]=== BẢNG TÍNH BỘ NHỚ DỰ KIẾN CHO THINKBOOK 32GB RAM ===[/bold cyan]\n")
    
    models = [
        ("Qwen2.5-Coder-7B", 7.6),
        ("Gemma-3-12B", 12.2),
        ("Qwen2.5-Coder-14B / Qwen3-14B", 14.8),
        ("Qwen3-30B-A3B (MoE)", 30.5),
    ]
    
    table = Table(title="Dung lượng RAM/VRAM ước tính (Context = 8,192 tokens)")
    table.add_column("Model", style="cyan")
    table.add_column("Q4_K_M", style="green")
    table.add_column("Q5_K_M", style="yellow")
    table.add_column("Q8_0", style="magenta")
    table.add_column("Đánh giá trên máy 32GB", style="white")
    
    for name, params in models:
        q4 = estimate_memory_gb(params, QUANT_BYTES_PER_PARAM["Q4_K_M (4-bit - Khuyên dùng)"])
        q5 = estimate_memory_gb(params, QUANT_BYTES_PER_PARAM["Q5_K_M (5-bit)"])
        q8 = estimate_memory_gb(params, QUANT_BYTES_PER_PARAM["Q8_0 (8-bit)"])
        
        status = "Chạy cực mượt, dư nhiều RAM" if q5 < 15 else "Chạy tốt ở bản Q4_K_M (~19GB)"
        table.add_row(name, f"{q4} GB", f"{q5} GB", f"{q8} GB", status)
        
    console.print(table)

if __name__ == "__main__":
    main()
