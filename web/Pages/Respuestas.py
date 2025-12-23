import reflex as rx
from web.Modelos.Respuesta import Respuesta
from web.Modelos.Pregunta import Pregunta
from web.States.RespuestaState import RespuestaState


def table_row_item(item: Respuesta):
    return rx.table.row(
        rx.table.cell(item.id),
        rx.table.cell(item.respuesta),
        rx.table.cell(rx.cond(item.correcta == 1, "SI", "NO")),
        rx.table.cell(
            rx.icon(
                "x",
                class_name="hover:scale-150",
                on_click=lambda x: RespuestaState.delete_respuesta(item.id),
            )
        ),
    )


def tabla_datos() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("id"),
                rx.table.column_header_cell("Respuesta"),
                rx.table.column_header_cell("correcta"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(RespuestaState.respuestas, table_row_item),
        ),
        width="100%",
    )


def select_items(p: Pregunta):
    return rx.select.item(p.pregunta, value=f"{p.id.to_string()}")


def select_forms():
    return rx.select.root(
        rx.select.trigger(placeholder="Seleccionar un pregunta"),
        rx.select.content(
            rx.select.group(rx.foreach(RespuestaState.preguntas, select_items)),
        ),
        name="pregunta_id",
    )


def form_data() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Escriba su respuesta", name="respuesta"),
                select_forms(),
                rx.checkbox("Correcta", name="correcta"),
            ),
            rx.button("Guardar", type="submit", class_name="mt-4"),
            on_submit=RespuestaState.submit_respuesta,
            reset_on_submit=True,
        )
    )


@rx.page("/respuestas", on_load=RespuestaState.laod_data)
def respuestas() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Respuestas Curso 2025", size="9"),
            form_data(),
            rx.spacer(),
            rx.divider(),
            rx.cond(
                RespuestaState.total_respuestas > 0,
                tabla_datos(),
                rx.text("No hay datos cargados"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
