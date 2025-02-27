from app.dao.UsuarioDao import UsuarioDao
from app.models.Usuario import Usuario
from app.dao.FilmeDao import FilmeDao

class UsuarioService:
    @staticmethod
    def add_usuario(usuario: Usuario):
        UsuarioDao.add_usuario(usuario)

    @staticmethod
    def get_all_usuarios():
        return UsuarioDao.get_all_usuarios()
    
    @staticmethod
    def delete_usuario(usuario_id: int):
        if not UsuarioDao.delete_usuario(usuario_id):
            raise ValueError('Usuário não encontrado.')
    
    @staticmethod
    def update_usuario(usuario_id: int, usuario_atualizado: Usuario):
        if not UsuarioDao.update_usuario(usuario_id, usuario_atualizado):
            raise ValueError('Usuário não encontrado.')
        
    @staticmethod
    def find_usuario_by_id(usuario_id: int) -> Usuario:
        usuario = UsuarioDao.find_usuario_by_id(usuario_id)
        if not usuario:
            raise ValueError('Usuário não encontrado.')
        return usuario
    
    @staticmethod
    def add_filme_a_usuario(usuario_id: int, filme_id: int):
        usuario = UsuarioDao.find_usuario_by_id(usuario_id)
        filme = FilmeDao.find_filme_by_id(filme_id)

        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        if not filme:
            raise ValueError("Filme não encontrado.")
        
        UsuarioDao.add_filme_a_usuario(usuario_id, filme_id)

    @staticmethod
    def remove_filme_de_usuario(usuario_id: int, filme_id: int):
        usuario = UsuarioDao.find_usuario_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")

        filme = next((f for f in usuario.favoritos if f.id == filme_id), None)
        if not filme:
            raise ValueError("Filme não encontrado na lista de favoritos.")

        UsuarioDao.remove_filme_de_usuario(usuario_id, filme_id)
