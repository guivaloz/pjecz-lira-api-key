"""
SIGA Salas, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.permisos import Permiso
from ..models.siga_salas import SigaSala
from ..schemas.siga_salas import SigaSalaOut

siga_salas = APIRouter(prefix="/api/siga_salas", tags=["siga"])


@siga_salas.get("", response_model=CustomPage[SigaSalaOut])
async def get_siga_salas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de siga_salas"""
    if current_user.permissions.get("SIGA SALAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(SigaSala).where(SigaSala.estatus == "A")
    return paginate(database, query)
