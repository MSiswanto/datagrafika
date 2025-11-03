import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import requests

# ===========================
# 🚨 Konfigurasi Halaman
# ===========================
st.set_page_config(
    page_title="Portfolio Data Science",
    page_icon="📊",
    layout="wide"
)

# ===========================
# CSS Kustom
# ===========================
st.markdown('''
<style>
/* Sidebar */
.sidebar-title { font-size:24px; font-weight:bold; color:#4B8BBE; margin-bottom:10px; }
.sidebar-box { background-color:#f0f2f6; padding:15px; border-radius:10px; border:1px solid #ccc; }

/* Main Title & Subtitle */
.main-title { font-size:48px; font-weight:bold; color:#2C3E50; text-align:center; margin-bottom:30px; }
.subtitle { font-size:24px; color:#7F8C8D; text-align:center; margin-bottom:50px; }

/* Card */
.card { background-color:#F9F9F9; padding:20px; border-radius:10px; box-shadow:2px 2px 12px rgba(0,0,0,0.1); margin-bottom:20px; }
</style>
''', unsafe_allow_html=True)

# ===========================
# Sidebar
# ===========================
st.sidebar.markdown('<div class="sidebar-title">Navigasi</div>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    menu = st.radio("", ["🏠 Home", "📂 Projects", "📰 Blog", "📞 Contact"])
    st.markdown('</div>', unsafe_allow_html=True)

# ===========================
# Halaman Home
# ===========================
if menu == "🏠 Home":
    st.markdown("<div class='main-title'>👨‍💻 Data Science Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore our projects and latest insights in Data Science and AI</div>", unsafe_allow_html=True)

    st.subheader("Selamat datang di DGrafika!")
    st.markdown('''
<div style='text-align: justify; background-color: #ffffff; padding: 25px; border-radius: 10px;
            border: 1px solid #ddd; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-bottom:20px;
            font-size:18px; line-height:1.6;'>
  <h3 style='text-align:center; color:#4B8BBE;'>About Us</h3>
  <p style='text-align:justify; font-size:18px; line-height:1.7;'>
      🚀 <strong>Startup kami bergerak dalam bidang Data Science.</strong><br>
      Kami menangani berbagai proyek terkait AI dan data science seperti data cleaning, data analysis, dan visualisasi data.<br>
      Di website ini, Anda dapat menelusuri berbagai proyek kami — mulai dari prediksi dropout, analisis e-commerce, eksperimen model generatif terbaru, serta proyek NLP dan Computer Vision.
  </p>
</div>
''', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📫 Hubungi Saya")
    st.markdown('''
📍 Location : East Java, Indonesia  
📧 Email   : [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
💼 LinkedIn: [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
🐙 GitHub  : [github.com/MSiswanto](https://github.com/MSiswanto)
''')

# ===========================
# Halaman Projects
# ===========================
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
        st.link_button("View Project", "https://analysis-brazilianecommerce.streamlit.app/")
        st.markdown("</div>", unsafe_allow_html=True)

# ===========================
# Halaman Blog
# ===========================
elif menu == "📰 Blog":
    st.subheader("🧠 Artikel")
    st.markdown('''
Berikut beberapa topik yang sedang hangat di dunia data science:

- 🔍 RAG (Retrieval-Augmented Generation)
- 📊 AutoML tools seperti Google VertexAI dan H2O.ai
- 🤖 LLMs (Claude, Gemini, GPT-4o)
- 🧠 Prompt engineering
''')

    for title, desc in [
        ("🔍 Memahami Overfitting dan Cara Mengatasinya",
         "Overfitting adalah salah satu tantangan utama dalam pembuatan model ML. Artikel ini membahas penyebab, tanda-tanda, dan solusi untuk menghindari overfitting."),
        ("📊 Exploratory Data Analysis (EDA) yang Efektif",
         "Bagaimana cara mengeksplorasi data sebelum modeling? Di artikel ini saya membahas teknik EDA praktis, tools visualisasi, dan insight dari data e-commerce.")
    ]:
        st.markdown(f'''
<div style='border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:20px; background-color:#fefefe;'>
    <h4>{title}</h4>
    <p>{desc}</p>
    <a href="#" target="_blank">📖 Baca Selengkapnya</a>
</div>
''', unsafe_allow_html=True)

# ===========================
# Halaman Contact
# ===========================
elif menu == "📞 Contact":
    st.title("📞 Contact Us")
    st.markdown('''
Terima kasih telah mengunjungi portofolio kami. Silakan hubungi kami melalui kontak di bawah ini:
**📧 Email:** [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
**💼 LinkedIn:** [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
**🐙 GitHub:** [github.com/MSiswanto](https://github.com/MSiswanto) 
**🌐 Website:** [meilana.dev](https://grafika.streamlit.app/)
''')

import streamlit as st
from datetime import datetime

# ===========================
# Session state initialization
# ===========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ===========================
# Chat widget (collapsible)
# ===========================
with st.expander("💬 Chat with AI Assistant", expanded=False):
    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input box
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt,
            "time": datetime.now().strftime("%H:%M")
        })
        with st.chat_message("user"):
            st.write(prompt)

        # AI response (replace with your model/API call)
        ai_response = f"AI reply to: {prompt}"  # <-- replace with OpenAI/Gemini/etc.
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": ai_response,
            "time": datetime.now().strftime("%H:%M")
        })
        with st.chat_message("assistant"):
            st.write(ai_response)

# ===========================
# Optional: custom CSS to make it look modern
# ===========================
st.markdown("""
<style>
/* Chat bubble colors */
.stChatMessage.user { background-color: #DCF8C6 !important; border-radius: 15px; padding: 8px; }
.stChatMessage.assistant { background-color: #F1F0F0 !important; border-radius: 15px; padding: 8px; }

/* Expander header */
.css-1r6slb0 { font-weight: bold; font-size: 16px; color: #25D366; }  /* adjust class if needed */
</style>
""", unsafe_allow_html=True)



   
   
