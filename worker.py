from models import SessionLocal
from graph_client import obtener_correos, enviar_correo
from email_handler import interpretar_comando

def run():
    db = SessionLocal()
    mensajes = obtener_correos()

    for mensaje in mensajes.get("value", []):
        asunto = mensaje["subject"]
        cuerpo = mensaje["body"]["content"]
        remitente = mensaje["from"]["emailAddress"]["address"]

        respuesta = interpretar_comando(cuerpo, db)
        enviar_correo(remitente, "Respuesta a tu solicitud", str(respuesta))

    db.close()

if __name__ == "__main__":
    run()
