import streamlit as st

# --- CUSTOM PINK THEME ---
pink_style = """
<style>
/* Background App */
.main {
    background-color: #ffe9f3 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #ffedf7 !important;
}

/* Title colors */
h1, h2, h3 {
    color: #d63384 !important;
    font-weight: 700;
}

/* Buttons */
.stButton>button {
    background-color: #ff4dab !important;
    color: white !important;
    border-radius: 10px;
    border: none;
}

/* Info / Alert */
.stAlert {
    background-color: #ffe3ee !important;
    border-left: 5px solid #ff4dab !important;
}
</style>
"""

st.markdown(pink_style, unsafe_allow_html=True)


# --- PAGE IMPORTS ---
import pages.matrix_demo as matrix_demo
import pages.processing as processing
import pages.team as team


# --- SIDEBAR ---
st.sidebar.title("🎀 Navigation Menu")
page = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Home", "Matrix Demo", "Processing", "Team Members"]
)


# --- HOME PAGE ---
if page == "Home":
    st.title("💗 Image Tools — Final Project")
    st.header("🎉 Selamat Datang!")

    st.write("""
    ✨ Aplikasi ini dibuat sebagai final project kelompok 4.  
    Berisi fitur untuk:
    
    - 🖼️ *Image Processing Tools* (Transform, Filter, BG Removal)  
    - ➗ *Matrix Transformation Demo*  
    - 👥 *Team Members*  

    Silakan gunakan sidebar untuk pindah halaman.
    """)

    st.info("💡 Tips: Klik menu di kiri untuk melihat fitur lainnya!")


# --- MATRIX DEMO PAGE ---
elif page == "Matrix Demo":
    matrix_demo.run()


# --- PROCESSING PAGE ---
elif page == "Processing":
    processing.run()


# --- TEAM PAGE ---
elif page == "Team Members":
    team.run()
