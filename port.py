import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Upendra Chowdary Portfolio", layout="wide")

# --- Function to add rounded corners to images ---
def add_rounded_corners(img, radius):
    img = img.convert("RGBA")
    circle = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(circle)
    draw.rounded_rectangle((0, 0) + img.size, radius=radius, fill=255)
    img.putalpha(circle)
    return img

# --- Load and round images ---
image_left = add_rounded_corners(Image.open("upe1.jpg"), radius=60)
image_right = add_rounded_corners(Image.open("upe2.jpg"), radius=60)

# --- Header Section ---
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.image(image_left, use_column_width=True)
with col2:
    st.title("👨‍💻 Gangavarapu Upendra Chowdary")
    st.write("📍 Ongole | 📞 9912089471 | ✉️ 22pa1a0542@vishnu.edu.in")
    st.markdown(
        """
        [GitHub](https://github.com/upendra042) | 
        [LinkedIn](https://linkedin.com/in/upendra-chowdary-97838b2b7) | 
        [LeetCode](https://leetcode.com/u/22pa1a0542/) | 
        [GeeksforGeeks](https://www.geeksforgeeks.org/user/22pa1akzmz/)
        """
    )
with col3:
    st.image(image_right, use_column_width=True)

# --- Professional Summary ---
st.subheader("🔍 Professional Summary")
st.write("""
Results-driven Full Stack Developer with expertise in MERN stack (MongoDB, Express.js, React, Node.js) and Machine Learning. 
Adept at developing scalable applications, optimizing performance, and integrating AI-driven solutions. 
Proficient in API development, database management, and real-time web applications, with a proven track record of enhancing system efficiency by up to 60%.
""")

# --- Education ---
st.subheader("🎓 Education")
st.write("""
- **B.Tech in Computer Science**, Vishnu Institute of Technology (2022–2026) | CGPA: 8.8  
- **Intermediate**, Sri Chaitanya College (2020–2022) | Score: 83.6%  
- **High School**, Sri Chaitanya (2020) | CGPA: 10.0
""")

# --- Skills ---
st.subheader("🛠️ Technical Skills")
st.write("""
- **Programming Languages**: Python, Java, C  
- **Web Development**: HTML, CSS, JavaScript, React.js, Node.js  
- **Databases**: MongoDB, Firestore  
- **API Development**: REST, WebSockets, Gemini, Weather, Movie  
- **Machine Learning & AI**: TensorFlow, OpenCV  
- **Tools & Frameworks**: Git, Docker, Firebase, Postman
""")

# --- Projects ---
st.subheader("💼 Projects & Experience")

with st.expander("🔷 Contract Farming Platform (SIH 2024)"):
    st.write("""
- Real-time contract farming web app using React.js, Node.js, Firestore, and WebSockets.  
- Reduced manual effort by 50%, improved load speed by 35%, and ensured 99.9% uptime.  
- Integrated AI-powered chatbot reducing response time by 60%.  
- Published research at Dockathon.
""")

with st.expander("🔷 AI-Powered Web Applications (Streamlit)"):
    st.write("""
- Built 5 AI-based tools: code generator, language converter, YouTube video generator, and more.  
- Automated 45% of repetitive coding tasks.  
- Integrated Gemini AI, Weather, and Movie APIs for dynamic content.
""")

with st.expander("🔷 Fake Logo Detection System"):
    st.write("""
- ML model with TensorFlow achieving 85% accuracy in counterfeit logo detection.  
- Supported brand authentication.
""")

with st.expander("🔷 Cookbook Website (Hackathon Project)"):
    st.write("""
- Interactive recipe recommendation system with React.js and MongoDB.  
- Improved user retention by 30%.
""")

with st.expander("🔷 Sports Scheduler (Full-Stack Advanced Backend)"):
    st.write("""
- Real-time event scheduler using Node.js, Express.js, and PostgreSQL.  
- Managed 50+ events/month and boosted adoption by 25%.
""")

with st.expander("🔷 React.js Mini Projects"):
    st.write("""
- QR Generator for test automation – reduced admin work by 35%.  
- To-Do App with authentication & movie info – improved task completion by 35%.
""")

# --- Live Project Links ---
st.subheader("🚀 Live Projects")
st.markdown("""
- [All Codes Generator](https://app-allc.streamlit.app/)
- [Farmer Chatbot](https://farmchat.streamlit.app/)
- [Buyer Chatbot](https://app-xuly9tluurpyfa4rxifntt.streamlit.app/)
- [YouTube Query Generator](https://app-real.streamlit.app/)
- [Nth Fibonacci Number](https://febnocci.streamlit.app/)
- [Coding Compiler](https://compile.streamlit.app/)
- [Student Chatbot for Skill Sharing](https://studchat.streamlit.app/)
""")

# --- Certifications ---
st.subheader("📜 Certifications & Achievements")
st.write("""
- Google AI-ML & Android Virtual Internships  
- Smart India Hackathon (SIH) 2024 Finalist  
- Paper Published at Dockathon on Contract Farming  
- Hackathon – Cookbook Website  
- MATLAB & AI-ML Training – TensorFlow, OpenCV
""")

# --- Extra Activities ---
st.subheader("🧩 Additional Experience")
st.write("""
- Peer Mentoring: Trained 20+ students in programming & web dev  
- Industrial Visit: Ambient Scientific – AI application insights  
- Event Coordinator (Festindi Fuego): Managed 5+ events  
- Communication Programs: Career Strokes, English Strokes  
- Startup Discussions: Participated in Sparktank incubation events
""")

# --- Languages ---
st.subheader("🗣️ Languages")
st.write("English (Professional) | Telugu (Native)")
