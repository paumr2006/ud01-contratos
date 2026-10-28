# experimento_memoria.py
import httpx

url = "http://localhost:11434/api/generate"

print("--- PETICIÓN 1: Presentación ---")

res1 = httpx.post(url, json={
    "model": "qwen2.5:0.5b",
    "prompt": "Hola, me llamo Laura García.",
    "stream": False
}, timeout=30.0)

print("Modelo:", res1.json()["response"].strip())



print("\n--- PETICIÓN 2: Pregunta sobre el pasado ---")
res2 = httpx.post(url, json={
    "model": "qwen2.5:0.5b",
    "prompt": "¿Cuál es mi nombre?",
    "stream": False
}, timeout=30.0)
print("Modelo:", res2.json()["response"].strip())