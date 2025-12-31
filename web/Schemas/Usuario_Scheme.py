from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: str = "user"


class UsuarioCreate(UsuarioBase):
    password: str  # aquí el usuario ingresa la contraseña en texto plano


class UsuarioRead(UsuarioBase):
    id: int

    model_config = {"from_attributes": True}  # equivalente a orm_mode


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    rol: Optional[str] = None
