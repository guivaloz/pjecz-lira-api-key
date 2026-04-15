"""
Autoridades, esquemas
"""

from pydantic import BaseModel, ConfigDict


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    distrito_clave: str
    distrito_nombre: str
    distrito_nombre_corto: str
    clave: str
    descripcion: str
    descripcion_corta: str
    es_jurisdiccional: bool
    es_activo: bool
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(BaseModel):
    """Esquema para entregar una autoridad"""

    success: bool
    message: str
    data: AutoridadOut | None = None
