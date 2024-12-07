import json
from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Nome do arquivo JSON
FILENAME = "filmes.json"

# Função para carregar os filmes do JSON
def load_filmes():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para salvar filmes no JSON
def save_filmes(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

#obter dados do arquivo
filmes = load_filmes()

@app.get("/filmes/")
async def list_filmes():
    """
    Retrieve the list of movies.
    """
    return {
        "status": "success",
        "message": "Movies retrieved successfully.",
        "data": list(filmes.values())
    }

@app.get("/filmes/{filme_id}")
async def get_filme_by_id(filme_id: int):
    """
    Retrieve a movie by its ID.
    """
    filme = filmes.get(str(filme_id))  
    if not filme:
        raise HTTPException(status_code=404, detail="Movie not found.")
    return {
        "status": "success",
        "message": "Movie retrieved successfully.",
        "data": filme
    }

@app.post("/filmes/")
async def create_filme(
    title: str = Form(...),
    director: str = Form(...),
    genre: str = Form(...),
    year: int = Form(...),
    description: str = Form(...)
):
    """
    Add a new movie to the list.
    """
    new_id = str(len(filmes) + 1) 
    filme = {
        "id": new_id,
        "title": title,
        "director": director,
        "genre": genre,
        "year": year,
        "description": description
    }
    filmes[new_id] = filme
    save_filmes(filmes)
    return {
        "status": "success",
        "message": "Movie added successfully.",
        "data": filme
    }

@app.put("/filmes/{filme_id}")
async def update_filme(
    filme_id: int,
    title: str = Form(...),
    director: str = Form(...),
    genre: str = Form(...),
    year: int = Form(...),
    description: str = Form(...)
):
    """
    Update a movie's details by its ID.
    """
    filme_id = str(filme_id)  
    if filme_id in filmes:
        filmes[filme_id].update({
            "title": title,
            "director": director,
            "genre": genre,
            "year": year,
            "description": description
        })
        save_filmes(filmes)
        return {
            "status": "success",
            "message": "Movie updated successfully.",
            "data": filmes[filme_id]
        }
    raise HTTPException(status_code=404, detail="Movie not found.")

@app.delete("/filmes/{filme_id}")
async def delete_filme(filme_id: int):
    """
    Delete a movie by its ID.
    """
    filme_id = str(filme_id) 
    if filme_id in filmes:
        deleted_filme = filmes.pop(filme_id)
        save_filmes(filmes)
        return {
            "status": "success",
            "message": "Movie deleted successfully.",
            "data": deleted_filme
        }
    raise HTTPException(status_code=404, detail="Movie not found.")
