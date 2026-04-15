"""
Database
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from ..config.settings import Settings, get_settings


def get_engine(settings: Annotated[Settings, Depends(get_settings)]) -> Engine:
    """Database engine"""

    # Create engine
    engine = create_engine(
        f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

    return engine


async def get_db(settings: Annotated[Settings, Depends(get_settings)]) -> Session:
    """Database session"""

    return Session(bind=get_engine(settings))
