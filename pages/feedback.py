import streamlit as st
from functions.get_s3_conn import upload_to_s3

st.title("Feedback")
with st.form("feedback_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    feedback = st.text_area("Give us some feedback! Good or bad, we'd love to hear it.")
    submitted = st.form_submit_button("Submit")
if submitted:
    feedback = {
    "name":name,
    "email":email,
    "phone":phone,
    "feedback":feedback
    }
    try:
        upload_to_s3('feedback', feedback)
    except Exception as e:
        pass