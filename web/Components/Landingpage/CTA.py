import reflex as rx


def CTA() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "CTA",
            ),
        ),
    )
