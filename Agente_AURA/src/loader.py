from langchain_community.document_loaders import CSVLoader


def cargar_documentos(path_csv):
    """
    Carga el archivo CSV y devuelve una lista de documentos.
    """

    loader = CSVLoader(
        file_path=path_csv,
        encoding="utf-8"
    )

    documentos = loader.load()

    return documentos