import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an expert coder. Help me to learn coding."
)

# Streamlit UI
st.title("AI Code Converter")

# User inputs for the source code and programming languages
source_code = st.text_area("Enter the source code")
source_language = st.selectbox("Select source programming language", ["Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])
target_language = st.selectbox("Select target programming language", ["Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])

# Generate the code when the user clicks the button
if st.button("Convert Code"):
    try:
        # Construct the prompt
        prompt = f"Convert the following {source_language} code to {target_language} code:\n\n{source_code}"
        
        # Generate the response
        response = model.generate_content(prompt)
        converted_code = response.text
        
        # Display the converted code
        st.subheader(f"Converted {target_language} Code")
        st.code(converted_code, language=target_language.lower())
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
