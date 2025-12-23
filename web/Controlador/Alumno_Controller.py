from web.Modelos.Alumno import Alumno
from web.Schemas.Alumno_Scheme import AlumnoCreate, AlumnoUpdate
from web.Controlador.Base_Controller import BaseController


class AlumnoController(BaseController[Alumno, AlumnoCreate, AlumnoUpdate]):
    def __init__(self):
        super().__init__(Alumno)
