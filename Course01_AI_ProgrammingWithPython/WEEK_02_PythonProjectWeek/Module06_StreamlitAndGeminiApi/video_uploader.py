import streamlit as st
st.title("Video Upload",anchor=False)
st.divider()


st.video("https://www.youtube.com/watch?v=Qzc_aX8c8g4&list=RDQzc_aX8c8g4&start_radio=1")

videoFile=st.file_uploader("Upload a video",["mp4","mov","avi"])
pressed=st.button("📤Upload",type="primary")

if pressed:
    if videoFile:
        st.video(videoFile)
        st.success("Uploaded successfully")


    else:
        st.error("u must Upload a file")