"""
SIGA Expedientes, esquemas
"""

from pydantic import BaseModel, ConfigDict


class SigaExpedienteOut(BaseModel):
    """Esquema para entregar expedientes"""

    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    expediente: str
    observaciones: str
    model_config = ConfigDict(from_attributes=True)


class OneSigaExpedienteOut(BaseModel):
    """Esquema para entregar un expediente"""

    success: bool
    message: str
    data: SigaExpedienteOut | None = None
