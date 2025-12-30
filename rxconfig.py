import reflex as rx
config = rx.Config(
    app_name="web",
    db_url="sqlite:///examen_2025.db",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://web-2514y8nbl8ye.up-de-fra1-k8s-1.apps.run-on-seenode.com"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]

)

