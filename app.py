import streamlit as st
from datetime import datetime
from PIL import Image
import pandas as pd
import plotly.express as px

# =========================================
# ⚙️ Konfigurasi Halaman
# =========================================
st.set_page_config(
    page_title="DGrafika Portfolio",
    page_icon="💡",
    layout="wide"
)

# =========================================
# 🎨 Header
# =========================================
st.title("💡 DataGrafika Portfolio")
st.write("Explore AI, Data Science, and Visualization Projects 🚀")

# =========================================
# 📁 Portfolio Section
# =========================================
col1, col2 = st.columns(2)
with col1:
    st.header("🧠 Dropout Prediction System")
    st.write("A Streamlit-based AI system to predict student dropout risk.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    st.link_button("Open Project", "https://grafika.streamlit.app")

with col2:
    st.header("📊 HR Attrition Dashboard")
    st.write("Interactive Looker Studio dashboard visualizing employee attrition trends.")
    st.image("https://lookerstudio.google.com/favicon.ico", width=40)
    st.link_button("View Dashboard", "https://lookerstudio.google.com/")

# =========================================
# 📞 Contact Section
# =========================================
st.markdown("---")
st.header("📩 Contact")
st.write("Reach me via [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/MSiswanto)")

# =========================================
# 💬 Floating Chatbot Section
# =========================================

# --- State initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# --- Simple AI logic
def simple_ai(prompt):
    prompt_lower = prompt.lower()
    if "halo" in prompt_lower or "hi" in prompt_lower:
        return "Halo! Senang bertemu denganmu. 😊"
    elif "nama" in prompt_lower:
        return "Saya chatbot portofolio DGrafika."
    elif "data" in prompt_lower:
        return "DGrafika mengerjakan proyek Data Science, AI, dan Machine Learning."
    elif "project" in prompt_lower:
        return "Beberapa proyek saya termasuk dropout prediction, HR analytics, dan AI dashboards."
    else:
        return "Terima kasih! Pertanyaanmu sudah saya catat. 😊"

# --- Floating chat button
toggle = st.button("💬 Chat", key="chat_toggle", help="Click to open/close chatbot")
if toggle:
    st.session_state.chat_open = not st.session_state.chat_open

# --- If chat opened
if st.session_state.chat_open:
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

    # --- Chat history
    for msg in st.session_state.chat_history:
        role_class = "user" if msg["role"] == "user" else "assistant"
        st.markdown(
            f"<div class='chat-bubble {role_class}'>{msg['content']}<br><small>{msg['time']}</small></div>",
            unsafe_allow_html=True
        )

    # --- Input box
    if prompt := st.chat_input("Type your message..."):
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt,
            "time": timestamp
        })
        ai_response = simple_ai(prompt)
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": ai_response,
            "time": datetime.now().strftime("%H:%M")
        })
        # ✅ Rerun safely using new Streamlit API
        st.session_state._chat_trigger = not st.session_state.get("_chat_trigger", False)
        st.rerun()
