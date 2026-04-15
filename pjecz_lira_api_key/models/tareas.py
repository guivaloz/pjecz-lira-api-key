"""
Tareas, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .usuarios import Usuario


class Tarea(UniversalMixin, table=True):
    """Tarea"""

    # Nombre de la tabla
    __tablename__: str = "tareas"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Clave foránea
    usuario_id: uuid.UUID = Field(foreign_key="usuarios.id")
    usuario: Usuario = Relationship(back_populates="tareas")

    # Columnas
    archivo: str = Field(max_length=256)
    comando: str = Field(max_length=256)
    ha_terminado: bool = Field(default=False)
    mensaje: str = Field(max_length=1024)
    url: str = Field(max_length=512)

    def __repr__(self):
        """Representación"""
        return f"<Tarea {self.id}>"
