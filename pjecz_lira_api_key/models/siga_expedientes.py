"""
SIGA Expedientes, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .autoridades import Autoridad


class SigaExpediente(UniversalMixin, table=True):
    """SigaExpediente"""

    # Nombre de la tabla
    __tablename__: str = "siga_expedientes"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Clave foránea
    autoridad_id: uuid.UUID = Field(foreign_key="autoridades.id")
    autoridad: Autoridad = Relationship(back_populates="siga_expedientes")

    # Columnas
    numero_expediente: str = Field(max_length=32)
    tipo_juicio: str = Field(max_length=256)
    observaciones: str | None = Field(max_length=1024)
    saji_expediente_id: int = Field(unique=True)

    # Hijos
    siga_agendas: list["SigaAgenda"] = Relationship(back_populates="siga_expediente")

    def __repr__(self):
        """Representación"""
        return f"<SigaExpediente {self.id}>"
