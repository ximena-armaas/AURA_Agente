# 💙✨ AURA
# Asistente Inteligente de Atención al Paciente

## 🏥 Introducción

AURA es un asistente inteligente basado en Inteligencia Artificial Generativa diseñado para apoyar la atención informativa de pacientes dentro de una clínica médica.

El sistema utiliza una arquitectura **Retrieval-Augmented Generation (RAG)** que permite responder preguntas frecuentes utilizando exclusivamente información almacenada en una base documental proporcionada por la institución médica.

Su propósito es facilitar el acceso a información como servicios disponibles, horarios, procesos administrativos, requisitos de atención y preguntas frecuentes, ofreciendo respuestas rápidas, claras y confiables.

AURA no reemplaza la valoración médica profesional ni genera diagnósticos. Su función es brindar orientación basada únicamente en la información autorizada disponible en su base de conocimiento.

---

# 🎯 Propósito del sistema

El desarrollo de AURA surge como una solución para mejorar la comunicación entre una clínica y sus pacientes mediante un asistente digital disponible para resolver consultas frecuentes.

## Objetivos principales

- Facilitar el acceso a información institucional.
- Reducir tiempos de respuesta ante preguntas frecuentes.
- Centralizar documentación relacionada con la atención al paciente.
- Implementar recuperación inteligente de información mediante búsqueda semántica.
- Generar respuestas consistentes utilizando Inteligencia Artificial.
- Evitar respuestas incorrectas mediante restricciones basadas en contexto.

---

# 🧠 Funcionamiento general

AURA utiliza una arquitectura RAG, donde el modelo de lenguaje no responde únicamente con conocimiento propio, sino que primero consulta una base documental especializada.

El proceso funciona de la siguiente manera:
             Paciente
                │
                ▼
      Realiza una consulta
                │
                ▼
          Aplicación
                │
                ▼
      Recuperación semántica
           (FAISS)
                │
                ▼
   Documentos relevantes encontrados
                │
                ▼
      Construcción del contexto
                │
                ▼
         Modelo Cohere
                │
                ▼
       Respuesta generada
                │
                ▼
             Paciente

---

# 🏗 Arquitectura del proyecto

La solución está compuesta por diferentes módulos encargados de procesar la información, realizar búsquedas inteligentes y generar respuestas.

## Flujo de datos

### 1. Carga de información

El sistema inicia leyendo el archivo documental donde se encuentra la información oficial de la clínica.

Responsable:
loader.py

---

### 2. Procesamiento documental

Los documentos son divididos en fragmentos pequeños para mejorar la precisión de búsqueda.

Responsable:
splitter.py

---

### 3. Generación de embeddings

Cada fragmento es convertido en una representación vectorial utilizando modelos de Cohere.

Responsable:
embeddings.py

---

### 4. Almacenamiento vectorial

Los vectores generados son almacenados en FAISS para permitir búsquedas mediante similitud semántica.

Responsable:
vectorstore.py

---

### 5. Recuperación de información

Cuando un paciente realiza una pregunta, el sistema identifica los fragmentos más relacionados con la consulta.

Responsable:
retriever.py

---

### 6. Generación de respuesta

El contexto recuperado es enviado al modelo de lenguaje junto con reglas específicas para generar una respuesta segura y coherente.

Responsable:
prompt.py
agent.py

---

# 🛡 Reglas de comportamiento de AURA

Para garantizar respuestas confiables, el asistente sigue las siguientes restricciones:

- Utiliza únicamente información disponible en la base documental.
- No inventa información.
- No proporciona diagnósticos médicos.
- No recomienda tratamientos personalizados.
- Mantiene comunicación profesional y clara.
- Indica cuando una información no está disponible.

Cuando una consulta no puede ser respondida, AURA responde:

---

# 🗂 Organización del proyecto
│
├── src/
│ ├── agent.py
│ ├── chat.py
│ ├── embeddings.py
│ ├── loader.py
│ ├── prompt.py
│ ├── retriever.py
│ ├── splitter.py
│ └── vectorstore.py
│
├── rag_base.csv
├── requirements.txt
├── main.py
├── README.md
└── .env


---

# ⚙️ Instalación y configuración

## Requisitos previos

Antes de ejecutar el proyecto es necesario contar con:

- Python 3.12 o superior.
- Una API Key válida de Cohere.
- Acceso a terminal o consola.

---

# ⚙️ Instalación y configuración

## 1. Descargar el proyecto

Clonar el repositorio utilizando Git:

```bash
git clone https://github.com/ximena-armaas/AURA_Agente.git
```

---

## 2. Acceder al directorio del proyecto

```bash
cd Agente_AURA
```

---

## 3. Crear entorno virtual

En Windows:

```bash
python -m venv .venv
```

---

## 4. Activar entorno virtual

```bash
.venv\Scripts\activate
```

---

## 5. Instalar dependencias

Instalar todas las librerías necesarias para ejecutar el proyecto:

```bash
pip install -r requirements.txt
```

---

## 6. Configurar variables de entorno

Crear un archivo llamado:

```
.env
```

Agregar la API Key de Cohere:

```env
COHERE_API_KEY=TU_API_KEY
```

---

# ▶️ Ejecución

Para iniciar AURA ejecutar:

```bash
python main.py
```

Cuando el sistema inicia correctamente se mostrará:

```text
============================================================
💙✨ AURA
Asistente Inteligente de Atención al Paciente
============================================================

Escribe tu consulta o escribe 'gracias' para finalizar.
```

---

# 📚 Fuente de conocimiento

AURA utiliza como fuente principal de información el archivo:

```
rag_base.csv
```

Este documento contiene la información institucional utilizada para generar las respuestas del asistente.

La base de conocimiento incluye información relacionada con:

- Información general de la clínica.
- Servicios disponibles.
- Especialidades médicas.
- Horarios de atención.
- Atención al paciente.
- Preguntas frecuentes.
- Procesos administrativos.
- Métodos de contacto.
- Facturación.
- Requisitos para consultas.

La información contenida en este archivo representa la única fuente autorizada utilizada por AURA para responder las consultas de los pacientes.

---

# 🧪 Ejemplos de consultas

AURA puede responder preguntas frecuentes como:

### Consulta

```
¿Cómo puedo agendar una cita?
```

---

### Consulta

```
¿Qué documentos necesito para mi primera consulta?
```

---

### Consulta

```
¿Cómo puedo solicitar una factura?
```

---

# 🧰 Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3.12 | Desarrollo principal del sistema |
| LangChain | Construcción de la arquitectura RAG |
| Cohere API | Modelo generativo y generación de embeddings |
| FAISS | Motor de búsqueda vectorial |
| CSVLoader | Lectura de la base documental |
| PromptTemplate | Definición del comportamiento del agente |
| Streamlit | Desarrollo de interfaz web (si aplica) |

---

# 🚀 Despliegue

Actualmente, **AURA** se encuentra desplegado en **Streamlit Cloud**, por lo que puede utilizarse directamente desde el siguiente enlace:

**https://auraagente-mju5v29y4x3esgef2hejvy.streamlit.app/**

El proyecto incluye dos formas de ejecución:

- **Modo Streamlit** (implementación actual): utilizado para el despliegue web y la interacción mediante una interfaz gráfica.
- **Modo consola (Python)**: permite ejecutar el agente de forma local desde la terminal.

Ambos modos ya se encuentran implementados dentro del archivo **`main.py`**. Actualmente, el código correspondiente a la ejecución en **Streamlit** es el que está habilitado, mientras que la versión para **Python por consola** permanece comentada.

Para ejecutar el proyecto de forma local desde la terminal únicamente es necesario:

1. Comentar el bloque correspondiente a **Streamlit**.
2. Descomentar el bloque correspondiente a la ejecución por **Python**.

No es necesario realizar cambios adicionales en la lógica del proyecto, ya que ambos modos comparten la misma arquitectura y componentes internos.

---

# 👩‍💻 Autora

## Ximena Armas Cuatecontzi

Proyecto desarrollado como implementación de un:

**Asistente Inteligente de Atención al Paciente basado en Retrieval-Augmented Generation (RAG)**

Tecnologías principales:

- Python
- LangChain
- Cohere
- FAISS
- Inteligencia Artificial Generativa