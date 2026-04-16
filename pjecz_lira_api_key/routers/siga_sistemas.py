"""
SIGA Sistemas, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.siga_sistemas import SigaSistema
from ..schemas.siga_sistemas import SigaSistemaOut

siga_sistemas = APIRouter(prefix="/api/siga_sistemas", tags=["siga"])


@siga_sistemas.get("", response_model=CustomPage[SigaSistemaOut])
async def get_siga_sistemas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de siga_sistemas"""
    if current_user.permissions.get("SIGA SALAS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(SigaSistema).where(SigaSistema.estatus == "A")
    return paginate(database, query)
