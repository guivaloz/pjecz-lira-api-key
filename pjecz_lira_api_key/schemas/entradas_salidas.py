"""
Entradas-Salidas, esquemas
"""

from pydantic import BaseModel, ConfigDict


class EntradaSalidaOut(BaseModel):
    """Esquema para entregar entradas-salidas"""

    usuario_email: str
    usuario_nombre: str
    tipo: str
    direccion_ip: str
    model_config = ConfigDict(from_attributes=True)


class OneEntradaSalidaOut(BaseModel):
    """Esquema para entregar una entrada-salida"""

    success: bool
    message: str
    data: EntradaSalidaOut | None = None
