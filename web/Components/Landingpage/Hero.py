import reflex as rx

# Background
def background_gradient():
    return rx.box(
        class_name="absolute inset-0 bg-grid-slate-100 [mask-image:linear-gradient(0deg,white,rgba(255,255,255,0.6))] -z-10"
    )

# NAVBAR
def nav():
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.icon(
                        tag="graduation-cap",
                        class_name="h-8 w-8 text-blue-600",
                    ),
                    rx.text.span(
                        "ExamPro",
                        class_name="text-2xl font-bold text-gray-900",
                    ),
                    class_name="flex items-center space-x-2",
                ),
                rx.box(
                    rx.link(
                        "Características",
                        href="#features",
                        class_name="text-gray-600 hover:text-blue-600 transition-colors",
                    ),
                    rx.link(
                        "Cómo Funciona",
                        href="#how-it-works",
                        class_name="text-gray-600 hover:text-blue-600 transition-colors",
                    ),
                    rx.button(
                        "Comenzar",
                        class_name="bg-blue-600 text-white px-6 py-2 rounded-lg "
                        "hover:bg-blue-700 transition-colors",
                    ),
                    class_name="hidden md:flex items-center space-x-8",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="container mx-auto px-4 py-6",
        )
    )

def hero_content():
    # HERO CONTENT
    return rx.box(
        rx.box(
            # LEFT COLUMN
            rx.box(
                rx.heading(
                    "Evalúa a tus estudiantes de forma ",
                    rx.text.span(
                        "inteligente",
                        class_name="text-blue-600",
                    ),
                    as_="h1",
                    class_name="text-4xl md:text-6xl font-bold text-gray-900 leading-tight",
                ),
                rx.text(
                    "Crea, administra y corrige exámenes automáticamente. "
                    "La plataforma completa para gestionar evaluaciones online.",
                    class_name="text-lg md:text-xl text-gray-600 leading-relaxed",
                    as_="p",
                ),
                rx.box(
                    rx.button(
                        "Empezar Gratis",
                        rx.icon(
                            tag="arrow-right",
                            class_name="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform",
                        ),
                        class_name="bg-blue-600 text-white px-8 py-4 rounded-lg "
                        "hover:bg-blue-700 transition-all hover:shadow-xl "
                        "flex items-center justify-center group",
                    ),
                    rx.button(
                        "Ver Demo",
                        class_name="border-2 border-gray-300 text-gray-700 px-8 py-4 "
                        "rounded-lg hover:border-blue-600 hover:text-blue-600 "
                        "transition-colors",
                    ),
                    class_name="flex flex-col sm:flex-row gap-4",
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            "10K+",
                            class_name="text-3xl font-bold text-gray-900",
                        ),
                        rx.box(
                            "Exámenes Creados",
                            class_name="text-sm text-gray-600",
                        ),
                    ),
                    rx.box(
                        rx.box(
                            "50K+",
                            class_name="text-3xl font-bold text-gray-900",
                        ),
                        rx.box(
                            "Estudiantes Activos",
                            class_name="text-sm text-gray-600",
                        ),
                    ),
                    class_name="flex items-center space-x-8 pt-4",
                ),
                class_name="space-y-6",
            ),
            # RIGHT COLUMN (CARD)
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.text.span(
                                "Examen: Matemáticas",
                                class_name="text-sm font-medium text-gray-500",
                            ),
                            rx.text.span(
                                "En Progreso",
                                class_name="bg-green-100 text-green-700 px-3 py-1 "
                                "rounded-full text-xs font-medium",
                            ),
                            class_name="flex items-center justify-between",
                        ),
                        rx.box(
                            rx.box(
                                class_name="h-full bg-blue-600 rounded-full",
                                style={"width": "60%"},
                            ),
                            class_name="h-2 bg-gray-200 rounded-full overflow-hidden",
                        ),
                        rx.box(
                            rx.foreach(
                                [1, 2, 3],
                                lambda i: rx.box(
                                    rx.box(
                                        1,
                                        class_name="w-8 h-8 bg-blue-100 rounded-full "
                                        "flex items-center justify-center "
                                        "text-blue-600 font-medium",
                                    ),
                                    rx.box(
                                        class_name="flex-1 h-4 bg-gray-100 rounded",
                                    ),
                                    class_name="flex items-center space-x-3",
                                ),
                            ),
                            class_name="space-y-3",
                        ),
                        class_name="space-y-4",
                    ),
                    class_name="bg-white rounded-2xl shadow-2xl p-8 "
                    "transform hover:scale-105 transition-transform",
                ),
                rx.box(
                    rx.box(
                        "95%",
                        class_name="text-2xl font-bold",
                    ),
                    rx.box(
                        "Precisión",
                        class_name="text-xs",
                    ),
                    class_name="absolute -bottom-4 -right-4 bg-blue-600 "
                    "text-white p-4 rounded-xl shadow-xl",
                ),
                class_name="relative hidden md:block",
            ),
            class_name="grid md:grid-cols-2 gap-12 items-center",
        ),
        class_name="container mx-auto px-4 py-20 md:py-32",
    )
