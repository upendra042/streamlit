import streamlit as st
import subprocess

# Streamlit UI
st.title("Online Compiler")

# User inputs for the source code and programming language
source_code = st.text_area("Enter the source code")
language = st.selectbox("Select programming language", ["Python", "C", "Java", "JavaScript", "Ruby", "Go", "Rust", "PHP", "Swift", "Kotlin", "TypeScript", "R", "Scala"])

def compile_and_run_code(source_code, language):
    if language == "Python":
        try:
            exec_globals = {}
            exec(source_code, exec_globals)
            return str(exec_globals)
        except Exception as exec_error:
            return f"An error occurred during execution: {exec_error}"

    elif language == "C":
        # Save source code to a temporary file
        with open("temp.c", "w") as f:
            f.write(source_code)
        # Compile and run the C program
        compile_cmd = ["gcc", "temp.c", "-o", "temp.out"]
        run_cmd = ["./temp.out"]
    
    elif language == "Java":
        with open("Temp.java", "w") as f:
            f.write(source_code)
        compile_cmd = ["javac", "Temp.java"]
        run_cmd = ["java", "Temp"]

    elif language == "JavaScript":
        with open("temp.js", "w") as f:
            f.write(source_code)
        run_cmd = ["node", "temp.js"]

    elif language == "Ruby":
        with open("temp.rb", "w") as f:
            f.write(source_code)
        run_cmd = ["ruby", "temp.rb"]

    elif language == "Go":
        with open("temp.go", "w") as f:
            f.write(source_code)
        run_cmd = ["go", "run", "temp.go"]

    elif language == "Rust":
        with open("temp.rs", "w") as f:
            f.write(source_code)
        compile_cmd = ["rustc", "temp.rs", "-o", "temp.out"]
        run_cmd = ["./temp.out"]

    # Add other languages similarly

    else:
        return f"Compilation for {language} is not supported yet."

    if language in ["C", "Rust"]:
        # Compile the code
        compile_process = subprocess.run(compile_cmd, capture_output=True, text=True)
        if compile_process.returncode != 0:
            return f"Compilation error:\n{compile_process.stderr}"
        
        # Run the compiled executable
        run_process = subprocess.run(run_cmd, capture_output=True, text=True)
        return run_process.stdout if run_process.returncode == 0 else f"Runtime error:\n{run_process.stderr}"

    else:
        # Run the interpreted language command
        run_process = subprocess.run(run_cmd, capture_output=True, text=True)
        return run_process.stdout if run_process.returncode == 0 else f"Runtime error:\n{run_process.stderr}"

# Compile and run the code when the user clicks the button
if st.button("Run Code"):
    result = compile_and_run_code(source_code, language)
    st.subheader("Execution Result")
    st.text(result)
