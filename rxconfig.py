import os
import reflex as rx
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
)

