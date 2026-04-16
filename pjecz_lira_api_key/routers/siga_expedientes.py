"""
SIGA Expedientes, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.siga_expedientes import SigaExpediente
from ..schemas.siga_expedientes import SigaExpedienteOut

siga_expedientes = APIRouter(prefix="/api/siga_expedientes", tags=["siga"])


@siga_expedientes.get("", response_model=CustomPage[SigaExpedienteOut])
async def get_siga_expedientes(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de siga_expedientes"""
    if current_user.permissions.get("SIGA EXPEDIENTES", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(SigaExpediente).where(SigaExpediente.estatus == "A")
    return paginate(database, query)
