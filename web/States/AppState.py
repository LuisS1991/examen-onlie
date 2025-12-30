import reflex as rx
from typing import List
from web.Controlador import (
    AlumnoController,
    PreguntaController,
    RespuestaController,
    ExamenAlumnoController,
)
from web.Modelos import Alumno, Pregunta, Respuesta, RespuestaAlumno
from web.Schemas import PreguntaOut


class AppState(rx.State):
    _examenAlumnoController = ExamenAlumnoController()
    examen_presentados: List[RespuestaAlumno] = []
    _alumnoController = AlumnoController()
    alumnos: List[Alumno] = []

    _preguntaController = PreguntaController()
    preguntas: List[Pregunta] = []

    _respuestaController = RespuestaController()
    respuestas: List[Respuesta] = []

    preguntas_examen: List[PreguntaOut] = []
