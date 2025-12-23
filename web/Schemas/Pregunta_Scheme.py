from typing import List
from pydantic import BaseModel
from web.Schemas.Respuesta_Scheme import RespuestaOut

class PreguntaBase(BaseModel):
    pregunta: str


class PreguntaCreate(PreguntaBase):
    pass


class PreguntaUpdate(PreguntaBase):
    id: int


class PreguntaOut(PreguntaBase):
    id: int
    respuestas: List[RespuestaOut] = []
