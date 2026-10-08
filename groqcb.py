import streamlit as st
from groq import Groq

# ---------------------------------------
# PAGE SETTINGS
# ---------------------------------------

st.set_page_config(
    page_title="Jhansi's AIbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------------------
# GROQ API KEY
# ---------------------------------------

GROQ_API_KEY = "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"

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)

# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("🤖 Groq AI Chatbot")
st.write("Ask anything and chat with Groq AI!")

# ---------------------------------------
# CHAT HISTORY
# ---------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------
# DISPLAY PREVIOUS MESSAGES
# ---------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------
# USER INPUT
# ---------------------------------------

user_message = st.chat_input("Type your message here...")

# ---------------------------------------
# SEND MESSAGE
# ---------------------------------------

if user_message:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # Get response from Groq
    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages
        )

        bot_response = response.choices[0].message.content

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response
        })

    except Exception as e:

        st.error(f"Error: {e}")

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

with st.sidebar:

    st.header("⚙️ Chat Settings")

    st.write("### About")

    st.write(
        """
        This chatbot uses:

        🤖 Groq LLM  
        🐍 Python  
        🎈 Streamlit  

        Your conversation is maintained
        during the current session.
        """
    )

    # Clear conversation button
    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()
