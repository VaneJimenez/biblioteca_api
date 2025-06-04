from msal import ConfidentialClientApplication
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_ID = os.getenv("USER_ID")  # ej. correo de biblioteca
SCOPE = ["https://graph.microsoft.com/.default"]

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

app = ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)

def obtener_token():
    result = app.acquire_token_silent(SCOPE, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=SCOPE)
    return result['access_token']

def obtener_correos():
    token = obtener_token()
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://graph.microsoft.com/v1.0/users/{USER_ID}/mailFolders/Inbox/messages?$top=10'
    res = requests.get(url, headers=headers)
    return res.json()

def enviar_correo(destinatario, asunto, contenido):
    token = obtener_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    url = f'https://graph.microsoft.com/v1.0/users/{USER_ID}/sendMail'
    body = {
        "message": {
            "subject": asunto,
            "body": {
                "contentType": "Text",
                "content": contenido
            },
            "toRecipients": [{"emailAddress": {"address": destinatario}}]
        }
    }
    res = requests.post(url, headers=headers, json=body)
    return res.status_code
