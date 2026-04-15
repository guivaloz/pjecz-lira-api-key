"""
Distritos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin


class Distrito(UniversalMixin, table=True):
    """Distrito"""

    # Nombre de la tabla
    __tablename__: str = "distritos"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Columnas
    clave: str = Field(unique=True, max_length=16)
    nombre: str = Field(unique=True, max_length=256)
    nombre_corto: str = Field(max_length=64)
    es_distrito_judicial: bool = Field(default=False)
    es_distrito: bool = Field(default=False)
    es_jurisdiccional: bool = Field(default=False)
    es_activo: bool = Field(default=True)

    # Hijos
    autoridades: list["Autoridad"] = Relationship(back_populates="distrito")

    def __repr__(self):
        """Representación"""
        return f"<Distrito {self.clave}>"
