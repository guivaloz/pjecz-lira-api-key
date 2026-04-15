"""
Domicilios, esquemas
"""

from pydantic import BaseModel, ConfigDict


class DomicilioOut(BaseModel):
    """Esquema para entregar domicilios"""

    clave: str
    edificio: str
    domicilio_completo: str
    model_config = ConfigDict(from_attributes=True)


class OneDomicilioOut(BaseModel):
    """Esquema para entregar un domicilio"""

    success: bool
    message: str
    data: DomicilioOut | None = None
