import reflex as rx
import sqlmodel as sm
from typing import Optional


class Examen(rx.Model, table=True):
    __tablename__: str = "examen"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    titulo: str
    desc: str
    usuario_id: int = sm.Field(foreign_key="usuario.id")
    creado_en: Optional[str] = sm.Field(default=None, sa_column=sm.Column(sm.DateTime, server_default=sm.func.now()))