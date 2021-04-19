from sqlalchemy import Column, Interge, String, Boolean
from src.infra.sqlalchemy.config.databse import Base

class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Interge, primary_key=True, index=True)
    nome = Column(string)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)