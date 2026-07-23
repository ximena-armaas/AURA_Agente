import streamlit as st
from pathlib import Path

from src.loader import cargar_documentos
from src.splitter import dividir_documentos
from src.embeddings import crear_embeddings
from src.vectorstore import crear_vectorstore
from src.retriever import crear_retriever
from src.chat import crear_chat
from src.prompt import crear_prompt
from src.agent import crear_agente


st.set_page_config(
    page_title="AURA",
    page_icon="💙",
    layout="wide"
)


@st.cache_resource(show_spinner="Preparando AURA...")
def cargar_agente():

    base_dir = Path(__file__).resolve().parent
    ruta_csv = base_dir / "rag_base.csv"

    # 1. Cargar documentos
    documentos = cargar_documentos(ruta_csv)

    # 2. Dividir documentos
    chunks = dividir_documentos(documentos)

    # 3. Crear embeddings
    embeddings = crear_embeddings()

    # 4. Crear vectorstore
    vectorstore = crear_vectorstore(chunks, embeddings)

    # 5. Crear retriever
    retriever = crear_retriever(vectorstore)

    # 6. Modelo
    chat = crear_chat()

    # 7. Prompt
    prompt = crear_prompt()

    # 8. Agente
    return crear_agente(chat, retriever, prompt)


agente = cargar_agente()


st.title("💙✨ AURA")
st.caption("Tu asistente inteligente para acompañarte en cada consulta.")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! 😊 Soy **AURA**. ¿En qué puedo ayudarte hoy?"
        }
    ]


for mensaje in st.session_state.messages:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])


pregunta = st.chat_input("Escribe tu pregunta...")


if pregunta:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": pregunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            try:
                respuesta = agente.invoke(pregunta)

                st.markdown(respuesta)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": respuesta
                    }
                )

            except Exception as e:

                mensaje_error = (
                    "Lo siento, ocurrió un error al procesar tu consulta."
                )

                st.error(mensaje_error)

                st.exception(e)