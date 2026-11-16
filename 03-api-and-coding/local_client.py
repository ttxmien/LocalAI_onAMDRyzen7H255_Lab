from openai import OpenAI
from rich.console import Console

console = Console()

# Kết nối tới Ollama local server bằng chuẩn OpenAI SDK
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Bắt buộc truyền chuỗi bất kỳ, không dùng tới
)

def stream_code_review(code_snippet: str, model: str = "qwen2.5-coder:14b"):
    console.print(f"[bold cyan]Đang phân tích code bằng {model}...[/bold cyan]\n")
    
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Bạn là một Senior Software & DevOps Engineer. Hãy review đoạn code sau, "
                    "chỉ ra lỗi tiềm ẩn (memory leak, race condition, security) và đề xuất bản sửa tối ưu."
                ),
            },
            {"role": "user", "content": f"```cpp\n{code_snippet}\n```"},
        ],
        temperature=0.2,
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
    print("\n")

if __name__ == "__main__":
    sample_cpp_code = '''
    #include <iostream>
    #include <thread>
    int counter = 0;
    void increment() {
        for (int i = 0; i < 100000; ++i) {
            counter++;
        }
    }
    int main() {
        std::thread t1(increment);
        std::thread t2(increment);
        t1.join();
        t2.join();
        std::cout << "Counter: " << counter << std::endl;
        return 0;
    }
    '''
    stream_code_review(sample_cpp_code)
