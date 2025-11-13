import streamlit as st
from PIL import Image

st.title("Padding")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

img = Image.open("../../praktikum1/assets/1.png")
st.title("Padding")

col1, padding, col2= st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)