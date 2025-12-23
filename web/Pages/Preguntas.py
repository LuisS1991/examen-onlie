import reflex as rx
from web.States.PreguntasState import PreguntaState
from web.Modelos.Pregunta import Pregunta


def table_row_item(item: Pregunta):
    return rx.table.row(
        rx.table.cell(item.id),
        rx.table.cell(item.pregunta),
        rx.table.cell(
            rx.icon(
                "x",
                class_name="hover:scale-150",
                on_click=lambda x: PreguntaState.delete_pregunta(item.id),
            )
        ),
    )


def tabla_datos() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("id"),
                rx.table.column_header_cell("Pregunta"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(PreguntaState.preguntas, table_row_item),
        ),
        width="100%",
    )


def form_data() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(rx.text_area(placeholder="escribir pregunta", name="pregunta")),
            rx.button("Guardar", type="submit", class_name="mt-4"),
            on_submit=PreguntaState.submit_pregunta,
            reset_on_submit=True,
        )
    )


@rx.page("/preguntas", on_load=PreguntaState.laod_data)
def preguntas() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Preguntas Examen 2025", size="9"),
            rx.spacer(),
            form_data(),
            rx.divider(),
            rx.cond(
                PreguntaState.total_preguntas > 0,
                tabla_datos(),
                rx.text("No hay datos cargados.....", size="4"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
