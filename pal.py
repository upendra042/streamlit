import streamlit as st

st.title("palindrome or not")

a = st.text_input(label="Enter the term number (n)")


if a == a[::-1]:
    st.write("palindrome")
else:
    st.write("not a palindrome")