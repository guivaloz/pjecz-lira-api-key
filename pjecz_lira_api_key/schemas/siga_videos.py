"""
SIGA Videos, esquemas
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SigaVideoOut(BaseModel):
    """Esquema para entregar videos"""

    siga_expediente_expediente: str
    siga_sala_clave: str
    numero: int
    archivo: str
    descripcion: str
    inicio: datetime
    termino: datetime
    observaciones: str
    model_config = ConfigDict(from_attributes=True)


class OneSigaVideoOut(BaseModel):
    """Esquema para entregar un video"""

    success: bool
    message: str
    data: SigaVideoOut | None = None
