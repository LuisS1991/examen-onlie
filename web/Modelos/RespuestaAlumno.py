import reflex as rx


class RespuestaAlumno(rx.Model, table=True):
    alumno_id: int
    pregunta_id: int
    respuesta_id: int
