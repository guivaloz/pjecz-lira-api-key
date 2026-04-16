"""
Módulos, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.modulos import Modulo
from ..models.permisos import Permiso
from ..schemas.modulos import ModuloOut

modulos = APIRouter(prefix="/api/modulos", tags=["usuarios"])


@modulos.get("", response_model=CustomPage[ModuloOut])
async def get_modulos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de modulos"""
    if current_user.permissions.get("MODULOS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(Modulo).where(Modulo.estatus == "A").order_by(Modulo.nombre)
    return paginate(database, query)
