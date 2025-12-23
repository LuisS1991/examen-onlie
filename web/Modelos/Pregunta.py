import reflex as rx
import sqlmodel as sm
from typing import List, Optional


class Pregunta(rx.Model, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    pregunta: str

    # Relación 1 → N
    respuestas: List["Respuesta"] = sm.Relationship(back_populates="pregunta")
