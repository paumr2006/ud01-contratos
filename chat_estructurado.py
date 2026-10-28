# chat_estructurado.py
import httpx

url = "http://localhost:11434/api/chat"

messages = [
    {
        "role": "system",
        "content": "Eres un asistente de atención técnica de una empresa. Responde de forma concisa y profesional."
    }
]

print("Iniciando Chat Estructurado con Roles (Escribe 'salir' para terminar)\n")

while True:
    prompt = input("Usuario: ")
    if prompt.lower() in ("salir", "exit"):
        break

    messages.append({"role": "user", "content": prompt})

    response = httpx.post(url, json={
        "model": "qwen2.5:0.5b",
        "messages": messages,
        "stream": False
    }, timeout=30.0)

    respuesta = response.json()["message"]["content"].strip()
    messages.append({"role": "assistant", "content": respuesta})

    print(f"Asistente: {respuesta}\n")