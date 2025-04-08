from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt = st.text_area("Define your AI Agent:", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","llama-3.1-8b-instant"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

selected_model = st.selectbox(
    "Select Model:",
    MODEL_NAMES_GROQ if provider == "Groq" else MODEL_NAMES_OPENAI
)

allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything!")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {data}")

