from web.Pages.Layout import layout
from web.Pages.Index import index
from web.Pages.Alumnos import alumnos
from web.Pages.Preguntas import preguntas
from web.Pages.Respuestas import respuestas
from web.Pages.Examen import examen
from web.Pages.CorregirExamen import corregir_examen
from web.Pages.Auth import Login, Registrar

__all__ = [
    "layout",
    "index",
    "preguntas",
    "alumnos",
    "respuestas",
    "examen",
    "corregir_examen",
    "Registrar",
    "Login",
]
