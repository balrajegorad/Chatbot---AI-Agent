# Chatbot---AI-Agent
Sure! Here's a clean, professional, and detailed `README.md` for your project:

---

# 🤖 Personalized AI Chatbot Agent using LangGraph

This project is a **personalized AI agent** built using **LangGraph**, **FastAPI**, and **Streamlit**, with support for **Groq** and **OpenAI** language models. It allows users to define custom agent behavior, interact through a simple UI, and optionally use real-time web search via **Tavily**.

---

## 🚀 Features

- 🔧 **Custom System Prompt** – Define your agent's personality and behavior.
- 🧠 **Multi-model Support** – Choose from Groq and OpenAI LLMs.
- 🌐 **Optional Web Search** – Enable real-time answers using Tavily.
- 💬 **Simple Chat UI** – Built with Streamlit for a fast, interactive interface.
- ⚡ **FastAPI Backend** – Handles API communication and model invocation.
- 🧩 **LangGraph Agent** – Uses a ReAct-based reasoning agent for advanced responses.

---

## 📁 Project Structure

```
├── ai_agent.py          # Core AI agent logic using LangGraph
├── backend.py           # FastAPI backend for handling chat requests
├── frontend.py          # Streamlit-based user interface
├── .env                 # Stores API keys (not committed to version control)
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ⚙️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/langgraph-ai-agent.git
   cd langgraph-ai-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up `.env` file** with your API keys (see above).

---

## 🖥️ Running the App

### 1. Start the FastAPI backend:
```bash
python backend.py
```
> This will start the server on `http://127.0.0.1:9999`

---

### 2. Run the Streamlit frontend:
```bash
streamlit run frontend.py
```

---

## 🧠 How It Works

- The user enters a system prompt, selects a model, and types a query.
- The frontend sends this input to the FastAPI backend.
- The backend invokes the appropriate LangGraph ReAct agent using:
  - A selected LLM (Groq or OpenAI)
  - A custom system prompt
  - Tavily search tool if enabled
- The final response from the agent is sent back and shown in the UI.

---

## 🧰 Tech Stack

- **LangGraph** – For ReAct-style AI agents
- **LangChain** – Model and tool abstraction
- **FastAPI** – Backend API
- **Streamlit** – Frontend UI
- **Tavily** – Optional web search tool
- **Groq / OpenAI** – Language models

---

## 📌 Future Improvements

- ✅ Chat history memory
- 🔒 Authentication for agent access
- 💾 Agent configuration saving
- 📄 PDF or document chat support

---

## 🧑‍💻 Author

Developed by [Balu Gorad]([https://your-website-or-linkedin.com](https://www.linkedin.com/in/balugorad/))
