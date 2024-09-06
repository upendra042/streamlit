import streamlit as st
import google.generativeai as genai
import re

# API keys and configuration
GEMINI_API = "AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk"
genai.configure(api_key=GEMINI_API)

# Define the AI model
model = genai.GenerativeModel(model_name="gemini-1.5-flash", 
                              system_instruction="You are a knowledgeable farming assistant. Provide accurate and helpful responses to farming-related queries in the same language as the input.")

st.title("Real-Time Farming AI Chat")

# Display marquees
marquee_message = "<span style='color: green; font-size: 20px; font-weight: bold;'>Developed by Upendra Chøwdary VITB</span>"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)

marquee_message = "Welcome to Real-Time Farming AI Chat - Enter your message below to chat!"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)

# Custom CSS for chat bubbles
st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            max-width: 600px;
            margin: auto;
            padding: 10px;
        }
        .chat-bubble {
            display: inline-block;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            max-width: 80%;
        }
        .user-message {
            background-color: #0078FF;
            color: white;
            align-self: flex-end;
        }
        .ai-response {
            background-color: #E5E5EA;
            color: black;
            align-self: flex-start;
        }
        .chat-input {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
        .chat-input input {
            width: 80%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .chat-input button {
            width: 18%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #0078FF;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Chat history storage
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to get AI response
def get_ai_response(user_message):
    prompt = f"Farmer: {user_message}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text

# Display chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f'<div class="chat-bubble user-message">{message["text"]}</div>', unsafe_allow_html=True)
    elif message['role'] == 'ai':
        st.markdown(f'<div class="chat-bubble ai-response">{message["text"]}</div>', unsafe_allow_html=True)

# Input for new message
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Type your farming-related question or message:")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Add user's message to chat history
        st.session_state.messages.append({'role': 'user', 'text': user_input})

        # Get AI response and add to chat history
        ai_response = get_ai_response(user_input)
        st.session_state.messages.append({'role': 'ai', 'text': ai_response})

        # Clear the input field
        st.write("")
    elif submit_button:
        st.warning("Please enter a message before sending.")
