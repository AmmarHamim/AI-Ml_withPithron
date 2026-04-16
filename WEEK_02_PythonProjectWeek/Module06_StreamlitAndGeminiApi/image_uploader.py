import streamlit as st

st.title("How to upload images",anchor=False)
st.divider()

uploaded=st.file_uploader("Upload your images",type=["jpg","jpeg","png"],accept_multiple_files=True)

print(type(uploaded))

if uploaded:
    # for file in uploaded:
        # st.image(file,caption=file.name,use_container_width=True)
        # st.write("File name:", file.name)
        # st.write("File size (bytes):", file.size)
        # st.write(f"{file.name} - {round(file.size/1024,2)} KB")
        # st.divider()

    col=st.columns(3)
    for i,img in enumerate(uploaded):

        with col[i%3]:
            st.image(img, caption=img.name, use_container_width=True)


