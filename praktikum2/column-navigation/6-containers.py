import streamlit as st
import numpy as np

st.title("Grids")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

st.title("Container")
with st.container():
    st.write("Element Inside Contianer")
    
#Defining Chart Element
st.line_chart(np.random.randn(40, 4))

st.write("Element Outside Container")