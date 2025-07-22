import streamlit as st
from textblob import TextBlob

# Autocorrect Function
def autocorrect_text(text):
    return str(TextBlob(text).correct())

# Streamlit UI
st.set_page_config(page_title="Autocorrect Tool", layout="centered")
st.title(" AI Autocorrect Tool")
st.markdown("Fix spelling mistakes instantly using AI!")

# Input
user_input = st.text_area("Enter your text below:", height=200)

# Button
if st.button("Correct Text"):
    if user_input.strip():
        corrected = autocorrect_text(user_input)
        st.success(" Corrected Text:")
        st.write(corrected)
    else:
        st.warning(" Please enter some text to correct.")
