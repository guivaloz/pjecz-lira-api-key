"""
UniversalMixin define las columnas y métodos comunes de todos los modelos
"""

from datetime import datetime

from sqlalchemy.sql.functions import now
from sqlmodel import Field, SQLModel


class UniversalMixin(SQLModel, table=False):
    """Columnas y métodos comunes a todas las tablas"""

    creado: datetime = Field(default=now())
    modificado: datetime = Field(default=now())
    estatus: str = Field(max_length=1, default="A")
