"""
Roles
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin


class Rol(UniversalMixin, table=True):
    """Rol"""

    # Nombre de la tabla
    __tablename__: str = "roles"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Columnas
    nombre: str = Field(max_length=256, unique=True)

    # Hijos
    permisos: list["Permiso"] = Relationship(back_populates="rol")
    usuarios_roles: list["UsuarioRol"] = Relationship(back_populates="rol")

    def __repr__(self):
        """Representación"""
        return f"<Rol {self.nombre}>"
