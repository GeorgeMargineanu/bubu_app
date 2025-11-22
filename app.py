import streamlit as st

st.title("Magic Name App")

name = st.text_input("Enter a name:")

if name.strip().lower() == "bubu":
    st.markdown("<h1 style='color: red; text-align: center;'>❤</h1>", unsafe_allow_html=True)
else:
    st.write("Write 'Bubu' to see the magic!")