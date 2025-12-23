import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.text("Formulario creado con React + TypeScript"),
        class_name="mt-6 text-center text-sm text-gray-500",
    )
