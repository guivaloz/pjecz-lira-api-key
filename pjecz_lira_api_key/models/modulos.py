"""
Modulos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin


class Modulo(UniversalMixin, table=True):
    """Modulo"""

    # Nombre de la tabla
    __tablename__: str = "modulos"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Columnas
    nombre: str = Field(unique=True, max_length=256)
    nombre_corto: str = Field(max_length=64)
    icono: str = Field(max_length=48)
    ruta: str = Field(max_length=64)
    en_navegacion: bool = Field(default=False)

    # Hijos
    bitacoras: list["Bitacora"] = Relationship(back_populates="modulo")
    permisos: list["Permiso"] = Relationship(back_populates="modulo")

    def __repr__(self):
        """Representación"""
        return f"<Modulo {self.nombre}>"
