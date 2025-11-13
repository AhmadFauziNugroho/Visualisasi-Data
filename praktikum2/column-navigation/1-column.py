import streamlit as st

st.title("Column")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

col1, col2 = st.columns(2)
col1.write("ini adalah kolom 1")
col1.image("../../praktikum1/assets/1.png")
col2.write("ini adalah kolom 2")
col2.image("../../praktikum1/assets/1.png")

