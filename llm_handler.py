from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

def procesar_mensaje(mensaje_usuario: str) -> str:
   
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=(
            "Eres un asistente inteligente de biblioteca. "
            "Interpreta solicitudes de usuarios para reservar libros, "
            "consultar disponibilidad o devolver materiales."
        )),
        HumanMessage(content="{input}")
    ])

    chain = prompt | llm

    respuesta = chain.invoke({"Input": mensaje_usuario})

    return respuesta.content
