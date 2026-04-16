"""
SIGA Videos, modelos
"""

import uuid
from datetime import datetime

from sqlalchemy.sql.functions import now
from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .siga_agendas import SigaAgenda
from .siga_salas import SigaSala


class SigaVideo(UniversalMixin, table=True):
    """SigaVideo"""

    # Nombre de la tabla
    __tablename__: str = "siga_videos"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    siga_agenda_id: uuid.UUID = Field(foreign_key="siga_agendas.id")
    siga_agenda: SigaAgenda = Relationship(back_populates="siga_videos")
    siga_sala_id: uuid.UUID = Field(foreign_key="siga_salas.id")
    siga_sala: SigaSala = Relationship(back_populates="siga_videos")

    # Columnas
    consecutivo: int
    descripcion: str = Field(max_length=256)
    inicio: datetime = Field(default=now())
    termino: datetime = Field(default=now())
    observaciones: str | None = Field(max_length=1024)

    # Columnas del video subido a GCS
    video_archivo: str | None = Field(max_length=64)
    video_blob: str | None = Field(max_length=256)
    video_mime_type: str | None = Field(max_length=256)
    video_tamano: int | None  # Tamaño en megabytes
    video_duracion: int | None  # Duración en segundos

    # Columnas cuando se ha transcrito
    transcripcion_json: str | None = Field(max_length=1024 * 1024)  # JSON
    transcripcion_txt: str | None = Field(max_length=1024 * 1024)

    def __repr__(self):
        """Representación"""
        return f"<SigaVideo {self.id}>"
