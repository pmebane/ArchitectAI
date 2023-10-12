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
    try:
        upload_to_s3('discovery', {k: v for k, v in st.session_state.items()})
    except Exception as e:
        pass