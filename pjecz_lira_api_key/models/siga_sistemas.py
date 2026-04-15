"""
SIGA Sistemas, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin


class SigaSistemas(UniversalMixin, table=True):
    """SigaSistemas"""

    # Nombre de la tabla
    __tablename__: str = "siga_sistemas"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Columnas
    clave: str = Field(max_length=16, unique=True)
    descripcion: str = Field(max_length=256)
    api_key: str = Field(max_length=128)
    buscar_agenda_url: str = Field(max_length=512)
    guardar_videos_url: str = Field(max_length=512)

    # Hijo
    autoridades: list["Autoridad"] = Relationship(back_populates="siga_sistema")

    def __repr__(self):
        """Representación"""
        return f"<SigaSistema {self.clave}>"
