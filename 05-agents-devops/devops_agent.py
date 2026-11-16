import json
import psutil
from openai import OpenAI
from rich.console import Console

console = Console()
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# 1. Định nghĩa các công cụ (Tools) mà Agent có thể sử dụng
def check_system_health() -> str:
    """Kiểm tra mức sử dụng CPU, RAM và ổ đĩa thực tế trên máy hiện tại."""
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return json.dumps({
        "cpu_usage_percent": cpu,
        "ram_total_gb": round(mem.total / (1024**3), 1),
        "ram_used_percent": mem.percent,
        "disk_free_gb": round(disk.free / (1024**3), 1)
    })

def read_service_logs(service_name: str) -> str:
    """Đọc log gần nhất của một microservice hoặc daemon."""
    mock_logs = {
        "gnss-manager": "[ERROR] 10:14:22 PPS signal timeout (>500ms). Fallback to dead-reckoning mode.",
        "docker-engine": "[INFO] 10:15:00 All 4 containers healthy. Memory footprint: 1.2GB.",
        "nginx": "[WARN] 10:12:05 Upstream response time > 2.5s on /api/v1/inference."
    }
    return mock_logs.get(service_name, f"Không tìm thấy log cho service '{service_name}'.")

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "check_system_health",
            "description": "Lấy thông số CPU, RAM, ổ đĩa thực tế của máy tính hiện tại.",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_service_logs",
            "description": "Đọc các dòng log mới nhất của một service cụ thể (ví dụ: gnss-manager, docker-engine, nginx).",
            "parameters": {
                "type": "object",
                "properties": {
                    "service_name": {
                        "type": "string",
                        "description": "Tên của service cần kiểm tra log"
                    }
                },
                "required": ["service_name"]
            }
        }
    }
]

AVAILABLE_FUNCTIONS = {
    "check_system_health": check_system_health,
    "read_service_logs": read_service_logs
}

def run_agent(user_prompt: str, model: str = "qwen2.5-coder:14b"):
    console.print(f"[bold yellow]Yêu cầu của bạn:[/bold yellow] {user_prompt}\n")
    messages = [
        {
            "role": "system",
            "content": "Bạn là một DevOps AI Agent. Hãy sử dụng các công cụ được cung cấp để kiểm tra dữ liệu thực tế trước khi đưa ra kết luận."
        },
        {"role": "user", "content": user_prompt}
    ]

    # Bước 1: Gửi prompt kèm danh sách tools cho LLM
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOLS_SCHEMA,
        temperature=0.1
    )

    msg = response.choices[0].message
    messages.append(msg)

    # Bước 2: Nếu LLM quyết định gọi tool
    if msg.tool_calls:
        for tool_call in msg.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments or "{}")
            console.print(f"[cyan]-> Agent đang gọi tool:[/cyan] [bold]{fn_name}({fn_args})[/bold]")
            
            fn_to_call = AVAILABLE_FUNCTIONS[fn_name]
            tool_result = fn_to_call(**fn_args)
            console.print(f"[dim]   Kết quả tool: {tool_result}[/dim]\n")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": fn_name,
                "content": tool_result
            })

        # Bước 3: Gửi kết quả tool lại cho LLM để tổng hợp báo cáo cuối cùng
        final_response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.2
        )
        console.print("[bold green]Báo cáo tổng hợp từ Agent:[/bold green]")
        console.print(final_response.choices[0].message.content)
    else:
        console.print(msg.content)

if __name__ == "__main__":
    run_agent("Kiểm tra giúp tôi tình trạng RAM/CPU hiện tại của máy và xem log của service gnss-manager có lỗi gì bất thường không?")
