import reflex as rx
import sqlmodel as sm
from typing import Optional


class ExamenAlumno(rx.Model, table=True):
    __tablename__ = "examen_alumno"
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    examen_id: int = sm.Field(foreign_key="examen.id")
    alumno_id: int = sm.Field(foreign_key="alumnos.id")
    calificacion: float = sm.Field(default=0.0)
    #por defecto la fecha de presentacion es la fecha actual
    fecha_presentacion: Optional[str] = sm.Field(default=None, sa_column=sm.Column(sm.DateTime, server_default=sm.func.now()))
