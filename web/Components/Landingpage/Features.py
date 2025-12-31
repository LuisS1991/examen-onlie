import reflex as rx


def Features() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Discover amazing features and join our community today!",
            ),
        ),
    )
