from llm_handler import procesar_mensaje
from crud import (
    registrar_libro, reservar_libro, renovar_reserva,
    eliminar_libro, eliminar_reserva, listar_libros
)
from sqlalchemy.orm import Session

def interpretar_comando(texto: str, db: Session):
    mensaje = procesar_mensaje(texto).lower()

    if "reservar" in mensaje:
        # Extrae nombre del libro y correo desde el texto con lógica más avanzada o usando otro LLM
        return reservar_libro(db, correo_usuario="user@example.com", libro_id=1)  # placeholder

    elif "listar" in mensaje or "libros disponibles" in mensaje:
        return listar_libros(db)

    elif "eliminar reserva" in mensaje:
        return eliminar_reserva(db, reserva_id=1)

    elif "renovar" in mensaje:
        return renovar_reserva(db, reserva_id=1)

    elif "eliminar libro" in mensaje:
        return eliminar_libro(db, libro_id=1)

    elif "registrar libro" in mensaje:
        return registrar_libro(db, titulo="Título de prueba", autor="Autor X")

    return "No se pudo interpretar tu solicitud."
