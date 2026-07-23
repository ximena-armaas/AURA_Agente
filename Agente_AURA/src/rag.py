from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


def formatear_documentos(documentos):
    return "\n\n".join(
        documento.page_content
        for documento in documentos
    )


def crear_cadena_rag(chat, retriever, prompt):

    cadena = (
        RunnableParallel(
            context=retriever | formatear_documentos,
            input=RunnablePassthrough()
        )
        | prompt
        | chat
        | StrOutputParser()
    )

    return cadena