import platform
import subprocess
import psutil
from rich.console import Console
from rich.table import Table

console = Console()

def get_gpu_info():
    try:
        cmd = 'powershell -Command "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"'
        output = subprocess.check_output(cmd, shell=True, text=True).strip()
        return output.replace("\n", ", ")
    except Exception:
        return "Không xác định"

def main():
    console.print("[bold cyan]=== KIỂM TRA SẴN SÀNG PHẦN CỨNG LOCAL AI ===[/bold cyan]\n")
    
    mem = psutil.virtual_memory()
    total_ram_gb = round(mem.total / (1024**3), 2)
    avail_ram_gb = round(mem.available / (1024**3), 2)
    
    table = Table(title="Thông số hệ thống hiện tại")
    table.add_column("Thành phần", style="cyan", no_wrap=True)
    table.add_column("Chi tiết", style="green")
    
    table.add_row("Hệ điều hành", f"{platform.system()} {platform.release()}")
    table.add_row("CPU", platform.processor())
    table.add_row("Số nhân / Luồng", f"{psutil.cpu_count(logical=False)} Cores / {psutil.cpu_count(logical=True)} Threads")
    table.add_row("Tổng RAM", f"{total_ram_gb} GB")
    table.add_row("RAM khả dụng hiện tại", f"{avail_ram_gb} GB")
    table.add_row("GPU phát hiện", get_gpu_info())
    
    console.print(table)
    
    console.print("\n[bold yellow]Khuyến nghị kích thước Model dựa trên RAM khả dụng:[/bold yellow]")
    if avail_ram_gb >= 22:
        console.print("- [green]Tốt nhất:[/green] Chạy mượt mọi model 14B (Q5_K_M) hoặc MoE 30B-A3B (Q4_K_M).")
    elif avail_ram_gb >= 12:
        console.print("- [green]Tốt:[/green] Nên dùng model 7B - 14B (Q4_K_M).")
    else:
        console.print("- [red]Lưu ý:[/red] Đang mở nhiều ứng dụng nặng. Nên đóng bớt tab trình duyệt hoặc dùng model 3B - 7B (Q4_K_M).")

if __name__ == "__main__":
    main()
