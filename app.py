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

# ===========================
# 💬 Mini Floating Chatbot
# ===========================
import streamlit.components.v1 as components

# ===========================
# Session state
# ===========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# ===========================
# CSS
# ===========================
st.markdown('''
<style>
.chat-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #25D366;
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    font-size: 28px;
    cursor: pointer;
    z-index: 9999;
    transition: transform 0.2s;
}
.chat-btn:hover { transform: scale(1.1); }
.chat-container {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 350px;
    height: 450px;
    background-color: white;
    border: 2px solid #25D366;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.25);
    z-index: 9998;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
}
.chat-header {
    background-color: #25D366;
    color: white;
    padding: 10px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    cursor: move;
}
.chat-messages {
    padding: 10px;
    flex: 1;
    overflow-y: auto;
    background-color: #f5f5f5;
}
.chat-input { padding: 10px; border-top: 1px solid #ddd; }
</style>
''', unsafe_allow_html=True)

# ===========================
# Floating chat button
# ===========================
if st.button("💬", key="chat_button"):
    st.session_state.chat_open = not st.session_state.chat_open

# ===========================
# Floating chat container
# ===========================
if st.session_state.chat_open:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Header with close button
    st.markdown('''
    <div class="chat-header">
        Chat AI
        <button id="chat-close" style="background:none;border:none;color:white;font-size:16px;cursor:pointer;">✖</button>
    </div>
    ''', unsafe_allow_html=True)

    # Messages
    st.markdown('<div class="chat-messages" id="chat-messages">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        bg = "#DCF8C6" if chat["role"]=="user" else "#F1F0F0"
        align = "right" if chat["role"]=="user" else "left"
        st.markdown(f'''
            <div style="background:{bg}; padding:8px; border-radius:8px; margin-bottom:5px; text-align:{align};">
                {chat["content"]}
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Chat input
    prompt = st.chat_input("Type your message...")
    if prompt:
        st.session_state.chat_history.append({"role":"user", "content":prompt})
        response = f"AI reply to: {prompt}"  # Replace with OpenAI/GPT API call
        st.session_state.chat_history.append({"role":"assistant", "content":response})
        st.experimental_rerun()  # auto-refresh

# ===========================
# JavaScript: handle X and auto-scroll
# ===========================
components.html('''
<script>
const closeBtn = window.parent.document.getElementById("chat-close");
if (closeBtn){
    closeBtn.onclick = () => {
        window.parent.postMessage({func: "closeChat"}, "*");
    }
}
// Auto-scroll
const chatMessages = window.parent.document.getElementById("chat-messages");
if(chatMessages){
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
</script>
''', height=0)

# ===========================
# Handle X button click
# ===========================
st.experimental_get_query_params()  # needed to trigger rerun
if st.session_state.get("chat_open") is False:
    st.experimental_rerun()
