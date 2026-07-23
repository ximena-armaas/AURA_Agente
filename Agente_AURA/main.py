from src.loader import cargar_documentos
from src.splitter import dividir_documentos
from src.embeddings import crear_embeddings
from src.vectorstore import crear_vectorstore
from src.retriever import crear_retriever
from src.chat import crear_chat
from src.prompt import crear_prompt
from src.agent import crear_agente
from pathlib import Path

# 1. Cargar documentos


BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "rag_base.csv"

documentos = cargar_documentos(csv_path)

# 2. Dividir documentos
chunks = dividir_documentos(documentos)

# 3. Crear embeddings
embeddings = crear_embeddings()

# 4. Crear FAISS
vectorstore = crear_vectorstore(chunks, embeddings)

# 5. Crear retriever
retriever = crear_retriever(vectorstore)

# 6. Crear modelo de chat
chat = crear_chat()

# 7. Crear prompt
prompt = crear_prompt()

# 8. Crear cadena RAG
agente = crear_agente(chat, retriever, prompt)

print("=" * 60)
print("💙✨ AURA 💙✨")
print("AURA, tu asistente inteligente para acompañarte en cada consulta.")
print("=" * 60)
print("Escribe 'Gracias' para finalizar la conversación.\n")

while True:

    pregunta = input("👤 Tu pregunta: ")

    if not pregunta.strip():
        print("\n⚠️ Por favor escribe una consulta.\n")
        continue


    if "gracias" in pregunta.lower():
        print("\n💙✨ Gracias por usar AURA, tu asistente inteligente para acompañarte en cada consulta.")
        print("¡Hasta pronto!")
        break
    try:
        respuesta = agente.invoke(pregunta)

        print("\n 💙✨ AURA 💙✨: \n")
        print(respuesta)

    except Exception as e:
        print("\n⚠️ Ocurrió un error al procesar tu consulta.")
        print("Por favor, intenta nuevamente.")
        

    print("\n" + "-" * 60 + "\n")