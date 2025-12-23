from typing import List
from web.Modelos.Pregunta import Pregunta
from web.Schemas import PreguntaCreate, PreguntaUpdate, PreguntaOut, RespuestaOut
from web.Controlador.Base_Controller import BaseController


class PreguntaController(BaseController[Pregunta, PreguntaCreate, PreguntaUpdate]):
    def __init__(self):
        super().__init__(Pregunta)

    async def pregutnas_examen(self):
        resultado = await self.get_all_with_join(
            join_loads_params=[Pregunta.respuestas]
        )
        return self.map_preguntas(resultado)

    def map_preguntas(self, preguntas_orm: List) -> List[PreguntaOut]:
        result = []
        for p in preguntas_orm:
            pregunta_out = PreguntaOut(
                id=p.id,
                pregunta=p.pregunta.strip(),
                respuestas=[
                    RespuestaOut(
                        id=r.id,
                        respuesta=r.respuesta,
                        correcta=bool(r.correcta),
                        pregunta_id=r.pregunta_id,
                    )
                    for r in p.respuestas
                ],
            )
            result.append(pregunta_out)
        return result
