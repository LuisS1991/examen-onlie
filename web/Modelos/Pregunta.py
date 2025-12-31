import reflex as rx
import sqlmodel as sm
from typing import List, Optional


class Pregunta(rx.Model, table=True):
    __tablename__: str = "pregunta"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    pregunta: str
    calificacion: int
    examen_id: int = sm.Field(foreign_key="examen.id")
    # Relación 1 → N
    respuestas: List["Respuesta"] = sm.Relationship(back_populates="pregunta")
