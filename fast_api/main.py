from typing import List
from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Usando um dicionário para armazenar filmes com um id como chave
filmes = {}


@app.get("/filmes/")
async def list_filmes():
    """
    Retrieve the list of movies.
    """
    return {
        "status": "success",
        "message": "Movies retrieved successfully.",
        "data": filmes
    }

@app.post("/filmes/")
async def create_filme(
    title: str = Form(...),
    director: str = Form(...),
    genre: str = Form(...),
    year: str = Form(...),  
    description: str = Form(...)
):
    """
    Add a new movie to the list.
    """
    new_id = len(filmes) + 1 
    filme = {
        "id": new_id,
        "title": title,
        "director": director,
        "genre": genre,
        "year": year,
        "description": description
    }
    filmes[new_id] = filme  # Adicionar o filme ao dicionário com o novo ID
    return {
        "status": "success",
        "message": "Movie added successfully.",
        "data": filme
    }
