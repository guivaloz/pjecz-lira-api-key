"""
Distritos, routers
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.distritos import Distrito
from ..schemas.distritos import DistritoOut

distritos = APIRouter(prefix="/api/v5/distritos", tags=["distritos"])


@distritos.get("", response_model=CustomPage[DistritoOut])
async def get_distritos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de distritos"""
