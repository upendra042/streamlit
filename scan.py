import streamlit as st
import google.generativeai as genai
from PIL import Image
import pytesseract

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
    system_instruction="You are an expert in solving any type of questions, including coding, job-related, and technical queries."
)

# Streamlit UI
st.title("AI Question Solver & Code Generator")

# Option to upload an image or enter a query
option = st.radio("Choose an input method:", ["Text Input", "Upload Image"])

problem = ""
if option == "Text Input":
    # User input for the problem description
    problem = st.text_input("Enter your question or problem description")

elif option == "Upload Image":
    # Image input from the user
    uploaded_image = st.file_uploader("Upload an image containing a question", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Load image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Extract text from the image using pytesseract (OCR)
        problem = pytesseract.image_to_string(image)
        st.write("Extracted Question:", problem)

# User selects programming language (optional for coding-related problems)
language = st.selectbox("Select programming language (optional for coding queries)", ["None", "Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])

# Generate the solution when the user clicks the button
if st.button("Get Solution"):
    try:
        # Adjust the prompt based on the problem type (coding or general question)
        if language == "None":
            prompt = f"Answer the following question: {problem}"
        else:
            prompt = f"Create a program in {language} for the following problem: {problem}. Provide the code in a simple manner with fewer lines of code."
        
        # Generate the response from the AI model
        response = model.generate_content(prompt)
        solution_text = response.text
        
        # Display the generated solution
        st.subheader("Generated Solution")
        st.text(solution_text)
        
        if language != "None":
            st.subheader(f"Generated {language} Code")
            st.code(solution_text, language=language.lower())
        
    except Exception as e:
        st.error(f"An error occurred: {e}")