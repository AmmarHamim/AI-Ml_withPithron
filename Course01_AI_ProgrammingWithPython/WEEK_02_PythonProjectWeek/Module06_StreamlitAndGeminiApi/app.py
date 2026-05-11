from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv() #loading the env files
api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)


st.title("Gemini App")
st.divider()
user_input=st.text_input("Enter your prompt")

if st.button("Generate"):
    if user_input:
        with st.spinner("Thinking... 🤔"):

            response=client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=user_input
            )

            st.write(response.text)