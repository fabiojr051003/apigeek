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
