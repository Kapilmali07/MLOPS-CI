import streamlit as st

#streamlit UI
st.title("power calculator")
st.write("Enter a  number to calculate it square, cube, and fifth power. ")

#get user input
n=st.number_input("Enter an Integer", value=1, step=1)

#calculate result
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#display result
st.write(f"the square of {n} is :{square}")
st.write(f"the cube of {n} is :{cube}")
st.write(f"the fifth power of {n} is :{fifth_power}")
