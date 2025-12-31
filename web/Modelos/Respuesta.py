import reflex as rx
import sqlmodel as sm
from typing import Optional


class Respuesta(rx.Model, table=True):
    __tablename__: str = "respuesta"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    respuesta: str
    correcta: int
    pregunta_id: int = sm.Field(foreign_key="pregunta.id")
    # Relación N → 1
    pregunta: Optional["Pregunta"] = sm.Relationship(back_populates="respuestas")
