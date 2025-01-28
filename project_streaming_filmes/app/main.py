from app.controllers.FilmeController import router as filme_router
from app.controllers.UsuarioController import router as usuario_router
from app.views.FilmeView import router as filme_view_router  # Corrigido

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Configurar o diretório de templates
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

# Criação da instância do FastAPI
app = FastAPI()

# Incluindo os controladores (routers)
app.include_router(filme_router, tags=["API - Filmes"])
app.include_router(usuario_router, tags=["API - Usuários"])

# Incluindo as views
app.include_router(filme_view_router, tags=["Views - Filmes"])
