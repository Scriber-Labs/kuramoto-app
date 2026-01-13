from eigenscribe_ui.theme.streamlit_theme import load_theme
load_theme()

import streamlit as st
from eigenscribe_ui.helpers.example import hello 

st.set_page_config(page_title="Eigenscribe © 2026 Streamlit Theme", layout="wide")
st.title("Eigenscribe © 2026 Streamlit Theme")
st.write("If you can see this, everything is working.")
st.write(hello())

st.markdown(
    """
    <div class="app-root">
        <h1 class="gradient-text">IF YOU SEE GRADIENT TEXT, CSS WORKS</h1>
        <p>This is a forced test.</p>
        <button>Test Button</button>
    </div>
    """,
    unsafe_allow_html=True,
)