# Movie API - FastAPI Project 🎬🚀

Este projeto implementa uma aplicação simples utilizando **FastAPI** para gerenciar uma coleção de filmes. A API permite que os usuários obtenham uma lista de filmes e adicionem novos filmes à coleção. A aplicação foi desenvolvida utilizando **FastAPI** como framework para a API, **Uvicorn** como servidor ASGI, e **Conda** para gerenciamento de dependências. **Postman** foi utilizado para testar e documentar os endpoints da API.

## Tecnologias Utilizadas 🛠️

- **FastAPI**: Framework moderno para a construção de APIs com Python 3.7+, baseado em dicas de tipo do Python.
- **Uvicorn**: Servidor ASGI utilizado para executar a aplicação FastAPI.
- **Conda**: Ferramenta de gerenciamento de ambientes para facilitar a instalação de dependências.
- **Postman**: Ferramenta para testar e documentar as requisições e respostas da API.

## Funcionalidades ✨

- **GET /filmes/**: Retorna uma lista de filmes armazenados.
- **POST /filmes/**: Permite adicionar um novo filme à coleção.

## Como Configurar o Projeto 🏗️

Para configurar e executar o projeto localmente, siga as instruções abaixo:

### 1. Clonar o repositório 💻

Clone o repositório do projeto para sua máquina local:

```bash
git clone <URL_do_repositório>
cd <diretório_do_repositório>

2. Criar um ambiente Conda 🧑‍💻

Crie um ambiente Conda para o projeto para garantir que as dependências sejam instaladas de maneira isolada:

conda create --name fastapi-movie-api python=3.8
conda activate fastapi-movie-api

3. Instalar as dependências 📦

Instale as dependências necessárias para o projeto com o pip:

pip install fastapi uvicorn

4. Executar a aplicação 🚀

Inicie a aplicação FastAPI usando o Uvicorn:

uvicorn main:app --reload

A aplicação estará disponível em http://127.0.0.1:8000.
