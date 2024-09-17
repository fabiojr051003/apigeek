from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, create_engine, SQLModel
from typing import List
from ..models import Produto
from ..schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
from ..services import ProdutoService

router = APIRouter()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/produtos/", response_model=ProdutoRead)
def create_produto(produto: ProdutoCreate, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    return service.create_produto(produto)

@router.get("/produtos/", response_model=List[ProdutoRead])
def list_produtos(nome: str = None, preco: float = None, categoria: str = None, franquia: str = None, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    return service.get_produtos(nome, preco, categoria, franquia)

@router.get("/produtos/{produto_id}", response_model=ProdutoRead)
def read_produto(produto_id: int, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    produto = service.get_produto(produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.put("/produtos/{produto_id}", response_model=ProdutoRead)
def update_produto(produto_id: int, produto_update: ProdutoUpdate, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    produto = service.update_produto(produto_id, produto_update)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.patch("/produtos/{produto_id}/estoque", response_model=ProdutoRead)
def atualizar_estoque(produto_id: int, quantidade: int, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    produto = service.atualizar_estoque(produto_id, quantidade)
    if produto is None:
        raise HTTPException(status_code=400, detail="Atualização de estoque inválida")
    return produto

@router.delete("/produtos/{produto_id}", response_model=dict)
def delete_produto(produto_id: int, session: Session = Depends(get_session)):
    service = ProdutoService(session)
    if not service.delete_produto(produto_id):
        raise HTTPException(status_code=404, detail="Produto não encontrado ou não pode ser excluído")
    return {"detail": "Produto excluído com sucesso"}
