import streamlit as st

# -------------------------------
# 🧠 Basic Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Chatbot Assistant",
    page_icon="🤖",
    layout="centered",
)

# -------------------------------
# 💬 Title and Intro
# -------------------------------
st.title("🤖 AI Chatbot Assistant")
st.caption("Your intelligent assistant powered by GPT-4o-mini")

# -------------------------------
# 🧠 Initialize Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there 👋! How can I help you today?"}
    ]

# -------------------------------
# 🧱 Display Chat History
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# 💬 Input Box for User Message
# -------------------------------
if prompt := st.chat_input("Type your message here..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # -------------------------------
    # 🧠 Generate Assistant Reply
    # -------------------------------
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Gunakan model OpenAI GPT bawaan Streamlit
                from openai import OpenAI
                client = OpenAI()
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"⚠️ Oops, something went wrong: {e}"

            st.markdown(reply)

    # Simpan pesan ke session state
    st.session_state.messages.append({"role": "assistant", "content": reply})

# -------------------------------
# ⚙️ Footer / Clear Chat Option
# -------------------------------
st.markdown("---")
if st.button("🗑️ Clear conversation"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Conversation cleared. How can I assist you now?"}
    ]
    st.rerun()
