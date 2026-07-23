import streamlit as st

from src.loader import cargar_documentos
from src.splitter import dividir_documentos
from src.embeddings import crear_embeddings
from src.vectorstore import crear_vectorstore
from src.retriever import crear_retriever
from src.chat import crear_chat
from src.prompt import crear_prompt
from src.agent import crear_agente


@st.cache_resource
def cargar_agente():
    documentos = cargar_documentos("rag_base.csv")
    chunks = dividir_documentos(documentos)
    embeddings = crear_embeddings()
    vectorstore = crear_vectorstore(chunks, embeddings)
    retriever = crear_retriever(vectorstore)
    chat = crear_chat()
    prompt = crear_prompt()

    return crear_agente(chat, retriever, prompt)


agente = cargar_agente()

st.set_page_config(
    page_title="AURA",
    page_icon="💙✨",
)

st.title("💙✨ AURA 💙✨")
st.subheader("AURA, tu asistente inteligente para acompañarte en cada consulta.")

st.write(
    "Realiza cualquier consulta relacionada con la clínica."
)

pregunta = st.text_input(
    "Escribe tu pregunta"
)

if st.button("Consultar"):

    if not pregunta.strip():
        st.warning("Por favor escribe una pregunta.")
    else:

        with st.spinner("Consultando..."):

            respuesta = agente.invoke(pregunta)

        st.success("Respuesta")

        st.write(respuesta)