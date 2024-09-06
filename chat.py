import streamlit as st
from tavily import TavilyClient
import google.generativeai as genai
import re
import googleapiclient.discovery

# API keys and configuration
GEMINI_API = "AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk"
TAVILY_API = "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"
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

genai.configure(api_key=GEMINI_API)
tavily = TavilyClient(api_key=TAVILY_API)

st.write("Developed by Upendra Chowdary VITB")
st.title("Real-Time AI Chat")

# Display marquees
marquee_message = "Welcome to Real-Time AI - Enter your query below to get started!"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)

query = st.text_input("Enter your query")

# YouTube API client setup
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_youtube(query):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=5
    )
    response = request.execute()
    return response

# AI Model for generating content
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are a helpful assistant. For any given query, provide a brief summary of the topic and include relevant YouTube links for learning more about it. Ensure the YouTube links are educational and appropriate for the topic.")

def search(query):
    # Perform search using TavilyClient
    return tavily.get_search_context(query, include_domains=["youtube.com", "wikipedia.org", "google.com"])

def extract_youtube_links(text):
    # Regular expression to find YouTube video IDs
    youtube_regex = r'(?:https?://(?:www\.)?youtube\.com/watch\?v=|https?://youtu\.be/)([\w-]+)'
    video_ids = re.findall(youtube_regex, text)
    youtube_links = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]
    return youtube_links

if st.button("Submit"):
    # Search and get response
    response = search(query)
    
    # Generate content using AI
    answer = model.generate_content(response)
    st.markdown(answer.text)
    
    # Extract and display YouTube links from AI response
    youtube_links = extract_youtube_links(answer.text)
    
    if youtube_links:
        st.subheader("YouTube Links:")
        for link in youtube_links:
            st.write(f"Extracted YouTube link: {link}")  # Debugging step
            st.video(link)
    else:
        # Perform YouTube search if no links are found
        st.warning("No YouTube links found in the response. Searching YouTube...")
        youtube_response = search_youtube(query)
        for item in youtube_response['items']:
            video_title = item['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            st.write(f"{video_title}: {video_url}")
            st.video(video_url)
    
    # Display results from Google and Wikipedia
    st.subheader("Search Results:")
    
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
