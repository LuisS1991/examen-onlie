import reflex as rx
from web.States.AlumnoState import AlumnoState
from web.Modelos.Alumno import Alumno


def table_row_item(item: Alumno):
    return rx.table.row(
        rx.table.cell(item.id),
        rx.table.cell(item.cedula),
        rx.table.cell(item.nombre),
        rx.table.cell(
            rx.icon(
                "x",
                class_name="hover:scale-150",
                on_click=lambda x: AlumnoState.delete_alumno(item.id),
            )
        ),
    )


def tabla_datos() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("id"),
                rx.table.column_header_cell("Cedula"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(AlumnoState.alumnos, table_row_item),
        ),
        width="100%",
    )


def form_alumnos() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Nombre", name="nombre"),
                rx.input(placeholder="Cedula", name="cedula"),
            ),
            rx.cond(
                AlumnoState.loading,
                rx.text(
                    "Guardando Datos....",
                    class_name="mt-4",
                ),
                rx.button(
                    "Guardar",
                    type="submit",
                    class_name="mt-4",
                ),
            ),
            on_submit=AlumnoState.submit_alumno,
            reset_on_submit=True,
        ),
    )


@rx.page("/alumnos", on_load=AlumnoState.laod_data)
def alumnos() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Alumnos Curso 2025", size="9"),
            form_alumnos(),
            rx.spacer(),
            rx.divider(),
            rx.cond(
                AlumnoState.total_alumnos > 0,
                tabla_datos(),
                rx.text("Loading...."),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
