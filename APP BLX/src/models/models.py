from pydantic import BaseModel
from typing import Optional, List

class User():
    id: str
    nome: str
    telefone: str
    meus_produtos: List[Produtos]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]

class Produtos(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = 'Sem observações'