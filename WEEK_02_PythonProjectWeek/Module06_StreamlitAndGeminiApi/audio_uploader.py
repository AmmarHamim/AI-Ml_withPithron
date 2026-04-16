import streamlit as st
st.title("Audio Upload",anchor=False)
st.divider()

audioFile=st.file_uploader("Upload an audio file",["mp3","wav","m4a"])

if audioFile:
    st.audio(audioFile,loop=True)