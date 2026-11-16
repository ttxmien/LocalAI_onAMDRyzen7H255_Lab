import requests
import chromadb
from openai import OpenAI
from rich.console import Console

console = Console()
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
EMBED_URL = "http://localhost:11434/api/embeddings"

# Dữ liệu mẫu: Tài liệu kỹ thuật & mã lỗi hệ thống nội bộ
KNOWLEDGE_BASE = [
    {
        "id": "doc_1",
        "text": "Mã lỗi DTC 0xB7F321 xảy ra khi dịch vụ GnssPositioning (Service ID 0xE025) bị mất đồng bộ xung PPS từ module thu vệ tinh quá 500ms. Cách khắc phục: Kiểm tra cáp coaxial anten GNSS và khởi động lại daemon gnss-manager."
    },
    {
        "id": "doc_2",
        "text": "Mã lỗi DTC 0xD814BE xuất hiện khi SOME/IP Instance 0x0001 không nhận được phản hồi đăng ký (Subscribe Eventgroup Ack) từ IPF consumer trong vòng 3 chu kỳ retry. Nguyên nhân thường do VLAN firewall chặn gói tin multicast."
    },
    {
        "id": "doc_3",
        "text": "Quy trình BAM recovery boot trên hệ thống Infotainment sẽ tự động kích hoạt nếu watchdog phát hiện tiến trình lõi treo quá 3 lần liên tiếp trong 60 giây. Log phục hồi được lưu tại /var/log/boot/bam_recovery.log."
    },
    {
        "id": "doc_4",
        "text": "Để tối ưu hiệu năng Local LLM trên AMD Radeon 780M, cần bật OLLAMA_VULKAN=1 và thiết lập OLLAMA_KV_CACHE_TYPE=q8_0 để giảm 40% mức chiếm dụng bộ nhớ RAM."
    }
]

def get_embedding(text: str, model: str = "nomic-embed-text"):
    resp = requests.post(EMBED_URL, json={"model": model, "prompt": text}, timeout=30)
    resp.raise_for_status()
    return resp.json()["embedding"]

def main():
    console.print("[bold cyan]1. Đang khởi tạo Vector DB (ChromaDB) và nhúng dữ liệu...[/bold cyan]")
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="tech_docs")

    for doc in KNOWLEDGE_BASE:
        emb = get_embedding(doc["text"])
        collection.add(
            ids=[doc["id"]],
            embeddings=[emb],
            documents=[doc["text"]]
        )

    query = "Hệ thống báo lỗi 0xD814BE trên SOME/IP thì nguyên nhân là gì và xử lý ra sao?"
    console.print(f"\n[bold yellow]Câu hỏi:[/bold yellow] {query}")

    # Truy xuất 2 đoạn liên quan nhất
    query_emb = get_embedding(query)
    results = collection.query(query_embeddings=[query_emb], n_results=2)
    retrieved_docs = results["documents"][0]

    context = "\n- ".join(retrieved_docs)
    console.print(f"\n[dim]Ngữ cảnh tìm thấy trong DB:\n- {context}[/dim]\n")

    # Gửi ngữ cảnh + câu hỏi cho LLM
    console.print("[bold green]Trả lời từ Local LLM:[/bold green]")
    response = client.chat.completions.create(
        model="qwen2.5-coder:14b",
        messages=[
            {
                "role": "system",
                "content": "Chỉ trả lời câu hỏi dựa trên NGỮ CẢNH được cung cấp. Nếu không có thông tin, hãy nói không biết."
            },
            {
                "role": "user",
                "content": f"NGỮ CẢNH:\n{context}\n\nCÂU HỎI: {query}"
            }
        ],
        temperature=0.1
    )
    console.print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
