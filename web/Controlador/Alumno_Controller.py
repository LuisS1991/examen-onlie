from web.Modelos.Alumno import Alumno
from web.Schemas.Alumno_Scheme import AlumnoCreate, AlumnoUpdate
from web.Controlador.Base_Controller import BaseController


class AlumnoController(BaseController[Alumno, AlumnoCreate, AlumnoUpdate]):
    def __init__(self):
        super().__init__(Alumno)

    async def find_cedula(self,cedula):
       return await self.get_by_one_with_filters([Alumno.cedula == cedula])
         
        