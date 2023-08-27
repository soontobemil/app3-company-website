import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("/Users/jaysim/Documents/Coding-Project/company-website-bonus/topics.csv")

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input(label="Enter your email")
    selected_topic = st.selectbox('What topic do you want to discuss?', df["topic"])
    raw_message = st.text_area(label="Enter your message")
    message = f"""\
Subject: New mail from {user_email}

From: {user_email}
Topic: {selected_topic}
Contents: {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was successfully sent")