import streamlit as st
import subprocess
import tempfile
import os

# Streamlit UI for the compiler
st.title("Online Code Compiler")

# User input for the code and programming language
code = st.text_area("Enter your code here")
language = st.selectbox("Select programming language", ["Python", "C", "C++", "Java"])

# Function to compile and run the code
def compile_and_run_code(language, code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=get_file_extension(language)) as temp_file:
            temp_file.write(code.encode())
            temp_file.flush()
            temp_file_name = temp_file.name
        
        # Depending on the language, compile and execute the code
        if language == "Python":
            result = subprocess.run(["python", temp_file_name], capture_output=True, text=True)  # Changed from 'python3' to 'python'
        elif language == "C":
            compile_result = subprocess.run(["gcc", temp_file_name, "-o", temp_file_name+".exe"], capture_output=True, text=True)
            if compile_result.returncode == 0:
                result = subprocess.run([temp_file_name+".exe"], capture_output=True, text=True)
            else:
                return compile_result.stderr
        elif language == "C++":
            compile_result = subprocess.run(["g++", temp_file_name, "-o", temp_file_name+".exe"], capture_output=True, text=True)
            if compile_result.returncode == 0:
                result = subprocess.run([temp_file_name+".exe"], capture_output=True, text=True)
            else:
                return compile_result.stderr
        elif language == "Java":
            compile_result = subprocess.run(["javac", temp_file_name], capture_output=True, text=True)
            if compile_result.returncode == 0:
                result = subprocess.run(["java", temp_file_name], capture_output=True, text=True)
            else:
                return compile_result.stderr
        else:
            return "Unsupported language"

        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

# Helper function to get the file extension based on language
def get_file_extension(language):
    extensions = {
        "Python": ".py",
        "C": ".c",
        "C++": ".cpp",
        "Java": ".java"
    }
    return extensions.get(language, "")

# Run the code when the user clicks the button
if st.button("Run Code"):
    if code:
        output = compile_and_run_code(language, code)
        st.subheader("Output")
        st.code(output)
    else:
        st.error("Please enter some code to run.")
