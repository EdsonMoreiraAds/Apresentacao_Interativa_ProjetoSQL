import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Pipeline Analítico — Escola de Idiomas",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
  /* Remove Streamlit chrome */
  [data-testid="stHeader"],
  [data-testid="stToolbar"],
  [data-testid="stDecoration"] { display: none !important; }
  .block-container { padding: 0.75rem 1rem 1rem !important; max-width: 100% !important; }

  /* Title bar */
  .title-bar {
    background: linear-gradient(90deg, #0B2B40, #065A82);
    color: white; padding: 10px 16px; border-radius: 8px;
    margin-bottom: 10px; display: flex;
    justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 4px;
  }
  .title-bar .main-title { font-size: 14px; font-weight: 700; }
  .title-bar .subtitle   { font-size: 11px; opacity: .75; }

  /* Slide counter */
  .counter {
    text-align: center; font-size: 14px; font-weight: 700;
    color: #065A82; padding: 6px 0;
  }

  /* Nav buttons */
  div[data-testid="column"] .stButton > button {
    width: 100%; border-radius: 8px; font-size: 20px;
    font-weight: 700; padding: 6px 4px;
    border: 1px solid #D8E3ED;
    background: #fff; color: #0B2B40;
    transition: background .2s, color .2s;
  }
  div[data-testid="column"] .stButton > button:hover {
    background: #065A82; color: #fff; border-color: #065A82;
  }
  div[data-testid="column"] .stButton > button:disabled { opacity: .3; }

  /* Slide image */
  div[data-testid="stImage"] img {
    border-radius: 8px;
    box-shadow: 0 4px 24px rgba(0,0,0,.15);
    width: 100% !important; height: auto !important;
  }

  /* Slider */
  div[data-baseweb="slider"] { padding: 0 4px; }

  /* Responsive: tighten on narrow screens */
  @media (max-width: 600px) {
    .title-bar .main-title { font-size: 12px; }
    .title-bar .subtitle   { display: none; }
    div[data-testid="column"] .stButton > button { font-size: 16px; padding: 4px 2px; }
  }
</style>
""", unsafe_allow_html=True)

# ── Slides ───────────────────────────────────────────────
slides_dir = Path(__file__).parent
slides = sorted(slides_dir.glob("slide_*.jpg"))
total = len(slides)

if "slide" not in st.session_state:
    st.session_state.slide = 0

def clamp(n): return max(0, min(total - 1, n))

# ── Header ───────────────────────────────────────────────
st.markdown("""
<div class="title-bar">
  <span class="main-title">📊 Pipeline Analítico Completo — Escola de Idiomas</span>
  <span class="subtitle">Digital College · Data Analytics 34 · Prof. Eduardo Oliveira</span>
</div>
""", unsafe_allow_html=True)

# ── Navigation buttons ───────────────────────────────────
c1, c2, c3, c4, c5 = st.columns([1, 1, 4, 1, 1])
with c1:
    if st.button("⏮", key="first", disabled=st.session_state.slide == 0):
        st.session_state.slide = 0; st.rerun()
with c2:
    if st.button("◀", key="prev", disabled=st.session_state.slide == 0):
        st.session_state.slide = clamp(st.session_state.slide - 1); st.rerun()
with c3:
    st.markdown(f'<div class="counter">Slide {st.session_state.slide + 1} de {total}</div>',
                unsafe_allow_html=True)
with c4:
    if st.button("▶", key="next", disabled=st.session_state.slide == total - 1):
        st.session_state.slide = clamp(st.session_state.slide + 1); st.rerun()
with c5:
    if st.button("⏭", key="last", disabled=st.session_state.slide == total - 1):
        st.session_state.slide = total - 1; st.rerun()

# ── Progress bar ─────────────────────────────────────────
st.progress((st.session_state.slide + 1) / total)

# ── Slide image ──────────────────────────────────────────
st.image(str(slides[st.session_state.slide]), use_container_width=True)

# ── Slider for quick jump ────────────────────────────────
new_val = st.slider(
    "Ir para slide:",
    min_value=1, max_value=total,
    value=st.session_state.slide + 1,
    label_visibility="collapsed",
)
if new_val - 1 != st.session_state.slide:
    st.session_state.slide = new_val - 1; st.rerun()
