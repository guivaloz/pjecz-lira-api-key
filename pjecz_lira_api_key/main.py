"""
PJECZ Lira API Key
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from .config.settings import get_settings
from .routers.autoridades import autoridades
from .routers.distritos import distritos

# FastAPI
app = FastAPI(
    title="PJECZ Casiopea API Key",
    description="API con autentificación del sistema de citas.",
    docs_url="/docs",
    redoc_url=None,
)

# CORSMiddleware
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS.split(","),
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Rutas
app.include_router(distritos)
app.include_router(autoridades)


# Paginación
add_pagination(app)


# Mensaje de Bienvenida
@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "API para el respaldo y la transcripción de videos."}
