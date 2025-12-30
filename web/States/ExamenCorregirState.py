import reflex as rx
from web.States.AppState import AppState

class ExamenCorregirState(AppState):

    async def load_data(self):
        self.examen_presentados =await self._examenAlumnoController.get_all()
        print(self.examen_presentados)
