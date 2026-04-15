"""
Domiiclios, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin


class Domicilio(UniversalMixin, table=True):
    """Domicilio"""

    # Nombre de la tabla
    __tablename__: str = "domicilios"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Columnas
    clave: str = Field(max_length=16, unique=True)
    edificio: str = Field(max_length=64, unique=True)
    domicilio_completo: str = Field(max_length=1024)
    es_activo: bool = Field(default=True)

    # Hijos
    siga_salas: list["SigaSala"] = Relationship(back_populates="domicilio")

    def __repr__(self):
        """Representación"""
        return f"<Domicilio {self.clave}>"
