import reflex as rx


def Footer_Landing() -> rx.Component:
    return rx.box(
        rx.text(
            "© 2024 My Company. All rights reserved.",
            class_name="text-sm text-gray-500",
        ),
        class_name="w-full py-4 bg-gray-100 flex justify-center",
    )
