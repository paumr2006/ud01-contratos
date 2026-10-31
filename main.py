from pydantic import ValidationError
from src.cliente_ollama import extraer_contacto

mensaje = "Hola, soy Laura García. Me interesa conocer precios de pavimentos para exterior. Mi email es laura@empersa.com"

try:

    resultado = extraer_contacto(mensaje)
    if resultado.valido:
        print("--- CONTRATO VALIDADO CON ÉXITO ---")
        print(f"Tipo devuelto: {type(resultado.cliente)}")
        print(f"Nombre:        {resultado.cliente.nombre}")
        print(f"Contacto:      {resultado.cliente.contacto}")
        print(f"Intención:     {resultado.cliente.intencion}")
    else:
        print("error extraccion" + resultado.mensaje)
except ConnectionError as e:
    # Error de infraestructura: fallo de red o caída del servicio Ollama
    print(f"Error de infraestructura: {e}")