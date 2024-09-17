import os
import uvicorn
from fastapi import FastAPI
from app.routers import products
from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

app = FastAPI()

# Criação das tabelas
SQLModel.metadata.create_all(engine)

# Inclusão das rotas
app.include_router(products.router, prefix="/api", tags=["produtos"])
@app.get("/")
def read_root():
    return {"Api Geek"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Usa a variável de ambiente PORT ou 8000 por padrão
    uvicorn.run(app, host="0.0.0.0", port=port)