"""
Authentications
"""

from sqlalchemy.orm import Session

from ..schemas.usuarios import UsuarioInDB
from .database import get_db


def get_user(
    usuario_id: int,
    database: Session = Depends(get_db),
) -> Optional[UsuarioInDB]:
    """Consultar un usuario por su id"""


def authenticate_user(
    api_key: str,
    database: Session,
) -> UsuarioInDB:
    """Autentificar un usuario por su api_key"""


async def get_current_active_user(
    api_key: str = Depends(X_API_KEY),
    database: Session = Depends(get_db),
) -> UsuarioInDB:
    """Obtener el usuario activo actual"""
