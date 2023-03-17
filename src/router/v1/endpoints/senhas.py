from fastapi import APIRouter
from fastapi import status

from src.service.services_senha import SenhaServiceFapi

router = APIRouter()


# Post senha (Funcionando)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_password(qtd_caractere: int, apelido_senha: str):
    tamanho_senha = qtd_caractere
    apelido = apelido_senha
    senha_1 = SenhaServiceFapi.insert_one_senha(tamanho_senha, apelido)
    return senha_1


# Get senha
@router.get("/{unique_id}", status_code=status.HTTP_200_OK)
async def get_password(unique_id):
    identificacao = unique_id
    get_dados = SenhaServiceFapi.get_one(identificacao)
    return get_dados


# Get todas as senhas
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_passwords():
    return_obj = SenhaServiceFapi.get_all()
    return return_obj


# # Put senha
# @router.put("/", status_code=status.HTTP_202_ACCEPTED)
# async def put_password():
#     pass


# Delete senha (Funcionando)
@router.delete("/{unique_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_password(uinique_id):
    id = uinique_id
    del_dados = SenhaServiceFapi.delete_trainer(id)
    return del_dados
