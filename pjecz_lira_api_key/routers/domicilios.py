"""
Domicilios, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.domicilios import Domicilio
from ..schemas.domicilios import DomicilioOut

domicilios = APIRouter(prefix="/api/domicilios", tags=["siga"])


@domicilios.get("", response_model=CustomPage[DomicilioOut])
async def get_domicilios(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de domicilios"""
    if current_user.permissions.get("DOMICILIOS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(Domicilio).where(Domicilio.estatus == "A").order_by(Domicilio.clave)
    return paginate(database, query)
