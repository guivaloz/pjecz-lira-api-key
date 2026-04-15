"""
Bitácoras, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .modulos import Modulo
from .usuarios import Usuario


class Bitacora(UniversalMixin, table=True):
    """Bitacora"""

    # Nombre de la tabla
    __tablename__: str = "bitacoras"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    modulo_id: uuid.UUID = Field(foreign_key="modulos.id")
    modulo: Modulo = Relationship(back_populates="bitacoras")
    usuario_id: uuid.UUID = Field(foreign_key="usuarios.id")
    usuario: Usuario = Relationship(back_populates="bitacoras")

    # Columnas
    descripcion: str = Field(max_length=256)
    url: str = Field(max_length=256)

    def __repr__(self):
        """Representación"""
        return f"<Bitacora {self.id}>"
