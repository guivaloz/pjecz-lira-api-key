"""
SIGA Agendas, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.siga_agendas import SigaAgenda
from ..schemas.siga_agendas import SigaAgendaOut

siga_agendas = APIRouter(prefix="/api/siga_agendas", tags=["siga"])


@siga_agendas.get("", response_model=CustomPage[SigaAgendaOut])
async def get_siga_agendas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de siga_agendas"""
    if current_user.permissions.get("SIGA AGENDAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(SigaAgenda).where(SigaAgenda.estatus == "A")
    return paginate(database, query)
