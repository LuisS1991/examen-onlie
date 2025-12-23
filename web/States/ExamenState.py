import reflex as rx
from web.States.AppState import AppState


class ExamenState(AppState):

    async def laod_data(self):
        self.preguntas_examen = await self._preguntaController.pregutnas_examen()
