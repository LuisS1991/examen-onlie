import reflex as rx
from web.Components.NavBar import navbar_icons

def layout(children: rx.Component) -> rx.Component:
    return rx.container(
        navbar_icons(),
        rx.vstack(
            children,
              class_name="w-full",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
