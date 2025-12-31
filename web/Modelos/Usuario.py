import reflex as rx
import sqlmodel as sm
from typing import Optional
from passlib.hash import bcrypt

class Usuario(rx.Model, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    nombre: str
    email: str
    password: str  # guardaremos el hash
    rol: str = "user"  # "admin" o "user"
