import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The best company")
contents = """
lorem ipsumlorem lorem ipsum ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum
"""
st.write(contents)

st.subheader("Our Team")

col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

df = pandas.read_csv("data.csv")


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])