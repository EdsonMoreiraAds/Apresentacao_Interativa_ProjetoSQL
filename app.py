import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Pipeline Analítico — Escola de Idiomas",
    page_icon="📊",
    layout="wide",
)

# CSS
st.markdown("""
<style>
[data-testid="stHeader"] { display:none; }
[data-testid="stToolbar"] { display:none; }
.block-container { padding: 0.5rem 1rem 1rem !important; max-width: 100% !important; }
div[data-testid="stImage"] img { border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,.15); }
.stButton > button {
    border-radius: 8px; font-weight: 600; font-size: 18px;
    padding: 6px 20px; border: 1px solid #D8E3ED;
    background: #fff; color: #0B2B40;
    transition: all .2s;
}
.stButton > button:hover { background: #065A82; color: #fff; border-color: #065A82; }
.stButton > button:disabled { opacity: .35; }
.slide-counter {
    text-align: center; font-size: 15px; font-weight: 600;
    color: #065A82; padding: 8px 0;
}
.title-bar {
    background: linear-gradient(90deg, #0B2B40, #065A82);
    color: white; padding: 10px 20px; border-radius: 8px;
    margin-bottom: 12px; font-size: 14px;
    display: flex; justify-content: space-between; align-items: center;
}
div[data-baseweb="slider"] { padding-top: 4px; }
</style>
""", unsafe_allow_html=True)

# Load slides
slides_dir = Path(__file__).parent / "slides"
slides = sorted(slides_dir.glob("slide_*.jpg"))
total = len(slides)

# Session state
if "slide" not in st.session_state:
    st.session_state.slide = 0

def go(n):
    st.session_state.slide = max(0, min(total - 1, st.session_state.slide + n))

def jump(n):
    st.session_state.slide = n

# Header
st.markdown("""
<div class="title-bar">
  <span>📊 Pipeline Analítico Completo — Escola de Idiomas</span>
  <span style="opacity:.7;font-size:12px">Digital College · Data Analytics 34 · Prof. Eduardo Oliveira</span>
</div>
""", unsafe_allow_html=True)

# Navigation bar
c1, c2, c3, c4, c5, c6, c7 = st.columns([1, 1, 1, 4, 1, 1, 1])
with c1:
    if st.button("⏮", disabled=st.session_state.slide == 0, key="first"):
        jump(0); st.rerun()
with c2:
    if st.button("◀", disabled=st.session_state.slide == 0, key="prev"):
        go(-1); st.rerun()
with c4:
    st.markdown(f'<div class="slide-counter">Slide {st.session_state.slide + 1} de {total}</div>', unsafe_allow_html=True)
with c6:
    if st.button("▶", disabled=st.session_state.slide == total - 1, key="next"):
        go(1); st.rerun()
with c7:
    if st.button("⏭", disabled=st.session_state.slide == total - 1, key="last"):
        jump(total - 1); st.rerun()

# Progress bar
st.progress((st.session_state.slide + 1) / total)

# Slide image
st.image(str(slides[st.session_state.slide]), use_container_width=True)

# Thumbnail strip
st.markdown("---")
st.markdown("**Ir para slide:**")
thumb_cols = st.columns(total)
for i, col in enumerate(thumb_cols):
    with col:
        if st.button(str(i + 1), key=f"t{i}",
                     type="primary" if i == st.session_state.slide else "secondary"):
            jump(i); st.rerun()
