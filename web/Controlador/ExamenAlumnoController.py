from web.Modelos.RespuestaAlumno import RespuestaAlumno
from web.Schemas.RespuesAlumnoExamen_Scheme import RespuesAlumnoExamenCreate, RespuesAlumnoExamenUpdate
from web.Controlador.Base_Controller import BaseController
from typing import List

class ExamenAlumnoController(BaseController[RespuestaAlumno, RespuesAlumnoExamenCreate, RespuesAlumnoExamenUpdate]):
    def __init__(self):
        super().__init__(RespuestaAlumno)

    
    async def create_exam(self,response:List[RespuesAlumnoExamenCreate]):
        if len(response) > 0:
            for res in response: 
               await self.create(res)
