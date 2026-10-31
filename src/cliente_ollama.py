import httpx
import json
from src.contratos import ContactoCliente

class ResultadoCliente:

    def __init__(valido, contacto, mensaje):
        self.valido = valido
        self.contacto = contacto
        self.mensaje = mensaje



def extraer_contacto(texto_usuario: str) -> ContactoCliente:
    url = "http://localhost:11434/api/chat"
    
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un extractor de datos de clientes. Analiza el mensaje del usuario y extrae "
                "los datos solicitados cumpliendo estrictamente con el esquema esperado."
            )
            },
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
                "model": "qwen2.5:0.5b",
                "messages": messages,
                "format": ContactoCliente.model_json_schema(), # Indicación de esquema para orientar la generación
                "stream": False
            },
            timeout=30.0
        )


        response.raise_for_status()
    except httpx.HTTºPError as e:
        # Error de comunicación con la infraestructura
        raise ConnectionError(f"Error de comunicación con Ollama: {e}") from e

    raw_content = response.json()["message"]["content"]

    print(f"Raw content: {raw_content}")
    print(json.dumps(ContactoCliente.model_json_schema(), indent=2, ensure_ascii=False))
    
    
    # 2. La Frontera de la Aplicación: Pydantic valida lo que el modelo propone.
    # Si la propuesta incumple el esquema o los tipos, model_validate_json eleva ValidationError directamente.
    try:
        resultado = ContactoCliente.model_validate_json(raw_content)
        print(f"Resultado: {resultado}")
        return ResultadoCliente(valido=True, contacto=resultado, mensaje="")
    except Exception as e:
        return ResultadoCliente(valido=False, contacto=resultado, mensaje=e)

    