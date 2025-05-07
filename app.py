# app.py

import streamlit as st
from utils import generate_script

# App title and header
st.title("YouTube Scriptwriting Tool")
st.header("Generate a video script by specifying a topic, length, and creativity level.")

# Main input fields for the video script
prompt = st.text_input("Provide the topic of the video:")
video_length = st.number_input("Specify video length (in minutes):", min_value=1, step=1)
creativity = st.slider("Set creativity level:", min_value=0.1, max_value=1.0, value=0.7)

# Button to generate the script
if st.button("Generate Script"):
    if not prompt:
        st.error("Please provide a topic for the video.")
    else:
        with st.spinner("Generating script..."):
            # Generate the script using GPT-2
            script = generate_script(prompt, video_length, creativity)
            st.success("Script generated successfully!")
            st.text_area("Generated Script", script, height=300)

