"""
Entradas-Salidas, modelos
"""

import uuid

from sqlmodel import Field, Relationship

from ..dependencies.universal_mixin import UniversalMixin
from .usuarios import Usuario


class EntradaSalida(UniversalMixin, table=True):
    """EntradaSalida"""

    TIPOS = {
        "INGRESO": "Ingresó",
        "SALIO": "Salió",
    }

    # Nombre de la tabla
    __tablename__: str = "entradas_salidas"

    # Clave primaria
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Claves foráneas
    usuario_id: uuid.UUID = Field(foreign_key="usuarios.id")
    usuario: Usuario = Relationship(back_populates="entradas_salidas")

    # Columnas
    tipo: str = Field(max_length=16, index=True)  # TODO: Enum
    direccion_ip: str = Field(max_length=64)

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
        return f"<EntradaSalida {self.id}>"
