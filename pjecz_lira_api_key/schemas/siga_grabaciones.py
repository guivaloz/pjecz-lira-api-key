"""
SIGA Grabaciones, esquemas
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SigaGrabacionOut(BaseModel):
    """Esquema para entregar grabaciones"""

    siga_expediente_expediente: str
    siga_sala_clave: str
    numero: int
    archivo: str
    descripcion: str
    inicio: datetime
    termino: datetime
    observaciones: str
    model_config = ConfigDict(from_attributes=True)


class DetailSigaGrabacionOut(SigaGrabacionOut):
    """Detalle completo de una grabacion"""

    url: str | None
    tamanio_bytes: int | None
    duracion_segundos: int | None
    transcripcion_json: str | None
    transcripcion_txt: str | None


class OneSigaGrabacionOut(BaseModel):
    """Esquema para entregar una grabacion"""

    success: bool
    message: str
    data: DetailSigaGrabacionOut | None = None
