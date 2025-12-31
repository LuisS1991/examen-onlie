import reflex as rx
import sqlmodel as sm
from typing import Optional


class RespuestaAlumno(rx.Model, table=True):
    __tablename__: str = "respuesta_alumno"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    respuesta_id: int = sm.Field(foreign_key="respuesta.id")
    pregunta_id: int = sm.Field(foreign_key="pregunta.id")
    examen_alumno_id: int = sm.Field(foreign_key="examen_alumno.id")
