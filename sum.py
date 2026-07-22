# Sum of 2 numbers 

import streamlit as st
st.title("Sum of 2 numbers")

n1= st.number_input("Enter no 1 : ")
n2= st.number_input("Enter no 2 : ")

ans = n1 + n2 

# check if the button pressed or not 

if(st.button("Calculate Sum")):
    st.text("Sum is {}  ".format(ans))
 