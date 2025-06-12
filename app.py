import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np
import requests

# Konfigurasi halaman
st.set_page_config(
    page_title="Portfolio Data Science",
    page_icon="📊",
    layout="wide"
)

# Tambahkan CSS kustom untuk tampilan modern
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 24px;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 50px;
    }
    .card {
        background-color: #F9F9F9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Halaman
st.markdown("<div class='main-title'>👨‍💻 Data Science Portfolio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore our projects and latest insights in Data Science and AI</div>", unsafe_allow_html=True)

# Menu Navigasi
menu = st.sidebar.radio("Navigasi", ["🏠 Home", "📂 Projects", "📰 Blog", "📞 Contact"])

# Halaman Home
if menu == "🏠 Home":
    st.subheader("Selamat datang di DGrafika!")
    st.write("""
        Kami merupakan startup yang bergerak dalam bidang Data Science. Kami menangani berbagai proyek terkait data meliputi; data cleaning, data analysis, dan data visualisasi.
        Di website ini, Anda dapat menelusuri berbagai proyek kami, mulai dari prediksi dropout, analisis e-commerce dengan berbagai algoritma machine learning dan deep learning
        hingga eksperimen dengan model generatif terbaru.
    """)
    st.markdown("---")
    st.subheader("📫 Hubungi Saya")

    st.markdown("""
    📍 Lokasi: East Java, Indonesia  
    📧 Email: [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
    💼 LinkedIn: [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
    🐙 GitHub: [github.com/MSiswanto](https://github.com/MSiswanto)
""")


# Halaman Projects
elif menu == "📂 Projects":
    st.subheader("📁 Project List")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🎓 Dropout Prediction")
        st.write("Model machine learning untuk memprediksi risiko mahasiswa dropout berdasarkan data akademik.")
        st.link_button("View Project", "https://dropout-prediction-detection.streamlit.app/")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛒 E-commerce Data Analysis")
        st.write("Analisis data transaksi e-commerce untuk mendapatkan insight tren dan perilaku konsumen.")
        st.link_button("View Project", "https://analysis-brazilianecommerce.streamlit.app/")  # Ganti dengan URL kamu
        st.markdown("</div>", unsafe_allow_html=True)

# Halaman Blog
elif menu == "📰 Blog":
    st.subheader("🧠 Artikel")
    st.markdown("""
    Berikut beberapa topik yang sedang hangat di dunia data science:

    - 🔍 **RAG (Retrieval-Augmented Generation)** semakin populer di NLP.
    - 📊 **AutoML** tools seperti Google VertexAI dan H2O.ai semakin memudahkan eksperimen.
    - 🤖 **LLMs** terus berevolusi dengan model seperti Claude, Gemini, dan GPT-4o.
    - 🧠 **Prompt engineering** kini menjadi keterampilan wajib untuk praktisi AI.
    
    *(Coming soon: artikel-artikel mendalam di bagian ini.)*
    """)

# Halaman Kontak
elif menu == "📞 Contact":
    st.title("📞 Contact Us")
    st.markdown("Terima kasih telah mengunjungi portofolio kami. Silakan hubungi kami melalui kontak di bawah ini:")

    # Bagian Informasi Kontak
    st.markdown("""
    **📧 Email:** [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
    **💼 LinkedIn:** [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
    **🐙 GitHub:** [github.com/MSiswanto](https://github.com/MSiswanto)  
    """)

    st.markdown("---")

    # Formulir Kontak dengan layout lebih sempit
    st.subheader("📬 Form to Contact (simulasi)")
    col1, col2, col3 = st.columns([1, 2, 1])  # kolom tengah lebar, sisi kiri-kanan kosong

    with col2:
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")

            submitted = st.form_submit_button("Send Message")
            if submitted:
                payload = {
                    "name": name,
                    "email": email,
                    "message": message
                }
                response = requests.post("https://script.google.com/macros/s/AKfycbx.../exec", json=payload)

                if response.status_code == 200:
                    st.success("✅ Terimakasih! Pesan berhasil diterima dan dikirim ke Google Sheet.")
                else:
                    st.error("❌ Gagal mengirim pesan.")

