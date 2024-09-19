import streamlit as st
import google.generativeai as genai
import pytesseract
import cv2
from PIL import Image

# Configure API key
genai.configure(api_key="AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk")

# Initialize model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Streamlit UI
st.title("AI Code Generator")

# Choose between text input or camera input
input_choice = st.radio("How would you like to provide the input?", ("Text Input", "Image Input"))

problem = ""

if input_choice == "Text Input":
    # User input for the problem description (text-based)
    problem = st.text_input("Enter problem description")

elif input_choice == "Image Input":
    # Capture image from camera
    uploaded_image = st.camera_input("Capture an image of the question")

    if uploaded_image is not None:
        # Convert to PIL image
        img = Image.open(uploaded_image)
        
        # Perform OCR using pytesseract
        problem = pytesseract.image_to_string(img)

        # Display the extracted text for the user to verify
        st.write("Extracted text from image:")
        st.text_area("", problem)

# Allow user to select the programming language
language = st.selectbox("Select programming language", ["Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])

# Generate the code when the user clicks the button
if st.button("Generate Code"):
    if problem:
        try:
            # Construct the prompt
            prompt = f"Create a program in {language} for the following problem: {problem}. Provide the code in a simple manner with fewer lines of code."
            
            # Generate the response
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
                system_instruction="You are an expert coder. Help me to learn coding."
            )
            response = model.generate_content(prompt)
            code_text = response.text
            
            # Display the generated code
            st.subheader(f"Generated {language} Code")
            st.code(code_text, language=language.lower())
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide a valid problem description.")
