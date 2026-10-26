import httpx
from src.contratos import ContactoCliente

def extraer_contacto(texto_usuario: str) -> ContactoCliente:
    url = "http://localhost:11434/api/chat"
    
    messages = [
        {
            "role": "system",
"content": "En el campo contacto del formato, retorna el número de teléfono +34 654654654. No retornes ningún email o correo."        },
        {
            "role": "user",
            "content": texto_usuario
        }
    ]
    
    # 1. Llamada HTTP: captura de errores de comunicación de infraestructura
    try:
        response = httpx.post(
            url,
            json={
                "model": "qwen2.5:0.5b",-
                "messages": messages,
                "format": ContactoCliente.model_json_schema(), # Indicación de esquema para orientar la generación
                "stream": False
            },
            timeout=30.0
        )


        response.raise_for_status()
    except httpx.HTTPError as e:
        # Error de comunicación con la infraestructura
        raise ConnectionError(f"Error de comunicación con Ollama: {e}") from e

    raw_content = response.json()["message"]["content"]
    
    # 2. La Frontera de la Aplicación: Pydantic valida lo que el modelo propone.
    # Si la propuesta incumple el esquema o los tipos, model_validate_json eleva ValidationError directamente.
    return ContactoCliente.model_validate_json(raw_content)