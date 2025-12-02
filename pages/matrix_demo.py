import streamlit as st
import numpy as np
from utils import translation_matrix, scaling_matrix, rotation_matrix

# 🌸 Custom Pink Theme
pink_style = """
<style>
/* Page Background */
.main {
    background-color: #ffe9f3 !important;
}

/* Title & Headers */
h1, h2, h3 {
    color: #d63384 !important;
    font-weight: 700;
}

/* Sliders */
.css-1cpxqw2, .stSlider {
    color: #d63384 !important;
}

/* Result Box */
.result-box {
    background-color: #ffe3ee;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #ff4dab;
}
</style>
"""
st.markdown(pink_style, unsafe_allow_html=True)

def run():
    st.title("🎀 Matrix Transformation Demo 💗")
    st.write("✨ Explore translation, rotation, and scaling in a fun & visual way!")

    st.subheader("📌 Input Coordinates")
    x = st.number_input("Coordinate **x**", value=10.0)
    y = st.number_input("Coordinate **y**", value=20.0)

    # ---------------- TRANSLATION ----------------
    st.subheader("💞 Translation")
    tx = st.slider("Shift on X (Tx)", -50, 50, 10)
    ty = st.slider("Shift on Y (Ty)", -50, 50, 5)

    Mt = translation_matrix(tx, ty)
    st.write("📘 Translation Matrix:")
    st.write(Mt)

    res_t = Mt @ np.array([x, y, 1])
    st.markdown(f"""
    <div class='result-box'>
        <b>✨ Hasil Translation:</b> {res_t[:2]}
    </div>
    """, unsafe_allow_html=True)

    # ---------------- ROTATION ----------------
    st.subheader("💫 Rotation")
    ang = st.slider("Rotation Angle (°)", -180, 180, 0)

    Mr = rotation_matrix(ang)
    st.write("📘 Rotation Matrix:")
    st.write(Mr)

    res_r = Mr @ np.array([x, y, 1])
    st.markdown(f"""
    <div class='result-box'>
        <b>🌟 Hasil Rotation:</b> {res_r[:2]}
    </div>
    """, unsafe_allow_html=True)
