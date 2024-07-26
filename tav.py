import streamlit as st
from tavily import TavilyClient
import google.generativeai as genai

GEMINI_API = st.secrets["GEMINI"]
TAVILY_API = st.secrets["TAVILY"]


genai.configure(api_key=GEMINI_API)
tavily = TavilyClient(api_key=TAVILY_API)

st.title("Real Time AI")

query = st.text_input("Enter your query")

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are a helpful assistant that summarizes the given content and produce understandable course of events. Keep it short but informative in normal english")

def search(query):
    return tavily.qna_search(query)


if st.button("Submit"):
    response = search(query)
    
    answer = model.generate_content(response)
    print(type(answer))
    st.markdown(answer.text)
