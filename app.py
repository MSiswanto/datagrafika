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
import streamlit.components.v1 as components

# ===========================
# Session state
# ===========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# ===========================
# Floating chat button
# ===========================
if st.button("💬", key="chat_button"):
    st.session_state.chat_open = not st.session_state.chat_open

# ===========================
# CSS for chat
# ===========================
st.markdown('''
<style>
.chat-container {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 350px;
    height: 450px;
    background-color: white;
    border: 2px solid #25D366;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    z-index: 9999;
}
.chat-header {
    background-color: #25D366;
    color: white;
    padding: 10px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: move;
}
.chat-messages {
    padding: 10px;
    flex: 1;
    overflow-y: auto;
    background-color: #e5ddd5;
    display: flex;
    flex-direction: column;
}
.chat-bubble {
    padding: 10px;
    border-radius: 15px;
    margin-bottom: 8px;
    max-width: 80%;
    word-wrap: break-word;
    font-size: 14px;
}
.user { background-color: #DCF8C6; align-self: flex-end; }
.ai { background-color: #F1F0F0; align-self: flex-start; }
.timestamp { font-size: 10px; color: gray; margin-top: 2px; text-align: right; }
</style>
''', unsafe_allow_html=True)

# ===========================
# Render chat
# ===========================
if st.session_state.chat_open:
    chat_box = st.container()
    with chat_box:
        st.markdown('<div class="chat-container" id="chat-container">', unsafe_allow_html=True)

        # Header with close button
        st.markdown('''
        <div class="chat-header" id="chat-header">
            Chat AI
            <button id="chat-close" style="background:none;border:none;color:white;font-size:16px;cursor:pointer;">✖</button>
        </div>
        ''', unsafe_allow_html=True)

        # Messages
        messages_box = st.container()
        with messages_box:
            for chat in st.session_state.chat_history:
                role_class = "user" if chat["role"]=="user" else "ai"
                timestamp = chat.get("time","")
                st.markdown(f'''
                    <div class="chat-bubble {role_class}">
                        {chat["content"]}
                        <div class="timestamp">{timestamp}</div>
                    </div>
                ''', unsafe_allow_html=True)

        # Chat input
        prompt = st.chat_input("Type your message...")
        if prompt:
            now = datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append({"role":"user","content":prompt,"time":now})
            response = f"AI reply to: {prompt}"  # replace with your AI call
            st.session_state.chat_history.append({"role":"assistant","content":response,"time":now})
            st.experimental_rerun()  # refresh chat immediately

# ===========================
# JS for draggable + close button + auto-scroll
# ===========================
components.html('''
<script>
const chatContainer = window.parent.document.getElementById("chat-container");
const chatHeader = window.parent.document.getElementById("chat-header");
const closeBtn = window.parent.document.getElementById("chat-close");
const chatMessages = chatContainer ? chatContainer.querySelector('.chat-messages') : null;

// Close chat
if (closeBtn){
    closeBtn.onclick = () => {
        window.parent.postMessage({func: "closeChat"}, "*");
    }
}

// Auto-scroll
if(chatMessages){
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Make draggable
if(chatContainer && chatHeader){
    chatHeader.onmousedown = function(event){
        let shiftX = event.clientX - chatContainer.getBoundingClientRect().left;
        let shiftY = event.clientY - chatContainer.getBoundingClientRect().top;

        function moveAt(pageX, pageY){
            chatContainer.style.left = pageX - shiftX + 'px';
            chatContainer.style.top = pageY - shiftY + 'px';
        }

        function onMouseMove(event){
            moveAt(event.pageX, event.pageY);
        }

        document.addEventListener('mousemove', onMouseMove);

        document.onmouseup = function(){
            document.removeEventListener('mousemove', onMouseMove);
            document.onmouseup = null;
        };
    };

    chatHeader.ondragstart = function() { return false; };
}
</script>
''', height=0)

# ===========================
# Listen for close button
# ===========================
params = st.experimental_get_query_params()
if st.session_state.get("chat_open") is False:
    st.experimental_rerun()
