import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyBuaKP0XoYSfqrtpipRe4qiMCUa6lM56Nc")

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

marquee_message = "<span style='color: green; font-size: 20px; font-weight: bold;'>Developed by upendra chøwdary VITB"
st.markdown(f"<marquee>{marquee_message}</marquee>", unsafe_allow_html=True)


# Streamlit UI
st.title("AI Code Generator")

# User input for the problem description and programming language
problem = st.text_input("Enter problem description")
language = st.selectbox("Select programming language", ["Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])

# Generate the code when the user clicks the button
if st.button("Generate Code"):
    try:
        # Construct the prompt
        prompt = f"Create a program in {language} for the following problem: {problem}. Provide the code in a simple manner with fewer lines of code."
        
        # Generate the response
        response = model.generate_content(prompt)
        code_text = response.text
        
        # Display the generated code
        st.subheader(f"Generated {language} Code")
        st.code(code_text, language=language.lower())
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
