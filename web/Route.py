from enum import Enum


class RouteName(Enum):
    INDEX = "Home"
    ALUMNOS = "Alumnos"
    PREGUNTAS = "Preguntas"
    RESPUESTAS = "Respuestas"
    EXAMEN = "Examen"
    EXAMEN_CORREGIR = "Correcciones"


class Route(Enum):
    GENERICO="#"
    INDEX = "/"
    ALUMNOS = "/alumnos"
    PREGUNTAS = "/preguntas"
    RESPUESTAS = "/respuestas"
    EXAMEN = "/examen"
    EXAMEN_CORREGIR = "/examen/corregir"
