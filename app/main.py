import streamlit as st
from eigenscribe_ui.styles.theme import load_theme
from eigenscribe_ui.helpers.example import hello

# This MUST be the first Streamlit command
st.set_page_config(page_title="Eigenscribe © 2026 Streamlit Theme", layout="wide")

# Now load the theme
load_theme()

st.title("Eigenscribe © 2026 Streamlit Theme")
st.write("If you can see this, everything is working.")
st.write(hello())

st.markdown(
    """
    <div class="app-root">
        <h1 class="gradient_text1">IF YOU SEE GRADIENT TEXT, CSS WORKS</h1>
        <p>This is a forced test.</p>
        <button class="btn">Test Button</button>
    </div>
    """,
    unsafe_allow_html=True,
)