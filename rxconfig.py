import reflex as rx

config = rx.Config(
    app_name="web",
    db_url="sqlite:///examen_2025.db",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]

)
