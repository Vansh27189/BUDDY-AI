# 👾 BuddyAI – Streamlit Chatbot with LangChain & Gemini

BuddyAI is a simple yet powerful AI chatbot built using **Streamlit**, **LangChain**, and **Google Gemini**.  
It supports **context-aware conversations** by storing chat history and sending it back to the model on every user interaction.

---

## 🚀 Features

- 💬 Chat-style interface using Streamlit
- 🧠 Conversation memory using `st.session_state`
- 🔗 LangChain integration for structured LLM calls
- ⚡ Google Gemini (fast & efficient)
- ♻️ Persistent chat history across reruns
- 🌐 Deployable on Render / Streamlit Cloud

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Google Gemini API**# 👾 BuddyAI — AI Chatbot with Memory

**BuddyAI** is a conversational AI chatbot built using **Streamlit**, **LangChain**, and **Google Gemini**.  
It provides a clean chat interface with **persistent conversation memory**, allowing users to have natural, context-aware conversations.

🔗 **Try it live:**  
👉 https://buddy-ai-vansh.streamlit.app/

---

## ✨ Features

- 💬 Modern chat-style interface
- 🧠 Conversation memory using Streamlit `session_state`
- 🔗 LangChain for structured LLM interaction
- ⚡ Google Gemini (fast, low-latency responses)
- ♻️ Chat history persists across app reruns
- 🌐 Deployed and publicly accessible

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Google Gemini API**
- **python-dotenv**

---

## 📂 Project Structure

```
AI-BUDDY/
├── QNA_BOT.py          # Main Streamlit application
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignored files (env, venv, cache)
└── .env               # Local environment variables (not pushed)
```

---

## 🔐 Environment Variables

Create a `.env` file locally:

```env
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ **Do not upload `.env` to GitHub.**  
For deployment, environment variables are configured on the hosting platform.

---

## ▶️ Run Locally

### 1️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the app
```bash
streamlit run QNA_BOT.py
```

---

## 🧠 How Conversation Memory Works

- `st.session_state` is a **dictionary** that persists across Streamlit reruns.
- The key `"messages"` stores a **list of dictionaries**, each representing a chat message:

```python
{"role": "user", "content": "Hello"}
{"role": "assistant", "content": "Hi! How can I help you?"}
```

- Before calling the Gemini model, this list is converted into LangChain message objects.
- This allows the AI to **remember previous messages** and respond with context.

---

## 🌍 Live Demo

You can try BuddyAI here without any setup:

👉 **https://buddy-ai-vansh.streamlit.app/**

---

## 🚀 Future Enhancements

- Streaming responses
- Clear chat button
- System prompt customization
- RAG (PDF / document-based chatbot)
- Enhanced UI animations and themes

---

## 👤 Author

Built by **Vansh**  
A learning-focused project exploring modern AI application development with LangChain and Streamlit.

---

## 📜 License

This project is intended for educational and personal use.

- **python-dotenv**

---

## 📂 Project Structure

