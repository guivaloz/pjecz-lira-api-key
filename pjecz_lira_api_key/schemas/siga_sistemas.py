"""
SIGA Sistemas, esquemas
"""

from pydantic import BaseModel, ConfigDict


class SigaSistemaOut(BaseModel):
    """Esquema para entregar sistemas"""

    clave: str
    descripcion: str
    model_config = ConfigDict(from_attributes=True)


class OneSigaSistemaOut(BaseModel):
    """Esquema para entregar un sistema"""

    success: bool
    message: str
    data: SigaSistemaOut | None = None
