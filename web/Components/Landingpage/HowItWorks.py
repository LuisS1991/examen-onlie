import reflex as rx


def HowItWorks() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Evaluación Automática!",
            ),
        ),
    )
