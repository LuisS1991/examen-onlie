from typing import Optional
from pydantic import BaseModel


class RespuestaBase(BaseModel):
    respuesta: str
    correcta: int
    pregunta_id: int


class RespuestaCreate(RespuestaBase):
    pass


class RespuestaUpdate(RespuestaBase):
    id: int


class RespuestaOut(RespuestaBase):
    id: int
