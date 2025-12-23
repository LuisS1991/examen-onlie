import reflex as rx
from web.States.AppState import AppState
from web.Schemas.Alumno_Scheme import AlumnoCreate


class AlumnoState(AppState):
    # _alumnoController = AlumnoController()
    # alumnos: List[Alumno]
    loading: bool = False

    async def laod_data(self):
        self.alumnos = await self._alumnoController.get_all()

    @rx.var
    def total_alumnos(self) -> int:
        return len(self.alumnos)

    @rx.event
    async def submit_alumno(self, form_data: dict):
        self.loading = True
        datos = AlumnoCreate(**form_data)
        result = await self._alumnoController.create(datos)
        if result:
            self.alumnos.append(result)
        self.loading = False

    @rx.event
    async def delete_alumno(self, id: int):
        result = await self._alumnoController.delete(id)
        if result:
            self.alumnos = [a for a in self.alumnos if a.id != id]
