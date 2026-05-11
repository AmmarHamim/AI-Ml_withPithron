import streamlit as st

st.title("How to take Input",anchor=False)
st.divider()

name=st.text_input("Enter your name")
# st.write("Your name is ",name)
age=st.number_input("Enter your age",value=None,placeholder="Type your age")

# st.write("Your age is ",age)

password=st.text_input("Enter your password ",type="password")
# st.write("Your password is ", password)


selected=st.selectbox("Select your Gender",("Male","Female"),index=None,accept_new_options=True)
st.write("You selected ",selected)

pressed=st.button("Confirm",type="primary")


if(pressed):
    st.write(f"Your name is {name} and age is {age} and password is {password}")
else:
    st.write("Click the button")