# 📚 Biblioteca con FastAPI + LangChain + Microsoft Graph API

Este proyecto permite a los usuarios realizar operaciones sobre libros por correo electrónico, usando lenguaje natural y procesamiento con LLMs.

## 🚀 Funciones
- Registrar, listar y eliminar libros.
- Reservar, renovar y eliminar reservas.
- Procesamiento automático de correos entrantes.
- Respuesta automática vía correo.
- Despliegue en Azure.

## 🛠️ Herramientas usadas
- Python, FastAPI, SQLAlchemy, LangChain, Uvicorn
- Microsoft Graph API
- PostgreSQL
- Azure App Service / Azure Container

## 📦 Instalación local

```
git clone https://github.com/VaneJimenez/biblioteca_api.git
cd biblioteca_api
python -m venv venv
venv\Scripts\activate # source venv/bin/activate en Linux
pip install -r requirements.txt
```

## ⚙️ Configuración del entorno
Crea un archivo .env y añade:
```
DATABASE_URL=postgresql://user:password@localhost:puerto/nombre_db
OPENAI_API_KEY=TU_CLAVE_OPENAI
MSAL_CLIENT_ID=...
MSAL_CLIENT_SECRET=...
TENANT_ID=...
```
## ▶️ Ejecutar servidor
```
uvicorn main:app --reload
```
