from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel

def formatear_documentos(documentos):
    """
    Convierte una lista de documentos en un único texto.
    """

    return "\n\n".join(
        documento.page_content
        for documento in documentos
    )

def crear_agente(chat, retriever, prompt):
    """
    Construye la cadena completa del agente RAG.
    """

    cadena = (
        RunnableParallel(
            context=retriever | formatear_documentos,
            question=RunnablePassthrough(),
        )
        | prompt
        | chat
        | StrOutputParser()
    )

    return cadena