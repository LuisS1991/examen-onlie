from web.Modelos.Usuario import Usuario
from web.Schemas.Usuario_Scheme import  UsuarioCreate, UsuarioUpdate
from web.Controlador.Base_Controller import BaseController


class UsuarioController(BaseController[Usuario, UsuarioCreate, UsuarioUpdate]):
    def __init__(self):
        super().__init__(Usuario)