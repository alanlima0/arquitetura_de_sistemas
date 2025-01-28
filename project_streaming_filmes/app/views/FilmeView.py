from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.FilmeService import FilmeService

# Criar o router para views
router = APIRouter()

# Configurar templates (usando a configuração do main.py)
templates = Jinja2Templates(directory="app/templates/")

@router.get("/", response_class=HTMLResponse)
def listar_filmes(request: Request):
    """Exibe a lista de todos os filmes"""
    filmes = FilmeService.get_all_filmes()  # Busca os filmes no serviço
    return templates.TemplateResponse("filmes/index.html", {"request": request, "filmes": filmes})

@router.get("/tela_form", response_class=HTMLResponse)
def tela_form(request: Request):
    """
    Exibe a página com o formulário para adicionar um novo filme.
    """
    return templates.TemplateResponse("filmes/add_filme.html", {"request": request})
