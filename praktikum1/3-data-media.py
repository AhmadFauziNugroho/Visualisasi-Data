import streamlit as st
import base64
from PIL import Image

st.title("Praktikum 01 - VisDat")
st.caption("2-data-elements")
st.markdown("""
            - KAYS ELHAQ RABBANI - 0110222218
            - AHMAD FAUZI NUGROHO - 0110222293
            - MUHAMMAD AL FARUQ - 0110122057
""")

st.subheader('Images')
st.write("menampilkan gambar")
st.image("assets/1.png")


st.write("menampilkan banyak gambar")
gambar_banyak = [
    'assets/1.png',
    'assets/2.png',
    'assets/3.png',
    'assets/4.png',
]
st.image(gambar_banyak, width=150)

st.subheader('Background Image')
def add_local_background_image_(image):
    with open(image, "rb") as image:
        encode_string = base64.b64encode(image.read())
    st.write("ini gambar")
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:files/{"jpeg"};base64,{encode_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background image")
add_local_background_image_('assets/5.jpeg')

st.subheader("Resizing Image")
original_image = Image.open("assets/1.png")
st.title("original image")
st.image(original_image)
resized_image = original_image.resize((600, 350))
st.title("resized image")
st.image(resized_image)
