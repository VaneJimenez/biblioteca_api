from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import SessionLocal
import crud

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/libros")
def obtener_libros(db: Session = Depends(get_db)):
    return crud.listar_libros(db)

@app.post("/libros")
def crear_libro(titulo: str, autor: str, db: Session = Depends(get_db)):
    return crud.registrar_libro(db, titulo, autor)

