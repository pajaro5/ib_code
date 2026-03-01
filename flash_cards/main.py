import streamlit as st
import pandas as pd
from flashcard import Flashcard
from deck import Deck  

def main():
    st.set_page_config(page_title="OOP Flashcards", layout="centered") # Layout centered se ve mejor para cartas
    st.title("🗂️ Repasador de OOP")

    if 'my_deck' not in st.session_state:
        try:
            # Asegúrate que este archivo exista
            df = pd.read_csv("flashcards.csv", header=None) 
            st.session_state.my_deck = Deck(df.values)
        except FileNotFoundError:
            st.error("Archivo 'flashcards.csv' no encontrado.")
            return

    deck = st.session_state.my_deck
    
    # Verificamos si hay cartas antes de continuar
    if not deck.cards:
        st.write("¡No hay cartas en el mazo!")
        return

    current = deck.get_current()

    # --- LÓGICA DE CONTENIDO ---
    # Si la carta está "volteada", mostramos respuesta, si no, la pregunta
    if deck.is_flipped:
        contenido = f"**Respuesta:**\n\n{current.answer}"
        color_borde = "#4CAF50" # Verde para respuesta
    else:
        contenido = f"**Pregunta:**\n\n{current.question}"
        color_borde = "#FF9800" # Naranja para pregunta

    # --- INTERFAZ DE LA CARTA ---
    # --- INTERFAZ DE LA CARTA ---
    st.markdown(
        f"""
        <div style="
            padding: 20px; 
            border-radius: 10px; 
            border-left: 10px solid {color_borde}; 
            background-color: #262730; 
            color: #FFFFFF;  /* <--- ESTA LÍNEA ARREGLA EL PROBLEMA */
            box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
            margin-bottom: 20px;
            font-size: 20px;">
            {contenido}
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- BOTONES DINÁMICOS ---
    # Usamos 3 columnas: Anterior | Acción Central | Siguiente
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Anterior", use_container_width=True):
            deck.previous_card()
            st.rerun()

    with col2:
        # El botón central cambia según el estado (Ver respuesta o nada)
        if not deck.is_flipped:
            if st.button("👀 Ver Respuesta", use_container_width=True):
                deck.toggle_flip()
                st.rerun()
        else:
            # Opcional: Podrías dejar este vacío o poner un mensaje
            st.info("Respuesta visible")

    with col3:
        if st.button("Siguiente ➡️", use_container_width=True):
            deck.next_card()
            st.rerun()
    

if __name__ == "__main__":
    main()