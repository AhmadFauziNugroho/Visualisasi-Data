import streamlit as st
import time

st.title("Grids")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(" (seconds) seconds have passed")
        time.sleep(1)
        st.write("Times up!")