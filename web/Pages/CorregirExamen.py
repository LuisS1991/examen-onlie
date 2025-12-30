import reflex as rx
from web.States import ExamenCorregirState
from web.Route import Route
from web.Pages.Layout import layout
from web.Modelos import RespuestaAlumno


def examen_card(examen: RespuestaAlumno):
    return rx.card(examen.id, height="10vh")


@rx.page(Route.EXAMEN_CORREGIR.value, on_load=ExamenCorregirState.load_data)
def corregir_examen() -> rx.Component:
    return layout(
        rx.center(
            rx.vstack(
                rx.heading("Corrección de Examen", as_="h2", size="4"),
                rx.grid(
                    rx.foreach(ExamenCorregirState.examen_presentados, examen_card),
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                class_name="w-full",
            ),
            class_name="w-full",
        )
    )
