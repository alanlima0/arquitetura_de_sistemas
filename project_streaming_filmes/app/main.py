from fastapi import FastAPI
from app.controllers.FilmeController import router as filme_router
from app.controllers.UsuarioController import router as usuario_router
from fastapi.responses import HTMLResponse

# Criação da instância do FastAPI
app = FastAPI()

# Incluindo os controladores (routers)
app.include_router(filme_router)
app.include_router(usuario_router)

# Página inicial
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API de Filmes, Listas e Usuários</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #333;
                color: #fff;
                padding: 15px;
                text-align: center;
            }
            h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            .container {
                padding: 30px;
                text-align: center;
            }
            footer {
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 10px;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Bem-vindo à API de Filmes, Listas e Usuários 🎬</h1>
        </header>
        <div class="container">
            <h2>Esta API permite acessar, adicionar, atualizar e excluir filmes, listas e usuários!</h2>
            <p>Acesse os endpoints para interagir com filmes, listas e usuários cadastrados.</p><br>
            <a href="http://127.0.0.1:8000/filmes/">Listar Filmes</a>
        </div>
        <footer>
            <p>&copy; 2025 API de Filmes, Listas e Usuários. Todos os direitos reservados.</p>
        </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
