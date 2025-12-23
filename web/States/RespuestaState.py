import reflex as rx
from web.States.AppState import AppState
from web.Schemas.Respuesta_Scheme import RespuestaCreate


class RespuestaState(AppState):
    # _respuestaController = RespuestaController()
    # respuestas: List[Respuesta]

    async def laod_data(self):
        self.preguntas = await self._preguntaController.get_all()
        self.respuestas = await self._respuestaController.get_all()

    @rx.var
    def total_respuestas(self) -> int:
        return len(self.respuestas)


    @rx.event
    async def submit_respuesta(self, form_data: dict):
        datos = RespuestaCreate(
            respuesta=form_data["respuesta"],
            correcta=1 if "correcta" in form_data and form_data.get("correcta") == "on" else 0,
            pregunta_id=int(form_data["pregunta_id"]),
        )
        result = await self._respuestaController.create(datos)
        if result:
            self.respuestas.append(result)

    @rx.event
    async def delete_respuesta(self, id: int):
        result = await self._respuestaController.delete(id)
        if result:
            self.respuestas = [p for p in self.respuestas if p.id != id]
