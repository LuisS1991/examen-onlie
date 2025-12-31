import reflex as rx
from web.Route import Route

@rx.page(Route.LOGIN.value)
def Login() -> rx.Component:
    return rx.box(
        rx.text("Página de Inicio de Sesión", class_name="text-2xl font-bold"),
        class_name="min-h-screen flex items-center justify-center bg-gray-100",
    )