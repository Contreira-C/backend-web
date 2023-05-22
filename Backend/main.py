from typing import Union

import crud
import models
import schema
from database import engine, get_db
from exceptions import FornecedorException, TenisException
from fastapi import Body, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#TENIS

#tenis
@app.get("/api/tenis/{tenis_id}", response_model=schema.Tenis)
def get_tenis_by_id(tenis_id:int, db:Session = Depends(get_db)):
    try:
        return crud.get_tenis_by_id(db, tenis_id)
    except TenisException as cie:
        raise HTTPException(**cie.__dict__)
    
#read
@app.get("/api/tenis", response_model=schema.PaginatedTenis)
def get_all_tenis(db: Session = Depends(get_db), offset:int = 0, limit:int = 10):
    db_tenis = crud.get_all_tenis(db, offset, limit)
    response = {"limit":limit, "offset":offset, "data":db_tenis}
    return response

#create
@app.post("/api/tenis",response_model=schema.TenisBase)
def create_tenis(tenis:schema.Tenis,db: Session = Depends(get_db)):
    try:
        return crud.create_tenis(db,tenis)
    except TenisException as cie:
        raise HTTPException(**cie.__dict__)
    
#update
@app.put("/api/tenis/{tenis_id}",response_model=schema.Tenis)
def update_tenis(tenis_id:int, tenis:schema.Tenis,db:Session = Depends(get_db)):
    try:
        return crud.update_tenis(db, tenis_id, tenis)
    except TenisException as cie:
        raise HTTPException(**cie.__dict__)
    
#delete
@app.delete("/api/tenis/{tenis_id}")
def delete_tenis_by_id(tenis_id:int,db:Session = Depends(get_db)):
    try:
        return crud.delete_tenis_by_id(db, tenis_id)
    except TenisException as cie:
        raise HTTPException(**cie.__dict__)
    

#FORNECEDOR
@app.get("/api/fornecedor/{fornecedor_id}", response_model=schema.Fornecedor)
def get_fornecedor_by_id(fornecedor_id:int, db:Session = Depends(get_db)):
    try:
        return crud.get_fornecedor_by_id(db, fornecedor_id)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    
#read
@app.get("/api/fornecedor", response_model=schema.PaginatedFornecedor)
def get_all_fornecedor(db: Session = Depends(get_db), offset:int = 0, limit:int = 10):
    db_fornecedor = crud.get_all_fornecedor(db, offset, limit)
    response = {"limit":limit, "offset":offset, "data":db_fornecedor}
    return response

#create
@app.post("/api/fornecedor",response_model=schema.Fornecedor)
def create_fornecedor(fornecedor:schema.FornecedorCreate,db: Session = Depends(get_db)):
    try:
        return crud.create_fornecedor(db,fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    
#update
@app.put("/api/fornecedor/{fornecedor_id}",response_model=schema.Fornecedor)
def update_fornecedor(fornecedor_id:int, fornecedor:schema.FornecedorCreate,db:Session = Depends(get_db)):
    try:
        return crud.update_fornecedor(db, fornecedor_id, fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    
#delete
@app.delete("/api/fornecedor/{fornecedor_id}")
def delete_fornecedor_by_id(fornecedor_id:int,db:Session = Depends(get_db)):
    try:
        return crud.delete_fornecedor_by_id(db, fornecedor_id)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    