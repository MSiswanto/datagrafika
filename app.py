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
    st.link_button("Open Project", "https://dropout-prediction-detection.streamlit.app/")
    st.image("https://lookerstudio.google.com/favicon.ico", width=40)
    st.link_button("View Dashboard", "https://lookerstudio.google.com/reporting/d93cb43d-d199-41c9-b088-566bf728d656/page/KdxKF")

with col2:
    st.header("📊 HR Attrition Dashboard")
    st.write("Interactive Looker Studio dashboard visualizing employee attrition trends.")
    st.image("https://lookerstudio.google.com/favicon.ico", width=40)
    st.link_button("View Dashboard", "https://lookerstudio.google.com/reporting/79ac12c1-f6b7-4cc1-a35d-e1906ae505d7/page/E9jJF")
    

# 🛒 Brazil E-Commerce Data Analysis
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn.pixabay.com/photo/2021/03/26/09/19/shopping-6125344_1280.png", use_container_width=True)

with col2:
    st.markdown("""
    ### 🛒 Brazil E-Commerce Data Analysis  
    **Unlocking Brazil E-Commerce: Data Insights & Dashboard**  
    Explore purchasing behaviors and customer patterns in one of the largest e-commerce markets in Latin America.  
    This project leverages **Python, Streamlit, and Plotly** to analyze **Olist’s public dataset**, revealing  
    key insights into sales trends, delivery performance, and customer satisfaction.

    **Highlights:**  
    - Cleaned and analyzed over **100K transactions** from Brazilian online retailers.  
    - Built an interactive **Streamlit dashboard** for data storytelling.  
    - Investigated **delivery delays and their impact on customer ratings**.  
    - Applied **product segmentation** to identify best-selling categories.  
    - Generated **business insights** to improve logistics efficiency.

    🔗 [View Live App](https://analysis-brazilianecommerce.streamlit.app/)
    """)

st.markdown("---")


# =========================================
# 📞 Contact Section
# =========================================
st.markdown("---")
st.header("📩 Contact")
st.write("Reach me via [LinkedIn](https://www.linkedin.com/in/meilanasiswanto/) | [GitHub](https://github.com/MSiswanto)")

# =========================================
# 💬 Floating Chatbot Section (Final Pro)
# =========================================
import streamlit as st
from datetime import datetime

# --- State initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# --- Simple AI logic
def simple_ai(prompt):
    prompt_lower = prompt.lower()
    if "halo" in prompt_lower or "hi" in prompt_lower:
        return "👋 Halo! Senang bertemu denganmu hari ini."
    elif "nama" in prompt_lower:
        return "Saya 🤖 chatbot portofolio DataGrafika."
    elif "project" in prompt_lower:
        return "📊 Saya bantu menampilkan proyek Data Science, AI, dan dashboard interaktif kamu."
    elif "terima kasih" in prompt_lower:
        return "🙏 Sama-sama! Senang bisa membantu."
    elif "data" in prompt_lower:
        return "🧠 DGrafika fokus pada AI, NLP, dan visualisasi data modern."
    else:
        return "✨ Maaf, saya belum paham pertanyaannya. Tapi saya akan terus belajar!"

# --- Floating chat button
toggle = st.button("💬 Chat", key="chat_toggle", help="Click to open/close chatbot")
if toggle:
    st.session_state.chat_open = not st.session_state.chat_open

# --- Show chat window
if st.session_state.chat_open:
    st.markdown("""
    <style>
    .floating-chat {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 350px;
        max-height: 480px;
        background-color: white;
        border: 2px solid #25D366;
        border-radius: 14px;
        padding: 10px 12px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.3);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        scroll-behavior: smooth;
        font-family: "Helvetica Neue", sans-serif;
    }
    .floating-chat-header {
        font-weight: 600;
        color: #25D366;
        text-align: center;
        font-size: 16px;
        margin-bottom: 6px;
    }
    .chat-bubble {
        padding: 8px 10px;
        margin: 5px 0;
        border-radius: 12px;
        max-width: 80%;
        word-wrap: break-word;
        line-height: 1.3;
        animation: fadeInUp 0.25s ease-in-out;
    }
    .user { background-color: #DCF8C6; align-self: flex-end; }
    .assistant { background-color: #F1F0F0; align-self: flex-start; }
    small { font-size: 10px; color: #555; }
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(8px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    <div class="floating-chat" id="chatbox">
        <div class="floating-chat-header">💬 Chat with DataGrafika</div>
    </div>
    """, unsafe_allow_html=True)

    # --- Display chat history
    for msg in st.session_state.chat_history:
        role_class = "user" if msg["role"] == "user" else "assistant"
        st.markdown(
            f"<div class='chat-bubble {role_class}'>{msg['content']}<br><small>{msg['time']}</small></div>",
            unsafe_allow_html=True
        )

    # --- Input
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
        st.session_state._chat_trigger = not st.session_state.get("_chat_trigger", False)
        st.rerun()

    # --- Auto-scroll to latest message
    st.markdown("""
    <script>
    var chatBox = document.getElementById('chatbox');
    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    </script>
    """, unsafe_allow_html=True)
