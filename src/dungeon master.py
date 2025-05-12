import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Título de la app
st.set_page_config(page_title="Dungeon Master Chatbot", page_icon="🐉")
st.title("🧙‍♂️ Dungeon Master Chatbot")
st.markdown("¡Habla con tu Dungeon Master para comenzar tu aventura en el mundo de Dungeons & Dragons!")

# Inicializa el historial del chat en la sesión
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "system", "content": "Eres un Dungeon Master experto en el lore de dragones y mazmorras. Responde con creatividad, drama y emoción."}
    ]

# Caja de entrada del usuario
mensaje_usuario = st.chat_input("¿Qué quieres decirle al Dungeon Master?")

# Si se envía un mensaje
if mensaje_usuario:
    st.session_state.mensajes.append({"role": "user", "content": mensaje_usuario})

    try:
        respuesta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.mensajes,
            temperature=0.8,
            max_tokens=700
        )
        contenido_respuesta = respuesta.choices[0].message.content.strip()
        st.session_state.mensajes.append({"role": "assistant", "content": contenido_respuesta})
    except Exception as e:
        contenido_respuesta = f"⚠️ Error al contactar con el Dungeon Master: {e}"
        st.session_state.mensajes.append({"role": "assistant", "content": contenido_respuesta})

# Muestra el historial del chat
for mensaje in st.session_state.mensajes[1:]:
    if mensaje["role"] == "user":
        with st.chat_message("user"):
            st.markdown(mensaje["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(mensaje["content"])
