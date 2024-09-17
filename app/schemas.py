from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade_estoque: int
    categoria: str
    franquia: str

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoRead(ProdutoBase):
    id: int

class ProdutoUpdate(BaseModel):
    nome: str = None
    descricao: str = None
    preco: float = None
    quantidade_estoque: int = None
    categoria: str = None
    franquia: str = None
