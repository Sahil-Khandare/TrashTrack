import streamlit as st
import base64
from pathlib import Path
from PIL import Image, ImageOps


def load_css(css_path, bg_image_path):

    image_data = base64.b64encode(
        Path(bg_image_path).read_bytes()
    ).decode()

    bg_data_uri = f"data:image/png;base64,{image_data}"

    css = Path(css_path).read_text()

    css = css.replace("__BG_IMAGE__", bg_data_uri)

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


def process_image(uploaded_file):

    image = Image.open(uploaded_file)

    image = ImageOps.exif_transpose(image).convert("RGB")

    return image