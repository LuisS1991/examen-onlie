from typing import Optional
from pydantic import BaseModel

class RespuesAlumnoExamenBase(BaseModel):
    alumno_id:int
    pregunta_id: int
    respuesta_id:int

class RespuesAlumnoExamenCreate(RespuesAlumnoExamenBase):
    pass


class RespuesAlumnoExamenUpdate(RespuesAlumnoExamenBase):
    id: int


class RespuesAlumnoExamenOut(RespuesAlumnoExamenBase):
    pass