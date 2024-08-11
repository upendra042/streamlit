import streamlit as st
from tavily import TavilyClient
import google.generativeai as genai
import re

GEMINI_API = "AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk"
TAVILY_API = "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"

genai.configure(api_key=GEMINI_API)
tavily = TavilyClient(api_key=TAVILY_API)

marquee_message = "<span style='color: green; font-size: 20px; font-weight: bold;'>Developed by upendra chøwdary VITB"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)


st.title("Real Time AI")

marquee_message = "Welcome to Real Time AI - Enter your query below to get started!"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)

query = st.text_input("Enter your query")

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are a helpful assistant. For any given query, provide a brief and summary of the topic and include relevant YouTube links for learning more about it. Ensure the YouTube links are educational and appropriate for the topic.")

prompt = (f"generate the present working youtube links based on the {query} given along with the some summary about {query}. ")

def search(query):
    return tavily.get_search_context(query,include_domains=["youtube.com", "wikipedia.org", "google.com"])

def extract_youtube_links(text):
    # Regular expression to find YouTube video IDs
    youtube_regex = r'(?:https?://(?:www\.)?youtube\.com/watch\?v=|https?://youtu\.be/)([\w-]+)'
    video_ids = re.findall(youtube_regex, text)

    # Construct full YouTube links
    youtube_links = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

    return youtube_links

if st.button("Submit"):
    response = search(query)
    answer = model.generate_content(response)
    
    st.markdown(answer.text)
    
    # Debugging: Print the raw response
    st.write(f"Raw Response: {answer.text}")
    
    # Extract and display YouTube links
    youtube_links = extract_youtube_links(answer.text)
    
    if not youtube_links:
        st.warning("No YouTube links found in the response.")
    
    for link in youtube_links:
        st.write(f"Extracted YouTube link: {link}")  # Debugging step
        st.video(link)
    # Display results from Google and Wikipedia
    st.subheader("Search Results:")
    
    # Display results for Google and Wikipedia
    if 'google.com' in response:
        st.write("Google Search Results:")
        # Extract Google search results
        google_results = re.findall(r'(https?://(?:www\.)?google\.com[^"]+)', response)
        for result in google_results:
            st.write(f"[Google Result]({result})")
    
    if 'wikipedia.org' in response:
        st.write("Wikipedia Search Results:")
        # Extract Wikipedia search results
        wikipedia_results = re.findall(r'(https?://(?:www\.)?wikipedia\.org[^"]+)', response)
        for result in wikipedia_results:
            st.write(f"[Wikipedia Result]({result})")
 
