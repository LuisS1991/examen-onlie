import reflex as rx


def card_title():
    return rx.box(
        rx.box(
            rx.icon("User", class_name="w-5 h-5 text-blue-600"),
            class_name="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center",
        ),
        rx.heading(
            "Información del Estudiante",
            as_="h2",
            class_name="text-lg md:text-xl font-semibold text-gray-900",
        ),
        class_name="flex items-center gap-3 mb-6",
    )


def card_body():
    return rx.box(
        rx.box(
            rx.text(
                "Nombre Completo",
                rx.text.span("*", class_name="text-red-500"),
                as_="label",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.input(
                type="text",
                placeholder="Ej: Juan Carlos García López",
                name="nombre_completo",
                class_name="w-full  rounded-lg border-2 border-gray-200 focus:border-blue-500 focus:outline-none transition-colors text-sm md:text-base",
            ),
        ),
        # cedula
        rx.box(
            rx.text(
                "Nro Cédula",
                rx.text.span("*", class_name="text-red-500"),
                as_="label",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.input(
                type="text",
                placeholder="Ej: 1234567890",
                name="cedula",
                class_name="w-full  rounded-lg border-2 border-gray-200 focus:border-blue-500 focus:outline-none transition-colors text-sm md:text-base",
            ),
        ),
        # grupo
        rx.box(
            rx.text(
                "Grupo",
                rx.text.span("*", class_name="text-red-500"),
                as_="label",
                class_name="block text-sm font-medium text-gray-700",
            ),
            rx.input(
                type="text",
                placeholder="Ej: G1-25",
                name="grupo",
                class_name="w-full  rounded-lg border-2 border-gray-200 focus:border-blue-500 focus:outline-none transition-colors text-sm md:text-base",
            ),
        ),
        class_name="space-y-4",
    )


def student_info_card() -> rx.Component:
    return rx.box(
        card_title(),
        card_body(),
        class_name="bg-white rounded-xl shadow-sm p-6 md:p-8 transition-all hover:shadow-md mb-6",
    )
