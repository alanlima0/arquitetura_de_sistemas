import json
import os
from typing import List, Optional
from app.models.Usuario import Usuario
from app.dao.FilmeDao import FilmeDao
from app.models.Filme import Filme


USUARIOS_FILE = os.path.join(os.path.dirname(__file__), '../data/usuarios.json')


class UsuarioDao:
    @staticmethod
    def _read_usuarios() -> List[Usuario]:
        try:
            with open(USUARIOS_FILE, 'r') as u:
                usuarios = json.load(u)
                # Converte cada usuário e seus favoritos para objetos
                return [Usuario(**{
                    **usuario,
                    "favoritos": [Filme(**f) for f in usuario.get("favoritos", [])]
                }) for usuario in usuarios]
        except FileNotFoundError:
            return []

    @staticmethod
    def _write_usuarios(usuarios: List[Usuario]):
        with open(USUARIOS_FILE, 'w') as u:
            # Serializa os usuários e seus favoritos
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
            usuarios = [u for u in usuarios if u.id != usuario_id]
            cls._write_usuarios(usuarios)
            return True
        return False

    @classmethod
    def update_usuario(cls, usuario_id: int, usuario_atualizado: Usuario) -> bool:
        if usuario_atualizado.id is None:
            usuario_atualizado.id = usuario_id  # Define o id se ele não foi passado

        usuarios = cls._read_usuarios()
        for i, u in enumerate(usuarios):
            if u.id == usuario_id:
                usuarios[i] = usuario_atualizado
                cls._write_usuarios(usuarios)
                return True
        return False


    @classmethod
    def add_filme_a_usuario(cls, usuario_id: int, filme_id: int):
        usuario = cls.find_usuario_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")

        filme = FilmeDao.find_filme_by_id(filme_id)
        if not filme:
            raise ValueError("Filme não encontrado.")

        if any(f.id == filme.id for f in usuario.favoritos):
            raise ValueError("Filme já está na lista de favoritos do usuário.")

        usuario.favoritos.append(filme)
        cls.update_usuario(usuario_id, usuario)


    @classmethod
    def remove_filme_de_usuario(cls, usuario_id: int, filme_id: int) -> bool:
        usuario = cls.find_usuario_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")

        filme = next((f for f in usuario.favoritos if f.id == filme_id), None)
        if not filme:
            raise ValueError("Filme não encontrado na lista de favoritos.")

        usuario.favoritos.remove(filme)
        cls.update_usuario(usuario_id, usuario)
        return True
