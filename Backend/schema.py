from typing import List
from pydantic import BaseModel

#TENIS
class TenisBase(BaseModel):
    nome:str
    modelo:str
    cor:str
    tamanho:int
    margem:int
    estilo:str

class Tenis(TenisBase):
    id:int
    class Config:
        orm_mode=True

class PaginatedTenis(BaseModel):
    limit:int
    offset:int
    data: List[Tenis]

#FORNECEDOR
class FornecedorBase(BaseModel):
    nome:str
    email:str
    cnpj:int

class FornecedorCreate(FornecedorBase):
    telefone:int
    categoria:str

class Fornecedor(FornecedorBase):
    id:int
    class Config:
        orm_mode=True

class PaginatedFornecedor(BaseModel):
    limit:int
    offset:int
    data: List[Fornecedor]