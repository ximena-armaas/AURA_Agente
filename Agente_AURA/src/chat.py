import os

from dotenv import load_dotenv
from langchain_cohere import ChatCohere

# Cargar variables del archivo .env
load_dotenv()


def crear_chat():
    """
    Crea el modelo de chat de Cohere.
    """

    chat = ChatCohere(
        model="command-a-03-2025",
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        temperature=0
    )

    return chat