import reflex as rx
import sqlmodel as sm
from typing import Optional


class Usuario(rx.Model, table=True):
    __tablename__: str = "usuario"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    nombre: str
    email: str
    password: str  # guardaremos el hash
    rol: str = "docente"  # "docente" o "alumno"
    activo: bool = True
