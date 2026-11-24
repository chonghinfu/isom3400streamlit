import streamlit as st
import math

# Title
st.title("Basic Web Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide", "Sin()"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Sin()":
        #"pass" this is cause error because {result} becomes undefined
        result = math.sin(math.radians(num1))
    else:
        result = "Invalid operation!"

    st.subheader(f"Result: {result}")


#return a/b if b !=0 else "Error: Division by zero" --> this means if b not equals to zero, then a/b, else ...
