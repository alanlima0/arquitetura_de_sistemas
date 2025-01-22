import json
import os
from typing import List, Optional
from app.models.Usuario import Usuario
from app.dao.FilmeDao import FilmeDao


USUARIOS_FILE = os.path.join(os.path.dirname(__file__), '../data/usuarios.json')

class UsuarioDao:
    @staticmethod
    def _read_usuarios() -> List[Usuario]:
        try:
            with open(USUARIOS_FILE, 'r') as u:
                usuarios = json.load(u)
                return [Usuario(**usuario) for usuario in usuarios]
        except FileNotFoundError:
            return []

    @staticmethod
    def _write_usuarios(usuarios: List[Usuario]):
        with open(USUARIOS_FILE, 'w') as u:
            json.dump([usuario.dict() for usuario in usuarios], u, indent=4)

    @classmethod
    def _get_novo_id(cls) -> int:
        usuarios = cls._read_usuarios()
        return max((u.id for u in usuarios), default=0) + 1

    @classmethod
    def add_usuario(cls, usuario: Usuario):
        usuarios = cls._read_usuarios()
        if usuario.id is None:
            usuario.id = cls._get_novo_id()

        if any(existe_usuario.id == usuario.id for existe_usuario in usuarios):
            raise ValueError('Já existe um usuário com esse id.')

        usuarios.append(usuario)
        cls._write_usuarios(usuarios)

    @classmethod
    def get_all_usuarios(cls) -> List[Usuario]:
        return cls._read_usuarios()

    @classmethod
    def find_usuario_by_id(cls, usuario_id: int) -> Optional[Usuario]:
        usuarios = cls._read_usuarios()
        return next((usuario for usuario in usuarios if usuario.id == usuario_id), None)

    @classmethod
    def delete_usuario(cls, usuario_id: int) -> bool:
        usuarios = cls._read_usuarios()
        usuario = cls.find_usuario_by_id(usuario_id)
        if usuario:
            usuarios.remove(usuario)
            cls._write_usuarios(usuarios)
            return True
        return False

    @classmethod
    def update_usuario(cls, usuario_id: int, usuario_atualizado: Usuario) -> bool:
        usuarios = cls._read_usuarios()
        usuario = next((u for u in usuarios if u.id == usuario_id), None)

        if not usuario:
            return False

        usuario.nome = usuario_atualizado.nome
        usuario.email = usuario_atualizado.email
        usuario.senha = usuario_atualizado.senha
        usuario.favoritos = usuario_atualizado.favoritos

        cls._write_usuarios(usuarios)
        return True

    @classmethod
    def add_filme_a_usuario(cls, usuario_id: int, filme_id: int):
        # Lê os dados dos usuários
        usuarios = cls._read_usuarios()
        
        # Busca o usuário pelo ID
        usuario = cls.find_usuario_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        # Busca o filme pelo ID
        filme = FilmeDao.find_filme_by_id(filme_id)
        if not filme:
            raise ValueError("Filme não encontrado.")
        
        # Verifica se o filme já está nos favoritos
        if any(f["id"] == filme.id for f in usuario.favoritos):
            raise ValueError("Filme já está na lista de filmes do usuário.")
        
        # Adiciona o filme aos favoritos do usuário
        usuario.favoritos.append(filme.dict())

        # Atualiza os dados no arquivo JSON
        # Atualiza o usuário encontrado
        for i, u in enumerate(usuarios):
            if u.id == usuario_id:  # Acesse o atributo id diretamente
                usuarios[i] = usuario.dict()  # Use o método dict() para converter o objeto em dicionário
                break


        # Escreve as alterações no arquivo
        cls._write_usuarios(usuarios)


    @classmethod
    def remover_filme_de_usuario(cls, usuario_id: int, filme_id: int):
        usuarios = cls._read_usuarios()
        usuario = cls.find_usuario_by_id(usuario_id)
        filme = FilmeDao.find_filme_by_id(filme_id)

        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        if not filme:
            raise ValueError("Filme não encontrado.")

        if filme in usuario.favoritos:  # Removendo o filme dos favoritos
            usuario.favoritos.remove(filme)
            cls._write_usuarios(usuarios)
        else:
            raise ValueError("Filme não encontrado na lista de filmes do usuário.")
