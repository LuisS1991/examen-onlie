from web.Modelos.Respuesta import Respuesta
from web.Schemas.Respuesta_Scheme import  RespuestaCreate, RespuestaUpdate
from web.Controlador.Base_Controller import BaseController


class RespuestaController(BaseController[Respuesta, RespuestaCreate, RespuestaUpdate]):
    def __init__(self):
        super().__init__(Respuesta)
