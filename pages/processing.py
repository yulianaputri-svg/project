import streamlit as st
from PIL import Image
import numpy as np
from utils import (
    pil_to_numpy, numpy_to_pil,
    translation_matrix, scaling_matrix, rotation_matrix,
    shear_matrix, reflection_matrix, apply_affine_transform
)

# 🌸 Custom Pink Theme
pink_style = """
<style>
/* Background */
.main {
    background-color: #ffe9f3 !important;
}

/* Titles */
h1, h2, h3 {
    color: #d63384 !important;
    font-weight: 700;
}

/* Sidebar title */
.css-1d391kg {
    color: #d63384 !important;
}

/* Result box */
.result-box {
    background-color: #ffe3ee;
    padding: 12px;
    border-radius: 12px;
    border-left: 4px solid #ff4dab;
    margin-top: 10px;
}
</style>
"""
st.markdown(pink_style, unsafe_allow_html=True)

def run():
    st.title("🎀 Image Processing Tools 💗")
    st.write("✨ Edit, transform, and play with your image using matrix transformations!")

    uploaded = st.file_uploader("📤 Upload image", type=["png","jpg","jpeg"])
    if not uploaded:
        st.info("Upload gambar dulu yaa 😊")
        return

    img = Image.open(uploaded).convert("RGBA")
    arr = pil_to_numpy(img)
    h, w = img.size[1], img.size[0]
    cx, cy = w / 2, h / 2

    st.subheader("🖼️ Original Image")
    st.image(img, width=300)

    mode = st.sidebar.selectbox("🎨 Mode", ["Transformations", "Filters"])

    if mode == "Transformations":
        tf = st.sidebar.selectbox("✨ Transformation Type", 
            ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"]
        )

        # ----- TRANSLATION -----
        if tf == "Translation":
            st.sidebar.markdown("**🔀 Translation Settings**")
            tx = st.sidebar.slider("Shift X (Tx)", -w, w, 0)
            ty = st.sidebar.slider("Shift Y (Ty)", -h, h, 0)
            M = translation_matrix(tx, ty)

        # ----- SCALING -----
        elif tf == "Scaling":
            st.sidebar.markdown("**📏 Scaling Settings**")
            sx = st.sidebar.slider("Scale X", 0.1, 3.0, 1.0)
            sy = st.sidebar.slider("Scale Y", 0.1, 3.0, 1.0)
            M = scaling_matrix(sx, sy, (cx, cy))

        # ----- ROTATION -----
        elif tf == "Rotation":
            st.sidebar.markdown("**🔄 Rotation Settings**")
            ang = st.sidebar.slider("Angle (°)", -180, 180, 0)
            M = rotation_matrix(ang, (cx, cy))

        # ----- SHEARING -----
        elif tf == "Shearing":
            st.sidebar.markdown("**📐 Shearing Settings**")
            shx = st.sidebar.slider("Shear X", -1.0, 1.0, 0.0)
            shy = st.sidebar.slider("Shear Y", -1.0, 1.0, 0.0)
            M = shear_matrix(shx, shy)

        # ----- REFLECTION -----
        elif tf == "Reflection":
            st.sidebar.markdown("**🪞 Reflection Settings**")
            axis = st.sidebar.selectbox("Choose Axis", ["x", "y"])
            M = reflection_matrix(axis)

        # Apply transformation
        out = apply_affine_transform(arr, M)
        out_pil = numpy_to_pil(out)

        st.subheader("💖 Transformed Image")
        st.image(out_pil, width=350)

        st.markdown(
            f"<div class='result-box'>✨ Transformation applied using <b>{tf}</b> method!</div>",
            unsafe_allow_html=True
        )

    else:
        st.subheader("🎨 Filters")
        st.info("Filter belum ditambahkan yaa 😁 (optional task)")


