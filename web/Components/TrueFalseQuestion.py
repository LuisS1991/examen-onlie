import reflex as rx
from web.States.IndexState import IndexState


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


def radio_input(option: str):
    return rx.text(
        rx.input(type="radio", class_name="sr-only"),
        rx.box(
            rx.icon("Circle", class_name="w-2 h-2 fill-white text-white"),
            class_name=rx.cond(
                IndexState.is_selected_option_bool,
                "flex-shrink-0 w-5 h-5 rounded-full border-2 mr-4  flex items-center justify-center transition-all border-blue-500 bg-blue-500",
                "flex-shrink-0 w-5 h-5 rounded-full border-2 mr-4  flex items-center justify-center transition-all border-gray-400 group-hover:border-blue-400",
            ),
        ),
        rx.text.span(
            option,
            class_name=rx.cond(
                IndexState.is_selected_option_bool,
                "text-sm md:text-base transition-colors text-gray-900 font-medium",
                "text-sm md:text-base transition-colors text-gray-700",
            ),
        ),
        as_="label",
        class_name=rx.cond(
            IndexState.is_selected_option_bool,
            "flex items-center p-4 rounded-lg border-2 cursor-pointer transition-all duration-200 group border-blue-500 bg-blue-50",
            "flex items-center p-4 rounded-lg border-2 cursor-pointer transition-all duration-200 group border-gray-200 hover:border-blue-300 hover:bg-gray-50",
        ),
        on_click=IndexState.toggle_optional_selected,
    )


def respuesta():
    return rx.box(
        radio_input("Verdadero"), radio_input("Falso"), class_name="space-y-3"
    )


def true_false_question():
    return rx.box(
        pregunta("Pregunta 2"),
        respuesta(),
        class_name="bg-white rounded-xl shadow-sm p-6 md:p-8 transition-all hover:shadow-md mb-6",
    )
