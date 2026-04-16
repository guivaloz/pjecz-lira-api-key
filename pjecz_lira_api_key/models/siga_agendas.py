"""
SIGA Agendas, modelos
"""

import uuid
from datetime import date, time

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .siga_expedientes import SigaExpediente


class SigaAgenda(UniversalMixin, table=True):
    """SigaAgenda"""

    # Nombre de la tabla
    __tablename__: str = "siga_agendas"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    siga_expediente_id: uuid.UUID = Field(foreign_key="siga_expedientes.id")
    siga_expediente: SigaExpediente = Relationship(back_populates="siga_agendas")

    # Columnas
    juez: str = Field(max_length=256)
    secretario: str = Field(max_length=256)
    tipo_audiencia: str = Field(max_length=256)
    fecha: date
    hora_inicio: time
    hora_finalizacion: time
    saji_agenda_id: int = Field(unique=True)

    # Hijos
    siga_videos: list["SigaVideo"] = Relationship(back_populates="siga_agenda")

    def __repr__(self):
        """Representación"""
        return f"<SigaAgenda {self.id}>"
