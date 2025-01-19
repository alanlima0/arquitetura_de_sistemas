from fastapi import FastAPI
from app.controllers.FilmeController import router
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Movie Streaming API</title>
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
            <h1>Bem-vindo à API de Streaming de Filmes 🎬</h1>
        </header>
        <div class="container">
            <h2>Esta API permite acessar, adicionar, atualizar e excluir filmes na sua coleção!</h2>
            <p>Acesse os endpoints para interagir com os filmes cadastrados na plataforma.</p>
        </div>
        <footer>
            <p>&copy; 2025 Streaming de Filmes API. Todos os direitos reservados.</p>
        </footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)