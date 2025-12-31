import reflex as rx
import sqlmodel as sm
from typing import Optional


class Alumno(rx.Model, table=True):
    __tablename__: str = "alumnos"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    nombre: str
    cedula: str
    grupo: str #G1-2025
    instituto: str = "Nursing School Uruguay" #valor por defecto 
