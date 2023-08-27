import streamlit as st
import pandas

df = pandas.read_csv("/Users/jaysim/Documents/Coding-Project/company-website-bonus/topics.csv")


st.title("Contact me")

st.text_input(label="Enter your email")
for index, row in df.iterrows():
    topics_list = (row["topic"])
    st.selectbox('What topic do you want to discuss?',
    (row["topic"]))
st.text_area(label="Your message here")
st.button("Submit")