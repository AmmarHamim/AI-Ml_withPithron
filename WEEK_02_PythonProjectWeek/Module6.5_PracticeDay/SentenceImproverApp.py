from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

st.title("Professional Sentence Improver ✨")
st.divider()

user_input=st.text_input("Enter your sentence ")

if st.button("Improve"):
    if user_input.strip()=="":
        st.error("You have not entered anything")
    else:
        prompt= f"Improve this sentence professionally and dont give me more than 3 options: {user_input}"
        
        with st.spinner("Improving...."):
            response=client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
            )

        
        st.markdown("### Improved Version:")
        st.success(response.text)


