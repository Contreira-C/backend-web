from sqlalchemy.orm import Session
from exceptions import TenisAlreadyExistError, TenisNotFoundError, FornecedorNotFoundError, FornecedorAlreadyExistError
import bcrypt, models, schema

#TENIS

#read
def get_tenis_by_id(db:Session, tenis_id:int):
    db_tenis =  db.query(models.Tenis).get(tenis_id)
    if db_tenis is None:
        raise TenisNotFoundError
    return db_tenis

def get_all_tenis(db:Session, offset:int, limit:int):
    return db.query(models.Tenis).offset(offset).limit(limit).all()

def get_tenis_by_model(db:Session, tenis_model:str):
    return db.query(models.Tenis).filter(models.Tenis.modelo == tenis_model).first()

#create
def create_tenis(db:Session, tenis:schema.TenisBase):
    db_tenis = get_tenis_by_model(db,tenis.modelo)
    if db_tenis is not None:
        raise TenisAlreadyExistError
    db_tenis = models.Tenis(**tenis.dict())
    db.add(db_tenis)
    db.commit()
    db.refresh(db_tenis)
    return db_tenis

#update
def update_tenis(db: Session, tenis_id:int, tenis:schema.Tenis):
    db_tenis = get_tenis_by_id(db,tenis_id)
    db_tenis.nome = tenis.nome
    db_tenis.modelo = tenis.modelo
    db_tenis.cor = tenis.cor
    db_tenis.tamanho = tenis.tamanho
    db_tenis.margem = tenis.margem
    db_tenis.estilo = tenis.estilo
    db.commit()
    db.refresh(db_tenis)
    return db_tenis

#delete
def delete_tenis_by_id(db:Session,tenis_id:int):
    db_tenis = get_tenis_by_id(db,tenis_id)
    db.delete(db_tenis)
    db.commit()
    return


#FORNECEDORES

#read
def get_fornecedor_by_id(db:Session, fornecedor_id:int):
    db_fornecedor =  db.query(models.Fornecedor).get(fornecedor_id)
    if db_fornecedor is None:
        raise FornecedorNotFoundError
    return db_fornecedor

def get_all_fornecedor(db:Session, offset:int, limit:int):
    return db.query(models.Fornecedor).offset(offset).limit(limit).all()

def get_fornecedor_by_cnpj(db:Session, fornecedor_cnpj:int):
    return db.query(models.Fornecedor).filter(models.Fornecedor.cnpj == fornecedor_cnpj).first()

#create
def create_fornecedor(db:Session, fornecedor:schema.FornecedorCreate):
    db_fornecedor = get_fornecedor_by_cnpj(db,fornecedor.cnpj)
    if db_fornecedor is not None:
        raise FornecedorAlreadyExistError
    db_fornecedor = models.Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

#update
def update_fornecedor(db: Session, fornecedor_id:int, fornecedor:schema.FornecedorCreate):
    db_fornecedor = get_fornecedor_by_id(db,fornecedor_id)
    db_fornecedor.nome = fornecedor.nome
    db_fornecedor.email = fornecedor.email
    db_fornecedor.telefone = fornecedor.telefone
    db_fornecedor.cnpj = fornecedor.cnpj
    db_fornecedor.categoria = fornecedor.categoria
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

#delete
def delete_fornecedor_by_id(db:Session,fornecedor_id:int):
    db_fornecedor = get_fornecedor_by_id(db,fornecedor_id)
    db.delete(db_fornecedor)
    db.commit()
    return