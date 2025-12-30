import reflex as rx
from web.States import ExamenState
from web.Schemas import PreguntaOut, RespuestaOut


def pregunta(pregunta: str):
    return rx.box(
        rx.heading(
            pregunta,
            rx.text.span("*", class_name="text-red-500 ml-1"),
            as_="h3",
            class_name="text-base md:text-lg text-gray-900 font-medium",
        ),
        class_name="mb-6",
    )


def respuestas_item(option: RespuestaOut):
    #Estado para verificar si esta opción está seleccionada
    #selected_options.get(option.pregunta_id) == option.id
    is_selected = ExamenState.is_selected_op.contains(f"{option.pregunta_id}-{option.id}")
    return rx.text(
        is_selected,
        # Input tipo radio oculto
        rx.input(
            type="radio",
            class_name="sr-only",
            checked=is_selected,
            on_click=lambda e: ExamenState.toggle_optional_selected(
                pregunta_id=option.pregunta_id, respuesta_id=option.id
            ),
        ),
        # Circulo del radio
        rx.box(
            rx.icon("Circle", class_name="w-2 h-2 fill-white text-white"),
            class_name=rx.cond(
                is_selected,
                "flex-shrink-0 w-5 h-5 rounded-full border-2 mr-4 flex items-center justify-center transition-all border-blue-500 bg-blue-500",
                "flex-shrink-0 w-5 h-5 rounded-full border-2 mr-4 flex items-center justify-center transition-all border-gray-400 group-hover:border-blue-400",
            ),
        ),
        # Texto de la opción
        rx.text.span(
            option.respuesta,
            class_name=rx.cond(
                is_selected,
                "text-sm md:text-base transition-colors text-gray-900 font-medium",
                "text-sm md:text-base transition-colors text-gray-700",
            ),
        ),
        as_="label",
        # Estilo del contenedor de la opción
        class_name=rx.cond(
            is_selected,
            "flex items-center p-4 rounded-lg border-2 cursor-pointer transition-all duration-200 group border-blue-500 bg-blue-50",
            "mb-2 flex items-center p-4 rounded-lg border-2 cursor-pointer transition-all duration-200 group border-gray-200 hover:border-blue-300 hover:bg-gray-50",
        ),
    )


def multiple_choice_question(p: PreguntaOut) -> rx.Component:
    return rx.box(
        pregunta(p.pregunta),
        rx.foreach(p.respuestas, respuestas_item),
        class_name="bg-white rounded-xl shadow-sm p-6 md:p-8 transition-all hover:shadow-md mb-6",
    )
