"""
Tareas, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.permisos import Permiso
from ..models.tareas import Tarea
from ..schemas.tareas import TareaOut

tareas = APIRouter(prefix="/api/tareas", tags=["usuarios"])


@tareas.get("", response_model=CustomPage[TareaOut])
async def get_tareas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de tareas"""
    if current_user.permissions.get("TAREAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(Tarea).where(Tarea.estatus == "A")
    return paginate(database, query)
