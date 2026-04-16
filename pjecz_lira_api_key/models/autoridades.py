"""
Autoridad
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .distritos import Distrito
from .siga_sistemas import SigaSistema


class Autoridad(UniversalMixin, table=True):
    """Autoridad"""

    # Nombre de la tabla
    __tablename__: str = "autoridades"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    distrito_id: uuid.UUID = Field(foreign_key="distritos.id")
    distrito: Distrito = Relationship(back_populates="autoridades")
    siga_sistema_id: uuid.UUID = Field(foreign_key="siga_sistemas.id")
    siga_sistema: SigaSistema = Relationship(back_populates="autoridades")

    # Columnas
    clave: str = Field(unique=True, max_length=16)
    descripcion: str = Field(max_length=256)
    descripcion_corta: str = Field(max_length=64)
    es_jurisdiccional: bool = Field(default=False)
    es_activo: bool = Field(default=True)

    # Hijos
    siga_expedientes: list["SigaExpediente"] = Relationship(back_populates="autoridad")
    usuarios: list["Usuario"] = Relationship(back_populates="autoridad")

    @property
    def distrito_clave(self):
        """Clave del distrito"""
        return self.distrito.clave

    @property
    def distrito_nombre(self):
        """Nombre del distrito"""
        return self.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Nombre corto del distrito"""
        return self.distrito.nombre_corto

    def __repr__(self):
        """Representación"""
        return f"<Autoridad {self.clave}>"
