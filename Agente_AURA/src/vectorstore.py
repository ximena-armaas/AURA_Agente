from langchain_community.vectorstores import FAISS

def crear_vectorstore(chunks, embeddings):
    """
    Crea una base de datos vectorial FAISS.
    """


    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore