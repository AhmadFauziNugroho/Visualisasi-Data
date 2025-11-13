import streamlit as st
from PIL import Image

st.title("Spaced Out")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

img = Image.open("../../praktikum1/assets/1.png")
st.title("Spaced Out Columns")

for i in range(2):
    cols= st.columns((3,1,2,1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
