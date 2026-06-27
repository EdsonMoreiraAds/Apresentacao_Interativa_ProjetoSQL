import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(
    page_title="Pipeline Analítico — Escola de Idiomas",
    page_icon="📊",
    layout="wide",
)

# Remove padding padrão do Streamlit para a apresentação ocupar tela cheia
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
    [data-testid="stHeader"] { display: none; }
    [data-testid="stToolbar"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

html_file = pathlib.Path(__file__).parent / "Apresentacao_Interativa_ProjetoSQL_v2.html"
html_content = html_file.read_text(encoding="utf-8")

components.html(html_content, height=950, scrolling=True)
