import streamlit as st
import numpy as np
import pandas as pd

st.title("Map")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

df = pd.DataFrame(
    np.random.randn(50,2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"] 
)
st.map(df)