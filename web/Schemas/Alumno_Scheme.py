from pydantic import BaseModel


class AlumnoBase(BaseModel):
    nombre: str
    cedula: str


class AlumnoCreate(AlumnoBase):
    pass


class AlumnoUpdate(AlumnoBase):
    id: int


class AlumnoOut(AlumnoBase):
    id: int
