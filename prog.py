import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="Enter your api key")

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
    system_instruction="You are an expert coder. Help me to learn coding and help me to learn Python."
)

# Streamlit UI
st.title("AI Python Code Generator")

# User input for the problem description
problem = st.text_input("Enter problem description")

# Generate the Python code when the user clicks the button
if st.button("Generate Python Code"):
    try:
        # Construct the prompt
        prompt = f"Create a Python program for the following problem: {problem}."
        
        # Generate the response
        response = model.generate_content(prompt)
        code_text = response.text
        
        # Display the generated code
        st.subheader("Generated Python Code")
        st.code(code_text, language='python')
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
