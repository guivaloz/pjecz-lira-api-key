"""
PJECZ Lira API Key
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from .config.settings import get_settings
from .routers.autoridades import autoridades
from .routers.bitacoras import bitacoras
from .routers.distritos import distritos
from .routers.domicilios import domicilios
from .routers.entradas_salidas import entradas_salidas
from .routers.modulos import modulos
from .routers.permisos import permisos
from .routers.roles import roles
from .routers.siga_agendas import siga_agendas
from .routers.siga_expedientes import siga_expedientes
from .routers.siga_salas import siga_salas
from .routers.siga_sistemas import siga_sistemas
from .routers.siga_videos import siga_videos
from .routers.tareas import tareas
from .routers.usuarios import usuarios
from .routers.usuarios_roles import usuarios_roles

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
app.include_router(autoridades)
app.include_router(bitacoras)
app.include_router(distritos)
app.include_router(domicilios)
app.include_router(entradas_salidas)
app.include_router(modulos)
app.include_router(permisos)
app.include_router(roles)
app.include_router(siga_agendas)
app.include_router(siga_expedientes)
app.include_router(siga_salas)
app.include_router(siga_sistemas)
app.include_router(siga_videos)
app.include_router(tareas)
app.include_router(usuarios)
app.include_router(usuarios_roles)

# Paginación
add_pagination(app)


# Mensaje de Bienvenida
@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "API para el respaldo y la transcripción de videos."}
