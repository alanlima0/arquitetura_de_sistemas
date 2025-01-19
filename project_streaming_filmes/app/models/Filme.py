from pydantic import BaseModel, Field
from typing import Optional

class Filme(BaseModel):
    id: Optional[int] = Field(default=None)
    titulo: str
    genero: str
    descricao: str
    ano: int
    avaliacao: float

