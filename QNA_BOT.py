from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.5
)
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: #e5e7eb;
}


.block-container {
    max-width: 900px;
    padding-top: 3rem;
}


h1 {
    text-align: center;
    font-weight: 700;
    letter-spacing: 1px;
}


.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 2rem;
}


.stChatMessage {
    border-radius: 16px;
    padding: 8px;
}


[data-testid="stChatMessage-user"] {
    background-color: #1f2937;
}


[data-testid="stChatMessage-assistant"] {
    background-color: #020617;
    border: 1px solid #1f2937;
}


textarea {
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)






st.markdown("""
<h1>👾 BuddyAI</h1>
<p class="subtitle">Your friendly AI companion · Ask anything</p>
""", unsafe_allow_html=True)


if st.button("🗑 Clear chat"):
    st.session_state.messages = []
    st.rerun()



with st.container():
    st.markdown("### 💬 Chat")


if "messages" not in st.session_state:
    
    st.session_state.messages = []

for messages in st.session_state.messages:
    role = messages["role"]
    content = messages["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything")

History =[]



if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)

    for msg in st.session_state.messages:
        if msg["role"]=="user":
            History.append(HumanMessage(content=msg["content"]))
        else:
            History.append(AIMessage(content=msg["content"]))

    res = llm.invoke(History)
    st.chat_message('ai').markdown(res.content)
    st.session_state.messages.append({"role":"ai","content":res.content})







