"""
Usuarios, esquemas
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UsuarioOut(BaseModel):
    """Esquema para entregar usuarios"""

    distrito_clave: str
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    email: str
    nombres: str
    apellido_paterno: str
    apellido_materno: str
    puesto: str | None
    model_config = ConfigDict(from_attributes=True)


class OneUsuarioOut(BaseModel):
    """Esquema para entregar un usuario"""

    success: bool
    message: str
    data: UsuarioOut | None = None


class UsuarioInDB(UsuarioOut):
    """Usuario en base de datos"""

    username: str
    permissions: dict
    hashed_password: str
    disabled: bool
    api_key: str
    api_key_expiracion: datetime
