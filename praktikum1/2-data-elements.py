import streamlit as st
import pandas as pd     # mengelola data dalam bentuk tabel (dataframe)
import numpy as np      # membuat data numerik acak
import altair as alt    # membuat chart interaktif
import matplotlib.pyplot as plt

st.title("Praktikum 01 - VisDat")
st.caption("2-data-elements")
st.markdown("""
            - KAYS ELHAQ RABBANI - 0110222218
            - AHMAD FAUZI NUGROHO - 0110222293
            - MUHAMMAD AL FARUQ - 0110122057
""")

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.dataframe(df)

st.subheader("Highlight Nilai Minimum")
st.dataframe(df.style.highlight_min(axis=0))

st.subheader("Tabel Status")
df = pd.DataFrame(
    np.random.randn (30,10),
    columns=('col_no %d' % i for i in range (10))
)
st.table(df)

st.subheader("Matrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C")

col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
            delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10,
            delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "- 1.132.649")


st.subheader("write as superfuction")
#Write Function as superfunction

st.write('ini datanya', df, 'Data ini format dataframe \n', "\nditulis dalam superfuntion")

#random values
df = pd.DataFrame(
    np.random.randn(10, 2), 
    columns=['a', 'b']
)

#chart
chart = alt.Chart(df).mark_bar().encode(
    x= 'a', y= 'b', tooltip=['a', 'b']
)

st.write(chart)
st.subheader('Magic')

# math tanpa function
"adding 5 & 4 = ", 5+4

#menampilkan var a dan value
a = 5
'a',a

#markdown + magic
"""
# Magic feature
markdown working without defining its function explicity
"""

# data frame dengan magic
df = pd.DataFrame({'col' : [1,2]})
'dataframe', df

# chart dengan magic
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

"chart", chart