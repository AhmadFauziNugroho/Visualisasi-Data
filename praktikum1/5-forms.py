import streamlit as st
import pandas as pd

st.title("Praktikum 01 - VisDat")
st.caption("5-forms")
st.markdown("""
            - KAYS ELHAQ RABBANI - 0110222218
            - AHMAD FAUZI NUGROHO - 0110222293
            - MUHAMMAD AL FARUQ - 0110122057
""")

st.subheader('Text Box')
name = st.text_input("Nama lu siapa?")
st.write("jadi namalu : ", name)

st.subheader('Text Area')
input_text = st.text_area("Kasih Review dong boii")
st.write(""""Review lu: \n""", input_text)

st.subheader('Number Input')
num = st.number_input("masukin nomor boii", 0, 10, 5, 2)
st.write("nomor terkencil adalah 0, \n nomor terbesar 10")
st.write("default = 10")
st.write("total = ", num)

st.subheader('Time')
st.time_input("input waktu")

st.subheader('Date')
st.date_input("masukan tangal")

st.subheader('Color')
color_code = st.color_picker("pilih warna")
st.header(color_code)

st.subheader('Dataset Upload')
data_file = st.file_uploader("upload csv", type=["csv"])
details = st.button("Check details")
if details:
    if data_file is not None :
        file_details    = {"file_name":data_file.name, "file_type":data_file.type, "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
else:
    st.write("gaada file csv")

st.subheader('Submit Button')
my_form =  st.form(key="form")
a = my_form.text_input(label="masukan text")

submit_button = my_form.form_submit_button(label='Submit boii')
st.write(a)