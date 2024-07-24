import streamlit as st
st.set_page_config(page_icon="",page_title="Upendra's portfolio")
st.title("GANGAVARAPU UPENDRA CHOWDARY",anchor=False)
st.subheader("WEB DEVELOPMENT",anchor=False)
with st.container(border=True):
    st.info("I am ------------")
col1,col2,col3=st.columns(3)
with col1:
    with st.expander(label="know me more",expanded=True):
        st.info("hey ---------")
with col2:
    with st.expander(label="knowing me more",expanded=True):
        st.warning("ongole")
with col3:
    with st.expander(label="knowed me more",expanded=True):
        st.error("Andhra pradesh")
       
