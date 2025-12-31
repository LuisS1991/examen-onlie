"""seed usuario default

Revision ID: 79c5c9585ff1
Revises: 442a7fa7fb21
Create Date: 2025-12-31 10:18:30.265715

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from passlib.hash import bcrypt


# revision identifiers, used by Alembic.
revision: str = "79c5c9585ff1"
down_revision: Union[str, Sequence[str], None] = "442a7fa7fb21"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()

    # verifica si el admin ya existe
    exists = conn.execute(
        sa.text("SELECT 1 FROM usuario WHERE email = :email"),
        {"email": "nantesluis72@gmail.com"},
    ).fetchone()

    if not exists:
        # crear hash de la contraseña
        hashed_pw = bcrypt.hash("1234")  # cambiar por tu contraseña inicial segura

        conn.execute(
            sa.text(
                "INSERT INTO usuario (nombre, email, password, rol,activo) "
                "VALUES (:nombre, :email, :password, :rol,:activo)"
            ),
            {
                "nombre": "Luis Nantes",
                "email": "nantesluis72@gmail.com",
                "password": hashed_pw,
                "rol": "docente",
                "activo": True,
            },
        )


def downgrade() -> None:
    """Downgrade schema."""
    conn = op.get_bind()
    conn.execute(sa.text("DELETE FROM usuario WHERE email = 'nantesluis72@gmail.com'"))
