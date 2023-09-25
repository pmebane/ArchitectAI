import streamlit as st

st.title("Feedback")
with st.form("feedback_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    feedback = st.text_area("Give us some feedback! Good or bad, we'd love to hear it.")
    submitted = st.form_submit_button("Submit")
#if submitted:
#   log to db