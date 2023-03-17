from fastapi import APIRouter

from src.router.v1.endpoints import senhas

api_router = APIRouter()
api_router.include_router(
    senhas.router, prefix="/Gerador_de_senhas", tags=["Gerador de senhas"]
)
