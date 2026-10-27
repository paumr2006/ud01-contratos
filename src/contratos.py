from pydantic import BaseModel, Field, AfterValidator, BaseModel, ValidationError

class ContactoCliente(BaseModel):
    nombre: str = Field(description="Nombre completo del cliente", min_length=2)
    email: str = Field(description="Email del cliente")
    intencion: str = Field(description="Intención principal declarada por el cliente")

    @field_validator("email")
    @classmethod
    def is_email(cls, value):
        if '@' and '.' not in value:
            raise ValueError("no es un email")
        return value
        
