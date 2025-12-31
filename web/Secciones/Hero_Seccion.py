import reflex as rx
from web.Components.Landingpage.Hero import background_gradient

def Hero_Seccion():
    return rx.container(
        background_gradient(),
        class_name="w-full relative bg-gradient-to-br from-blue-50 to-cyan-50 overflow-hidden",
    )
