from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["PGCLIENTENCODING"] = "utf8"
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False, unique=True)
    autor = Column(String(100), nullable=False)
    disponible = Column(Boolean)
    
    def __repr__(self):
        return f"<Libro id={self.id}, titulo='{self.titulo}', autor='{self.autor}', disponible={self.disponible}>"


class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True)
    correo_usuario = Column(String)
    libro_id = Column(Integer, ForeignKey('libros.id'))
    fecha_inicio = Column(DateTime(), default=datetime.now())
    fecha_fin = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"<Reserva id={self.id}, libro_id={self.libro_id}, correo={self.correo_usuario}, fin={self.fecha_fin}>"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la tabla
Base.metadata.create_all(bind=engine)


