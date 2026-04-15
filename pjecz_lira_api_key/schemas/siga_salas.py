"""
SIGA Salas, esquemas
"""

from pydantic import BaseModel, ConfigDict


class SigaSalaOut(BaseModel):
    """Esquema para entregar salas"""

    domicilio_clave: str
    domicilio_edificio: str
    clave: str
    descripcion: str
    direccion_ip: str
    direccion_nvr: str
    model_config = ConfigDict(from_attributes=True)


class OneSigaSalaOut(BaseModel):
    """Esquema para entregar una sala"""

    success: bool
    message: str
    data: SigaSalaOut | None = None
