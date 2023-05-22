from sqlalchemy import Column,Integer,String
from database import Base 

class Tenis(Base):
    __tablename__ = 'tenis'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    modelo = Column(String(150))
    cor = Column(String(150))
    tamanho = Column(Integer)
    margem = Column(Integer)
    estilo = Column(String(150))

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    email = Column(String(150))
    telefone = Column(Integer)
    cnpj = Column(Integer)
    categoria = Column(String(150))
    