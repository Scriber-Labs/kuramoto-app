import streamlit as st
from pathlib import Path
import os
import base64

def load_theme():
    root_path = Path(os.getcwd()) 
    css_path = root_path / "static" / "CSS" / "main.css"
    img_path = root_path / "static" / "images" / "wisp.jpg"

    if css_path.exists():
        css_content = css_path.read_text()
        
        # If the image exists, encode it and inject it into the CSS
        if img_path.exists():
            with open(img_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            
            # This replaces a placeholder in your CSS with the actual image data
            css_content = css_content.replace("REPLACE_WITH_WISP_BASE64", encoded_string)
        
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS not found at {css_path}")