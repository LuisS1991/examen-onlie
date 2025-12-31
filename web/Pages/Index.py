import reflex as rx
from rxconfig import config
from web.Components.Landingpage import  Features, HowItWorks, CTA, Footer_Landing
from web.Secciones.Hero_Seccion import Hero_Seccion 
from web.Route import Route


@rx.page(Route.INDEX.value)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        Hero_Seccion(),
        Features(),
        HowItWorks(),
        CTA(),
        rx.box(
            rx.button(
                "Iniciar Sesión",
                class_name="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-all shadow-lg hover:shadow-xl font-semibold",
                on_click=rx.redirect(Route.LOGIN.value),
            ),
            rx.button(
                "Registrarse",
                class_name="bg-cyan-600 text-white px-6 py-3 rounded-lg hover:bg-cyan-700 transition-all shadow-lg hover:shadow-xl font-semibold",
                on_click=rx.redirect(Route.REGISTRAR.value),
            ),
            class_name="fixed bottom-8 right-8 flex gap-4 z-50",
        ),
        Footer_Landing(),
        class_name="min-h-screen bg-white",
    )
