import streamlit as st
from datetime import datetime, timedelta
import streamlit.components.v1 as components

# ===========================
# Session state
# ===========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

if "last_interaction" not in st.session_state:
    st.session_state.last_interaction = datetime.now()

if "new_message" not in st.session_state:
    st.session_state.new_message = False

# ===========================
# Floating chat button with indicator
# ===========================
button_label = "💬"
if st.session_state.new_message and not st.session_state.chat_open:
    button_label += " 🔴"

if st.button(button_label, key="chat_button"):
    st.session_state.chat_open = not st.session_state.chat_open
    st.session_state.new_message = False  # clear red dot
    st.session_state.last_interaction = datetime.now()

# ===========================
# Auto-collapse after 30 seconds
# ===========================
if st.session_state.chat_open and datetime.now() - st.session_state.last_interaction > timedelta(seconds=30):
    st.session_state.chat_open = False

# ===========================
# CSS
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
# Render floating chat
# ===========================
if st.session_state.chat_open:
    st.markdown('<div class="chat-container" id="chat-container">', unsafe_allow_html=True)

    # Header with close button
    st.markdown('''
    <div class="chat-header" id="chat-header">
        Chat AI
        <button id="chat-close" style="background:none;border:none;color:white;font-size:16px;cursor:pointer;">✖</button>
    </div>
    ''', unsafe_allow_html=True)

    # Messages
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
        # AI reply (replace with actual API call)
        response = f"AI reply to: {prompt}"
        st.session_state.chat_history.append({"role":"assistant","content":response,"time":now})
        st.session_state.last_interaction = datetime.now()
        st.experimental_rerun()

# ===========================
# New message indicator
# ===========================
if not st.session_state.chat_open:
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"]=="assistant":
        st.session_state.new_message = True

# ===========================
# JS draggable + close button
# ===========================
components.html('''
<script>
const chatContainer = window.parent.document.getElementById("chat-container");
const chatHeader = window.parent.document.getElementById("chat-header");
const closeBtn = window.parent.document.getElementById("chat-close");

// Close chat
if (closeBtn){
    closeBtn.onclick = () => {
        window.parent.postMessage({func: "closeChat"}, "*");
    }
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
