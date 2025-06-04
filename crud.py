from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import Libro, Reserva

# Registrar un nuevo libro
def registrar_libro(db: Session, titulo: str, autor: str):
    nuevo_libro = Libro(titulo=titulo, autor=autor, disponible=True)
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

# Listar todos los libros
def listar_libros(db: Session):
    return db.query(Libro).all()

# Eliminar un libro por ID
def eliminar_libro(db: Session, libro_id: int):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
        return True
    return False

# Reservar un libro (y cambiar disponibilidad)
def reservar_libro(db: Session, correo_usuario: str, libro_id: int, dias_reserva: int = 7):
    libro = db.query(Libro).filter(Libro.id == libro_id, Libro.disponible == True).first()
    if not libro:
        return None  # libro no disponible o no existe

    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=dias_reserva)  # reserva por 7 días
    reserva = Reserva(
        correo_usuario=correo_usuario,
        libro_id=libro_id,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin
    )

    # Cambiar estado de disponibilidad
    libro.disponible =False

    db.add(reserva)
    db.commit()
    db.refresh(reserva)
    return reserva

# Renovar una reserva (por 7 días más)
def renovar_reserva(db: Session, reserva_id: int):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva:
        reserva.fecha_fin += timedelta(days=7)
        db.commit()
        db.refresh(reserva)
        return reserva
    return None

# Eliminar una reserva (y volver a poner el libro como disponible)
def eliminar_reserva(db: Session, reserva_id: int):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva:
        libro = db.query(Libro).filter(Libro.id == reserva.libro_id).first()
        if libro:
            libro.disponible = True
        db.delete(reserva)
        db.commit()
        return True
    return False
