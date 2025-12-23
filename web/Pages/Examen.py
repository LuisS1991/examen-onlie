import reflex as rx

from web.Components import (
    forms_header,
    student_info_card,
    footer,
    submit_button,
    multiple_choice_question,
    true_false_question,
)
from web.States.ExamenState import ExamenState


@rx.page("/examen", on_load=ExamenState.laod_data)
def examen() -> rx.Component:
    return rx.box(
        rx.box(
            forms_header(
                title="Examen Informatica - 2025",
                desc="examen final de la materia informatica academia privada",
            ),
            student_info_card(),
            rx.foreach(ExamenState.preguntas_examen, multiple_choice_question),
            submit_button(),
            footer(),
            class_name="max-w-2xl mx-auto",
        ),
        class_name="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 py-8 px-4",
    )
