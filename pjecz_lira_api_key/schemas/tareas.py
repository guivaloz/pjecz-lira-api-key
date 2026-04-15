"""
Tareas, esquemas
"""

from pydantic import BaseModel, ConfigDict


class TareaOut(BaseModel):
    """Esquema para entregar tareas"""

    usuario_email: str
    usuario_nombre: str
    archivo: str
    comando: str
    ha_terminado: bool
    mensaje: str
    url: str
    model_config = ConfigDict(from_attributes=True)


class OneTareaOut(BaseModel):
    """Esquema para entregar una tarea"""

    success: bool
    message: str
    data: TareaOut | None = None
