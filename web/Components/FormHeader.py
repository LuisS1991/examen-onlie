import reflex as rx


def forms_header(title: str, desc: str) -> rx.Component:
    return rx.box(
        rx.heading(
            title,
            as_="h1",
            class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-3",
        ),
        rx.text(
            desc,
            as_="p",
            class_name="text-gray-600 text-sm md:text-base leading-relaxed",
        ),
        class_name="bg-white rounded-t-2xl border-t-8 border-blue-500 shadow-sm p-8 mb-6",
    )
