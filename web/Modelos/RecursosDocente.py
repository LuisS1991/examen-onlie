import reflex as rx
import sqlmodel as sm
from typing import Optional


class RecursosDocente(rx.Model, table=True):
    __tablename__: str = "recursos_docente"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    nombre: str
    link: int
    desc: str
    usuario_id: int = sm.Field(foreign_key="usuario.id")
