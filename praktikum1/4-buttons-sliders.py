import streamlit as st
import time

st.title("Praktikum 01 - VisDat")
st.caption("2-data-elements")
st.markdown("""
            - KAYS ELHAQ RABBANI - 0110222218
            - AHMAD FAUZI NUGROHO - 0110222293
            - MUHAMMAD AL FARUQ - 0110122057
""")

st.title('membuat button')

st.subheader("Button")
button= st.button('Click Here')
if button:
    st.write('udah diclick')
else:
    st.write('belum diclick boii')


st.subheader('Radio Button')

gender = st.radio(
    "select gender",    
    ('male', 'female')) 
if gender == 'male':
    st.write('jadi lu laki')
else: 
    st.write('jadi lu perempuan')

st.subheader('Check Box')

st.write('hobi lu apa?')
check_1 = st.checkbox('game')
check_2 = st.checkbox('music')
check_3 = st.checkbox('coding')

st.subheader('Drop Down')

hobby = st.selectbox('hobi lu apa?: ',
                     ('game', 'mancing','music'))

st.subheader('Multiselect')
hobbies = st.multiselect(
    'hobi lu apa?',
    ['game', 'cola', 'soda', 'kue', 'bakpao'],
    ['game', 'cola', 'soda']
)

st.subheader('Download')

down_btn = st.download_button(
    label="download gambar",
    data=open("assets/1.png", "rb"),
    file_name="K",
    mime="image/png"
)

st.subheader('progress bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download selesai')

st.subheader('spinners')
with st.spinner('loading...'):
    time.sleep(5)
st.write('hello data scientists')