"""
Usuarios, modelos
"""

import uuid
from datetime import datetime

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .autoridades import Autoridad
from .permisos import Permiso


class Usuario(UniversalMixin, table=True):
    """Usuario"""

    # Nombre de la tabla
    __tablename__: str = "usuarios"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Clave foránea
    autoridad_id: uuid.UUID = Field(foreign_key="autoridades.id")
    autoridad: Autoridad = Relationship(back_populates="usuarios")

    # Columnas
    email: str = Field(max_length=256)
    nombres: str = Field(max_length=256)
    apellido_paterno: str = Field(max_length=256)
    apellido_materno: str = Field(max_length=256)
    puesto: str | None = Field(max_length=256)
    api_key: str | None = Field(max_length=128)
    api_key_expiracion: datetime | None
    contrasena: str | None = Field(max_length=256)

    # Hijos
    bitacoras: list["Bitacora"] = Relationship(back_populates="usuario")
    entradas_salidas: list["EntradaSalida"] = Relationship(back_populates="usuario")
    tareas: list["Tarea"] = Relationship(back_populates="usuario")
    usuarios_roles: list["UsuarioRol"] = Relationship(back_populates="usuario")

    @property
    def nombre(self):
        """Junta nombres, apellido_paterno y apellido materno"""
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno

    @property
    def permisos(self):
        """Entrega un diccionario con todos los permisos"""
        permisos_dict: dict[str, int] = {}
        for usuario_rol in self.usuarios_roles:
            if usuario_rol.estatus == "A":
                for permiso in usuario_rol.rol.permisos:
                    if permiso.estatus == "A":
                        etiqueta = permiso.modulo.nombre
                        if etiqueta not in permisos_dict or permiso.nivel > permisos_dict[etiqueta]:
                            permisos_dict[etiqueta] = permiso.nivel
        return permisos_dict

    def can(self, modulo_nombre: str, permission: int):
        """¿Tiene permiso?"""
        if modulo_nombre in self.permisos:
            return self.permisos[modulo_nombre] >= permission
        return False

    def can_view(self, modulo_nombre: str):
        """¿Tiene permiso para ver?"""
        return self.can(modulo_nombre, 1)

    def can_edit(self, modulo_nombre: str):
        """¿Tiene permiso para editar?"""
        return self.can(modulo_nombre, Permiso.MODIFICAR)

    def can_insert(self, modulo_nombre: str):
        """¿Tiene permiso para agregar?"""
        return self.can(modulo_nombre, Permiso.CREAR)

    def can_admin(self, modulo_nombre: str):
        """¿Tiene permiso para administrar?"""
        return self.can(modulo_nombre, Permiso.ADMINISTRAR)

    @property
    def distrito_clave(self):
        """Distrito clave"""
        return self.autoridad.distrito.clave

    @property
    def distrito_nombre(self):
        """Distrito nombre"""
        return self.autoridad.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Distrito nombre corto"""
        return self.autoridad.distrito.nombre_corto

    @property
    def autoridad_clave(self):
        """Autoridad clave"""
        return self.autoridad.clave

    @property
    def autoridad_descripcion(self):
        """Autoridad descripción"""
        return self.autoridad.descripcion

    @property
    def autoridad_descripcion_corta(self):
        """Autoridad descripción corta"""
        return self.autoridad.descripcion_corta

    def __repr__(self):
        """Representación"""
        return f"<Usuario {self.email}>"
