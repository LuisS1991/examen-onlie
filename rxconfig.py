import os
import reflex as rx
<<<<<<< HEAD
from dotenv import load_dotenv

# Cargar .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///examen_2025.db")

config = rx.Config(
    app_name="web",
    #frontend_port=80,
    db_url=DATABASE_URL,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
=======
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

>>>>>>> 7ad2bc4bad4e5b921d71de5b56014990930fe39d
)

