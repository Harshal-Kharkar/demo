import streamlit as st

with st.form(key='my_form'):
    st.write("## Input Form")
    name = st.text_input(label='Enter your name')
    age = st.number_input(label='Enter your age', min_value=0, max_value=120, value=25)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name: {name}, Age: {age}")
    print("your are in the submit block")