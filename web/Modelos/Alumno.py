import reflex as rx
import sqlmodel as sm
from typing import  Optional

class Alumno(rx.Model, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    nombre: str
    cedula: str
