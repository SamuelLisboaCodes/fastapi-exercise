from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Modelo de validação (Pydantic)
class Usuario(BaseModel):
    nome: str
    email: EmailStr

@app.get("/")
def raiz():
    return {"status": "API funcionando"}

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    # Se chegar aqui, o Pydantic já validou o email
    return {
        "mensagem": f"Usuário {usuario.nome} criado com sucesso",
        "email_recebido": usuario.email
    }
