"""
Permisos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .modulos import Modulo
from .roles import Rol


class Permiso(UniversalMixin, table=True):
    """Permiso"""

    VER: int = 1
    MODIFICAR: int = 2
    CREAR: int = 3
    BORRAR: int = 3
    ADMINISTRAR: int = 4

    # Nombre de la tabla
    __tablename__: str = "permisos"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    rol_id: uuid.UUID = Field(foreign_key="roles.id")
    rol: Rol = Relationship(back_populates="permisos")
    modulo_id: uuid.UUID = Field(foreign_key="modulos.id")
    modulo: Modulo = Relationship(back_populates="permisos")

    # Columnas
    nombre: str = Field(max_length=256, unique=True)
    nivel: int

    @property
    def rol_nombre(self):
        """Nombre del rol"""
        return self.rol.nombre

    @property
    def modulo_nombre(self):
        """Nombre del módulo"""
        return self.modulo.nombre

    def __repr__(self):
        """Representación"""
        return f"<Permiso {self.id}>"
