from pydantic import BaseModel, Field, ValidationError, field_validator

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
        
    @field_validator("intencion")
    @classmethod
    def validar_intencion(cls, value):
        valores = {"consulta", "compra", "soporte"}
        print(value)
        if value not in valores:
            raise ValidationError("La intención que devuelve el modelo no esta dentro de los valores consulta, compra ni soporte")
        return value






