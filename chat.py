import streamlit as st
from tavily import TavilyClient
import google.generativeai as genai
import re

# API keys and configuration
GEMINI_API = "AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk"
TAVILY_API = "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"

genai.configure(api_key=GEMINI_API)
tavily = TavilyClient(api_key=TAVILY_API)

st.write("Developed by Upendra Chowdary VITB")
st.title("Farmer's Real-Time AI Chat")

# Display a welcome message
marquee_message = "Welcome to the Farmer's AI Chat! Ask your farming-related questions below."
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)

# Input for user's query
query = st.text_input("Enter your farming-related query")

# AI Model for generating farming-related content
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    system_instruction=(
        "You are an AI assistant designed to help farmers. For any farming-related query, "
        "provide practical advice, information about crops, farming techniques, market prices, and other "
        "agriculture-related topics."
    )
)

def search(query):
    # Perform basic search using TavilyClient without domain filtering
    try:
        return tavily.get_search_context(query)
    except Exception as e:
        st.error(f"Error fetching data from Tavily: {e}")
        return None


if st.button("Submit"):
    # Search and get response from Tavily
    response = search(query)
    
    # Generate farming-related content using the AI model
    answer = model.generate_content(response)
    st.markdown(answer.text)
    
    # Display results from Google and Wikipedia
    st.subheader("Additional Search Results:")
    
    if 'google.com' in response:
        st.write("Google Search Results:")
        google_results = re.findall(r'(https?://(?:www\.)?google\.com[^"]+)', response)
        for result in google_results:
            st.write(f"[Google Result]({result})")
    
    if 'wikipedia.org' in response:
        st.write("Wikipedia Search Results:")
        wikipedia_results = re.findall(r'(https?://(?:www\.)?wikipedia\.org[^"]+)', response)
        for result in wikipedia_results:
            st.write(f"[Wikipedia Result]({result})")
