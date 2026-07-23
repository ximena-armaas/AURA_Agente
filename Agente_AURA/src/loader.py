from langchain_community.document_loaders import CSVLoader

def cargar_documentos(ruta_csv):
    loader = CSVLoader(
        file_path=str(ruta_csv),
        encoding="utf-8"
    )

    documentos = loader.load()

    return documentos