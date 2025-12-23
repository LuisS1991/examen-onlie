import reflex as rx
from typing import List
from web.Controlador import AlumnoController, PreguntaController, RespuestaController
from web.Modelos import Alumno, Pregunta, Respuesta
from web.Schemas import PreguntaOut

class AppState(rx.State):
    _alumnoController = AlumnoController()
    alumnos: List[Alumno] = []

    _preguntaController = PreguntaController()
    preguntas: List[Pregunta] = []

    _respuestaController = RespuestaController()
    respuestas: List[Respuesta] = []

    preguntas_examen:List[PreguntaOut] = []