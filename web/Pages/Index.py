import reflex as rx
from rxconfig import config
from web.Pages.Layout import layout
from web.Route import Route


@rx.page(Route.INDEX.value)
def index() -> rx.Component:
    # Welcome Page (Index)
    return layout(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
        )
    )
