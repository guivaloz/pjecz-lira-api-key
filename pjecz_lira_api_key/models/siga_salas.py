"""
SIGA Salas, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .domicilios import Domicilio


class SigaSala(UniversalMixin, table=True):
    """SigaSala"""

    # Nombre de la tabla
    __tablename__: str = "siga_salas"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Clave foránea
    domicilio_id: uuid.UUID = Field(foreign_key="domicilios.id")
    domicilio: Domicilio = Relationship(back_populates="siga_salas")

    # Columnas
    clave: str = Field(max_length=16, unique=True)
    descripcion: str = Field(max_length=256)
    direccion_ip: str | None = Field(max_length=64)
    direccion_nvr: str | None = Field(max_length=64)
    es_activo: bool = Field(default=True)
    tablero_icono: str | None = Field(max_length=64)

    # Hijos
    siga_videos: list["SigaVideo"] = Relationship(back_populates="siga_sala")

    def __repr__(self):
        """Representación"""
        return f"<SigaSala {self.clave}>"
