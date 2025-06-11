import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np

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
st.markdown("<div class='subtitle'>Explore my projects and latest insights in Data Science and AI</div>", unsafe_allow_html=True)

# Menu Navigasi
menu = st.sidebar.radio("Navigasi", ["🏠 Home", "📂 Projects", "📰 Blog", "📞 Contact"])


# Halaman Home
if menu == "🏠 Home":
    st.subheader("Selamat datang di portofolio saya!")
    st.write("""
        Saya adalah praktisi data dengan minat dalam machine learning, analisis data, dan visualisasi interaktif.
        Di website ini, Anda dapat menelusuri berbagai proyek saya, mulai dari prediksi dropout, analisis e-commerce,
        hingga eksperimen dengan model generatif terbaru.
    """)
    st.markdown("---")
    st.subheader("📫 Hubungi Saya")

    st.markdown("""
    📍 Lokasi: East Java, Indonesia  
    📧 Email: [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
    💼 LinkedIn: [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
    🐙 GitHub: [github.com/meilana](https://github.com/MSiswanto)
""")


# Halaman Projects
elif menu == "📂 Projects":
    st.subheader("📁 Daftar Proyek")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🎓 Dropout Prediction")
        st.write("Model machine learning untuk memprediksi risiko mahasiswa dropout berdasarkan data akademik.")
        st.link_button("Lihat Proyek", "https://dropout-prediction-detection.streamlit.app/")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛒 E-commerce Data Analysis")
        st.write("Analisis data transaksi e-commerce untuk mendapatkan insight tren dan perilaku konsumen.")
        st.link_button("Lihat Proyek", "https://analysis-brazilianecommerce.streamlit.app/")  # Ganti dengan URL kamu
        st.markdown("</div>", unsafe_allow_html=True)

# Halaman Blog
elif menu == "📰 Blog":
    st.subheader("🧠 Artikel & Update Algoritma")
    st.markdown("""
    Berikut beberapa topik yang sedang hangat di dunia data science:

    - 🔍 **RAG (Retrieval-Augmented Generation)** semakin populer di NLP.
    - 📊 **AutoML** tools seperti Google VertexAI dan H2O.ai semakin memudahkan eksperimen.
    - 🤖 **LLMs** terus berevolusi dengan model seperti Claude, Gemini, dan GPT-4o.
    - 🧠 **Prompt engineering** kini menjadi keterampilan wajib untuk praktisi AI.
    
    *(Coming soon: artikel-artikel mendalam di bagian ini.)*
    """)

# Halaman Kontak
elif menu == "📞 Kontak":
    #st.title("📞 Kontak Kami")
    st.subheader("📞 Kontak Kami")
    st.markdown("""
    Terima kasih telah mengunjungi portofolio kami.  
    Jangan ragu untuk menghubungi saya melalui saluran berikut:

    - 📧 Email: [msiswanto@gmail.com](mailto:msiswanto@gmail.com)
    - 💼 LinkedIn: [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)
    - 🐙 GitHub: [github.com/MSiswanto](https://github.com/MSiswanto)
    - 🌐 Website: [meilana.dev](https://https://grafika.streamlit.app/)
    """)
with st.form("contact_form"):
    st.text_input("Nama")
    st.text_input("Email")
    st.text_area("Pesan")
    submitted = st.form_submit_button("Kirim")
    if submitted:
        st.success("✅ Pesan berhasil dikirim! (simulasi)")


