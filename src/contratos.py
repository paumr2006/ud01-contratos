from pydantic import BaseModel, Field, AfterValidator, BaseModel, ValidationError

class ContactoCliente(BaseModel):
    nombre: str = Field(description="Nombre completo del cliente", min_length=2)

    @field_validator("email")
    
    contacto: str = Field(description="Forma de contacto con el cliente")
    intencion: str = Field(description="Intención principal declarada por el cliente")