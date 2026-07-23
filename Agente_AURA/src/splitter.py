from langchain_text_splitters import RecursiveCharacterTextSplitter


def dividir_documentos(documentos):
    """
    Divide los documentos en fragmentos (chunks).
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documentos)

    return chunks