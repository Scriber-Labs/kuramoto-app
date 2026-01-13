import streamlit as st
from pathlib import Path
import os
import base64


def load_theme():
    root_path = Path(os.getcwd())
    css_dir = root_path / "static" / "CSS"
    
    # Define the files we want to load
    main_css_path = css_dir / "main.css"
    streamlit_css_path = css_dir / "streamlit_ui.css"
    img_path = root_path / "static" / "images" / "wisp.jpg"

    combined_css = ""

    # 1. Load Main CSS
    if main_css_path.exists():
        combined_css += main_css_path.read_text()
    else:
        st.error(f"Main CSS not found at {main_css_path}")

    # 2. Load Streamlit UI CSS
    if streamlit_css_path.exists():
        combined_css += "\n" + streamlit_css_path.read_text()
    else:
        st.warning(f"Streamlit UI CSS not found at {streamlit_css_path}")

    # 3. Handle Background Image Injection
    if img_path.exists() and "REPLACE_WITH_WISP_BASE64" in combined_css:
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        combined_css = combined_css.replace("REPLACE_WITH_WISP_BASE64", encoded_string)

    # 4. Inject all styles at once
    if combined_css:
        st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)
