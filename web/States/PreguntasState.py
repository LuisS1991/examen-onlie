import reflex as rx
from web.States.AppState import AppState
from web.Schemas.Pregunta_Scheme import PreguntaCreate


class PreguntaState(AppState):
    # _preguntaController = PreguntaController()
    # preguntas: List[Pregunta]
    # loading: bool = False

    async def laod_data(self):
        self.preguntas = await self._preguntaController.get_all()

    @rx.var
    def total_preguntas(self) -> int:
        return len(self.preguntas)

    @rx.event
    async def submit_pregunta(self, form_data: dict):
        datos = PreguntaCreate(**form_data)
        result = await self._preguntaController.create(datos)
        if result:
            self.preguntas.append(result)

    @rx.event
    async def delete_pregunta(self, id: int):
        result = await self._preguntaController.delete(id)
        if result:
            self.preguntas = [p for p in self.preguntas if p.id != id]
