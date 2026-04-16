"""
SIGA Videos, rutas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlmodel import Session, select

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.permisos import Permiso
from ..models.siga_videos import SigaVideo
from ..schemas.siga_videos import SigaVideoOut

siga_videos = APIRouter(prefix="/api/siga_videos", tags=["siga"])


@siga_videos.get("", response_model=CustomPage[SigaVideoOut])
async def get_siga_videos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de siga_videos"""
    if current_user.permissions.get("SIGA VIDEOS", 0) < 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    query = select(SigaVideo).where(SigaVideo.estatus == "A")
    return paginate(database, query)
