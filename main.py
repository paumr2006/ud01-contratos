from pydantic import ValidationError
from src.cliente_ollama import extraer_contacto

mensaje = "Hola, soy Laura García. Me interesa conocer precios de pavimentos para exterior. Mi email es laura@empersa.com"

print("holaaa")
try:
    cliente = extraer_contacto(mensaje)
    print("--- CONTRATO VALIDADO CON ÉXITO ---")
    print(f"Tipo devuelto: {type(cliente)}")
    print(f"Nombre:        {cliente.nombre}")
    print(f"Contacto:         {cliente.contacto}")
    print(f"Intención:     {cliente.intencion}")
except ValidationError as e:
    # Error de contrato: el LLM produjo una propuesta no conforme al esquema o reglas
    print(f"Propuesta rechazada por el contrato de datos: {e}")
except ConnectionError as e:
    # Error de infraestructura: fallo de red o caída del servicio Ollama
    print(f"Error de infraestructura: {e}")