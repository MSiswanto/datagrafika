import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
from datetime import datetime

# ===========================
# Page config
# ===========================
st.set_page_config(
    page_title="Portfolio Data Science",
    page_icon="📊",
    layout="wide"
)

# ===========================
# Sidebar CSS & navigation
# ===========================
st.sidebar.markdown("""
<style>
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #4B8BBE;
    margin-bottom: 10px;
}
.sidebar-box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

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

# ===========================
# Page title
# ===========================
st.markdown("<div class='main-title'>👨‍💻 Data Science Portfolio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore our projects and latest insights in Data Science and AI</div>", unsafe_allow_html=True)

# ===========================
# Sidebar navigation
# ===========================
st.sidebar.markdown('<div class="sidebar-title">Navigasi</div>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    menu = st.sidebar.radio("", ["🏠 Home", "📂 Projects", "📰 Blog", "📞 Contact"])
    st.markdown('</div>', unsafe_allow_html=True)

# ===========================
# Pages
# ===========================
if menu == "🏠 Home":
    st.subheader("Selamat datang di DGrafika!")
    st.markdown("""
    <div style='
        text-align: justify;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #ddd;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        font-size: 18px;
        line-height: 1.6;
    '>
      <h3 style='text-align: center; color: #4B8BBE;'>About Us</h3>

      <p style='text-align: justify; font-size: 18px; line-height: 1.7;'>
          🚀 <strong>Startup kami bergerak dalam bidang Data Science.</strong><br>
          Kami menangani berbagai proyek terkait AI dan data science seperti data cleaning, data analysis, dan visualisasi data.<br>
          Di website ini, Anda dapat menelusuri berbagai proyek kami — mulai dari prediksi dropout, analisis e-commerce dengan berbagai algoritma machine learning dan deep learning, hingga eksperimen dengan model generatif terbaru, serta proyek NLP (sentiment analysis) dan Computer Vision.
      </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.subheader("📫 Hubungi Saya")
    st.markdown("""
    📍 Location : East Java, Indonesia  
    📧 Email   : [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
    💼 LinkedIn: [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
    🐙 GitHub  : [github.com/MSiswanto](https://github.com/MSiswanto)
""")

elif menu == "📂 Projects":
    st.subheader("📁 Project List")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🎓 Dropout Prediction")
        st.write("Model machine learning untuk memprediksi risiko mahasiswa dropout berdasarkan data akademik.")
        st.markdown("[View Project](https://dropout-prediction-detection.streamlit.app/)")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛒 E-commerce Data Analysis")
        st.write("Analisis data transaksi e-commerce untuk mendapatkan insight tren dan perilaku konsumen.")
        st.markdown("[View Project](https://analysis-brazilianecommerce.streamlit.app/)")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "📰 Blog":
    st.subheader("🧠 Artikel")
    st.markdown("""
    Berikut beberapa topik yang sedang hangat di dunia data science:

    - 🔍 **RAG (Retrieval-Augmented Generation)** semakin populer di NLP.
    - 📊 **AutoML** tools semakin memudahkan eksperimen.
    - 🤖 **LLMs** terus berevolusi dengan model seperti GPT-4o.
    - 🧠 **Prompt engineering** kini menjadi keterampilan wajib untuk praktisi AI.
    
    *(Coming soon: artikel-artikel mendalam di bagian ini.)*
    """)

elif menu == "📞 Contact":
    st.title("📞 Contact Us")
    st.markdown("""
    Terima kasih telah mengunjungi portofolio kami. Silakan hubungi kami melalui kontak di bawah ini:

    **📧 Email:** [msiswanto@gmail.com](mailto:msiswanto@gmail.com)  
    **💼 LinkedIn:** [linkedin.com/in/meilanasiswanto](https://linkedin.com/in/meilanasiswanto)  
    **🐙 GitHub:** [github.com/MSiswanto](https://github.com/MSiswanto) 
    **🌐 Website:** [meilana.dev](https://grafika.streamlit.app/)
    """)

# ===========================
# ===========================
# Premium Floating Chat
# ===========================
# ===========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

def simple_ai(prompt):
    prompt_lower = prompt.lower()
    if "halo" in prompt_lower or "hi" in prompt_lower:
        return "Halo! Senang bertemu denganmu. 😊"
    elif "nama" in prompt_lower:
        return "Saya chatbot portofolio DGrafika."
    elif "data science" in prompt_lower:
        return "DGrafika menangani proyek AI, Data Science, NLP, dan Computer Vision."
    else:
        return "Maaf, saya belum bisa menjawab itu. 😅"

toggle_button = st.empty()
if toggle_button.button("💬 Chat"):
    st.session_state.chat_open = not st.session_state.chat_open

if st.session_state.chat_open:
    chat_container = st.container()
    with chat_container:
        st.markdown("""
        <style>
        .floating-chat {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            max-height: 450px;
            background-color: white;
            border: 2px solid #25D366;
            border-radius: 12px;
            padding: 10px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.25);
            z-index: 9999;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        .floating-chat-header {
            font-weight: bold;
            color: #25D366;
            text-align: center;
            margin-bottom: 5px;
        }
        .chat-bubble {
            padding: 8px;
            margin: 5px 0;
            border-radius: 12px;
            max-width: 80%;
            animation: slideIn 0.3s ease-in-out;
        }
        .user { background-color: #DCF8C6; align-self: flex-end; }
        .assistant { background-color: #F1F0F0; align-self: flex-start; }
        @keyframes slideIn {
            from {opacity: 0; transform: translateY(10px);}
            to {opacity: 1; transform: translateY(0);}
        }
        </style>
        <div class="floating-chat">
            <div class="floating-chat-header">💬 Chat with AI</div>
        </div>
        """, unsafe_allow_html=True)

        # Display chat history
        for msg in st.session_state.chat_history:
            role_class = "user" if msg["role"] == "user" else "assistant"
            st.markdown(f"<div class='chat-bubble {role_class}'>{msg['content']}<br><small>{msg['time']}</small></div>", unsafe_allow_html=True)

        if prompt := st.chat_input("Type your message..."):
            timestamp = datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append({"role": "user","content": prompt,"time": timestamp})
            ai_response = simple_ai(prompt)
            st.session_state.chat_history.append({"role": "assistant","content": ai_response,"time": datetime.now().strftime("%H:%M")})
            st.experimental_rerun()
