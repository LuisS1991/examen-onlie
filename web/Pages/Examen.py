import reflex as rx

from web.Components import (
    forms_header,
    student_info_card,
    footer_examen,
    submit_button,
    multiple_choice_question,
)
from web.States.ExamenState import ExamenState
from web.Route import Route

@rx.page(Route.EXAMEN.value, on_load=ExamenState.laod_data)
def examen() -> rx.Component:
    return rx.box(
        rx.box(
            rx.form(
                forms_header(
                    title="Examen Informatica - 2025",
                    desc="examen final de la materia informatica academia privada",
                ),
                student_info_card(),
                rx.foreach(ExamenState.preguntas_examen, multiple_choice_question),
                submit_button(),
                on_submit=ExamenState.sumbit_response,
                reset_on_submit=True
            ),
            footer_examen(),
            class_name="max-w-2xl mx-auto",
        ),
        class_name="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 py-8 px-4",
    )
