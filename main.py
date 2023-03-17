from fastapi import FastAPI
from src.router.v1.api import api_router

app = FastAPI(title="API - Gerador de senhas")
app.include_router(api_router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8006, log_level="info", reload=True)
