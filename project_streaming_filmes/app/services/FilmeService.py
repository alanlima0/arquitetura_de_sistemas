from app.dao.FilmeDao import FilmeDao
from app.models.Filme import Filme

class FilmeService:
    @staticmethod
    def add_filme(filme: Filme):
        FilmeDao.add_filme(filme)

    @staticmethod
    def get_all_filmes():
        return FilmeDao.get_all_filmes()
    
    @staticmethod
    def delete_filme(filme_id: int):
        if not FilmeDao.delete_filme(filme_id):
            raise ValueError('Filme não encontrado.')
    
    @staticmethod
    def update_filme(filme_id: int, filme_atualizado:Filme):
        if not FilmeDao.update_filme(filme_id, filme_atualizado):
            raise ValueError('Filme não encontrado')
        
    @staticmethod
    def find_filme_by_id(filme_id: int):
        filme = FilmeDao.find_filme_by_id(filme_id)
        if not filme:
            raise ValueError('Filme não encontrado.')
        return filme