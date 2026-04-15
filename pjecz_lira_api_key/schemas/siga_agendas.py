"""
SIGA Agendas, esquemas
"""

from datetime import date, time

from pydantic import BaseModel, ConfigDict


class SigaAgendaOut(BaseModel):
    """Esquema para entregar agendas"""

    juez: str
    secretario: str
    tipo_audiencia: str
    fecha: date
    hora_inicio: time
    hora_finalizacion: time
    saji_agenda_id: int
    model_config = ConfigDict(from_attributes=True)


class OneSigaAgendaOut(BaseModel):
    """Esquema para entregar una agenda"""

    success: bool
    message: str
    data: SigaAgendaOut | None = None
