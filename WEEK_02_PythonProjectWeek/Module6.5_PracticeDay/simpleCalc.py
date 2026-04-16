import streamlit as st

st.title("Simple Calculator")
st.divider()

num1 = st.number_input("Enter first number",value=None)
num2 = st.number_input("Enter second number",value=None)

operator=st.selectbox("Choose Operation",["+","-","*","/"],index=None,placeholder="Select and operator")

if st.button("Calculate"):

    if num1 is not None and num2 is not None and operator:
        if operator=="+":
            result=num2+num1
        elif operator=="-":
            result=num1-num2
        
        elif operator=="*":
            result=num2*num1
        elif operator=="/":
            if num2==0:
                st.error("Can't divide by zero")
                result=None
            else:
                result=num1/num2

    else:
        if num1 is None and num2 is None:
            result=None
            st.error("Please enter numbers")

        elif num1 is None:
            result=None
            st.error("Please enter the first number")
        
        elif num2 is None:
            result=None
            st.error("Please enter the Second number")
        else:
            result=None
            st.error("Select an operator")

    
    if result is not None:
        st.success(f"{num1} {operator} {num2} = {result}")