import os

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

# Cargar las variables del archivo .env
load_dotenv()


def crear_embeddings():
    """
    Crea el modelo de embeddings de Cohere.
    """

    embeddings = CohereEmbeddings(
        model="embed-multilingual-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )

    return embeddings