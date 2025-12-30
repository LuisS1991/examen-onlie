from web.Schemas.Alumno_Scheme import AlumnoCreate, AlumnoUpdate, AlumnoOut
from web.Schemas.Pregunta_Scheme import PreguntaCreate, PreguntaUpdate, PreguntaOut
from web.Schemas.Respuesta_Scheme import RespuestaCreate, RespuestaUpdate, RespuestaOut
from web.Schemas.RespuesAlumnoExamen_Scheme import (
    RespuesAlumnoExamenBase,
    RespuesAlumnoExamenCreate,
    RespuesAlumnoExamenUpdate,
    RespuesAlumnoExamenOut,
)
from web.Schemas.MenuItemScheme import MenuItemScheme
__all__ = [
    "MenuItemScheme",
    "AlumnoCreate",
    "AlumnoUpdate",
    "AlumnoOut",
    "PreguntaCreate",
    "PreguntaUpdate",
    "PreguntaOut",
    "RespuestaCreate",
    "RespuestaUpdate",
    "RespuestaOut",
    "RespuesAlumnoExamenBase",
    "RespuesAlumnoExamenCreate",
    "RespuesAlumnoExamenUpdate",
    "RespuesAlumnoExamenOut",
]
