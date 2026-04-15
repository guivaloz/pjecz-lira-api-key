"""
Usuarios-Roles
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .roles import Rol
from .usuarios import Usuario


class UsuarioRol(UniversalMixin, table=True):
    """UsuarioRol"""

    # Nombre de la tabla
    __tablename__: str = "usuarios_roles"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    rol_id: uuid.UUID = Field(foreign_key="roles.id")
    rol: Rol = Relationship(back_populates="bitacoras")
    usuario_id: uuid.UUID = Field(foreign_key="usuarios.id")
    usuario: Usuario = Relationship(back_populates="bitacoras")

    # Columnas
    descripcion: str = Field(max_length=256)

    @property
    def rol_nombre(self):
        """Nombre del rol"""
        return self.rol.nombre

    @property
    def usuario_email(self):
        """Email del usuario"""
        return self.usuario.email

    @property
    def usuario_nombre(self):
        """Nombre del usuario"""
        return self.usuario.nombre

    def __repr__(self):
        """Representación"""
        return f"<UsuarioRol {self.id}>"
