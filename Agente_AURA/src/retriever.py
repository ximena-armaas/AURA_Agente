def crear_retriever(vectorstore):
    """
    Crea un retriever a partir del vector store.
    """

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever