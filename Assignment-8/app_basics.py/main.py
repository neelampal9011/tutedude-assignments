import streamlit as st

st.title("Welcome to streamlit ")
st.text_input("Enter your name : ")

if st.button('Greet me'):
    st.write("Hello !")
    
