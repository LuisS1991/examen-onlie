import reflex as rx
from web.Schemas.MenuItemScheme import MenuItemScheme
from web.Route import Route, RouteName

links_web = [
    MenuItemScheme(
        name=RouteName.INDEX.value, link=Route.INDEX.value, icon="home", subMenu=[]
    ),
    MenuItemScheme(
        name=RouteName.ALUMNOS.value,
        link=Route.ALUMNOS.value,
        icon="users",
        subMenu=[],
    ),
    MenuItemScheme(
        name="Propuesta",
        link=Route.GENERICO.value,
        icon="mail",
        subMenu=[
            MenuItemScheme(
                name=RouteName.PREGUNTAS.value,
                link=Route.PREGUNTAS.value,
                icon="",
                subMenu=[],
            ),
            MenuItemScheme(
                name=RouteName.RESPUESTAS.value,
                link=Route.RESPUESTAS.value,
                icon="",
                subMenu=[],
            ),
        ],
    ),
    MenuItemScheme(
        name="Evaluaciones",
        link=Route.GENERICO.value,
        icon="layers",
        subMenu=[
            MenuItemScheme(
                name=RouteName.EXAMEN.value,
                link=Route.EXAMEN.value,
                icon="",
                subMenu=[],
            ),
            MenuItemScheme(
                name=RouteName.EXAMEN_CORREGIR.value,
                link=Route.EXAMEN_CORREGIR.value,
                icon="",
                subMenu=[],
            ),
        ],
    ),
]


# DESKTOP
def navbar_icons_item(link_web: MenuItemScheme) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(link_web.icon), rx.text(link_web.name, size="4", weight="medium")
        ),
        href=link_web.link,
    )


# MOVIL
def navbar_icons_menu_item(link_web: MenuItemScheme) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(link_web.icon, size=16),
            rx.text(link_web.name, size="3", weight="medium"),
        ),
        href=link_web.link,
    )


# ITEM SUB MENU
def sub_menu_item(link: MenuItemScheme):
    return rx.menu.item(rx.link(link.name, href=link.link, class_name="w-full text-center"))


# MENU SON SUB NIVEL
def item_sub_menu(link_web: MenuItemScheme):
    return rx.hstack(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.text(link_web.name, size="4", weight="medium"),
                    rx.icon("chevron-down"),
                    weight="medium",
                    variant="ghost",
                    size="3",
                ),
            ),
            rx.menu.content(
                rx.foreach(link_web.subMenu, sub_menu_item),
            ),
        )
    )


# ELIGE TIPO MENU
def item_menu(link_web: MenuItemScheme):

    return rx.cond(
        link_web.subMenu.length() > 0,
        item_sub_menu(link_web=link_web),
        navbar_icons_item(link_web=link_web),
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    rx.foreach(links_web, item_menu),
                    spacing="6",
                ),
                rx.color_mode.button(position="top-right"),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.foreach(links_web, navbar_icons_menu_item),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
