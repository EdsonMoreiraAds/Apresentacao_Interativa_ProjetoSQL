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
  .block-container { padding: 0.5rem 0.75rem 1rem !important; max-width: 100% !important; }

  /* FORCE columns horizontal on ALL screen sizes (mobile fix) */
  [data-testid="stHorizontalBlock"] {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 4px !important;
    align-items: center !important;
  }
  [data-testid="stColumn"] {
    min-width: 0 !important;
    width: auto !important;
  }

  /* Nav buttons */
  [data-testid="stColumn"] .stButton > button {
    width: 100% !important;
    border-radius: 8px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 6px 2px !important;
    border: 1px solid #cdd8e3 !important;
    background: #fff !important;
    color: #0B2B40 !important;
    white-space: nowrap !important;
  }
  [data-testid="stColumn"] .stButton > button:hover {
    background: #065A82 !important; color: #fff !important;
  }
  [data-testid="stColumn"] .stButton > button:disabled { opacity: .3 !important; }

  /* Title bar */
  .title-bar {
    background: linear-gradient(90deg, #0B2B40, #065A82);
    color: white; padding: 10px 14px; border-radius: 8px;
    margin-bottom: 8px; font-size: 13px; font-weight: 700;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 2px;
  }
  .subtitle { font-size: 10px; opacity: .75; font-weight: 400; }

  /* Counter */
  .counter {
    text-align: center; font-size: 13px; font-weight: 700;
    color: #065A82; line-height: 1.2;
  }

  /* Slide image */
  [data-testid="stImage"] > img {
    width: 100% !important; height: auto !important;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,.18);
  }
</style>
""", unsafe_allow_html=True)

# ── Slides ────────────────────────────────────────────────
slides_dir = Path(__file__).parent
slides = sorted(slides_dir.glob("slide_*.jpg"))
total = len(slides)

if "slide" not in st.session_state:
    st.session_state.slide = 0

def clamp(n): return max(0, min(total - 1, n))

# ── Header ────────────────────────────────────────────────
st.markdown(f"""
<div class="title-bar">
  <span>📊 Pipeline Analítico Completo — Escola de Idiomas</span>
  <span class="subtitle">Digital College · DA34 · Prof. Eduardo Oliveira</span>
</div>
""", unsafe_allow_html=True)

# ── Nav row ───────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns([1, 1, 3, 1, 1])
with c1:
    if st.button("⏮", key="first", disabled=st.session_state.slide == 0):
        st.session_state.slide = 0; st.rerun()
with c2:
    if st.button("◀", key="prev", disabled=st.session_state.slide == 0):
        st.session_state.slide = clamp(st.session_state.slide - 1); st.rerun()
with c3:
    st.markdown(
        f'<div class="counter">{st.session_state.slide + 1} / {total}</div>',
        unsafe_allow_html=True,
    )
with c4:
    if st.button("▶", key="next", disabled=st.session_state.slide == total - 1):
        st.session_state.slide = clamp(st.session_state.slide + 1); st.rerun()
with c5:
    if st.button("⏭", key="last", disabled=st.session_state.slide == total - 1):
        st.session_state.slide = total - 1; st.rerun()

# ── Progress ──────────────────────────────────────────────
st.progress((st.session_state.slide + 1) / total)

# ── Slide image ───────────────────────────────────────────
st.image(str(slides[st.session_state.slide]), use_container_width=True)

# ── Slider ────────────────────────────────────────────────
val = st.slider(
    "slide",
    min_value=1, max_value=total,
    value=st.session_state.slide + 1,
    label_visibility="collapsed",
)
if val - 1 != st.session_state.slide:
    st.session_state.slide = val - 1; st.rerun()
