import streamlit as st
from pathlib import Path

def load_theme():
    css_path = Path(__file__).parent / "my_themes" / "dist" / "eigenscribe.css"
    st.markdown(
        f"<style>{css_path.read_text()}</style>",
        unsafe_allow_html=True,
    )
