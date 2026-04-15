"""
Bitacoras, esquemas
"""

from pydantic import BaseModel, ConfigDict


class BitacoraOut(BaseModel):
    """Esquema para entregar bitacoras"""

    usuario_email: str
    usuario_nombre: str
    modulo_nombre: str
    descripcion: str
    url: str
    model_config = ConfigDict(from_attributes=True)


class OneBitacoraOut(BaseModel):
    """Esquema para entregar una bitacora"""

    success: bool
    message: str
    data: BitacoraOut | None = None
