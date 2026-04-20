import streamlit as st
from PIL import Image
from api_call import output_generation


st.title("🐞 AI Code Debugger")
st.divider()


#images
images=st.file_uploader("Upload your code error screenshot",type=["jpeg","jpg","png"])

selected_opt=st.selectbox("Choose output type",["Hints","Solution with code"],index=None)

pressed=st.button("Debug Code")

if pressed:
    if images is None or selected_opt is None:
        st.error("⚠️ Please upload an image and select an option first!")

    else:
        pil_img=Image.open(images)
        with st.container(border=True):
            st.subheader("Here is the debug")
            with st.spinner("debugging...."):

                generated_output=output_generation(pil_img,selected_opt)

                st.markdown(generated_output)