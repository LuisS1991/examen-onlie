import reflex as rx
from web.States.ExamenState import ExamenState


def submit_button():
    return rx.box(
        rx.button(
           f"Enviar Respuesta",
            type="submit",
            disabled=ExamenState.toggle_optional_submit_button,
            class_name=rx.cond(
                ExamenState.toggle_optional_submit_button,
                "w-full md:w-auto px-8 py-3 rounded-lg font-medium text-white transition-all duration-200 bg-gray-300 cursor-not-allowed",
                "w-full md:w-auto px-8 py-3 rounded-lg font-medium text-white transition-all duration-200 bg-gray-300 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 hover:shadow-lg transform hover:-translate-y-0.5",
            ),
        ),
        rx.cond(
            ExamenState.toggle_optional_submit_button,
            rx.text(
                "Por favor responde todas las preguntas requeridas",
                as_="p",
                class_name="text-sm text-gray-500 mt-3",
            ),
        ),
        class_name="bg-white rounded-xl shadow-sm p-6 md:p-8",
    )
