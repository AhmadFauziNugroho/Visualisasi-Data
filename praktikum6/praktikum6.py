import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Praktikum 6 VISDAT")
st.write("Kelompok: 30")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")

# dataset
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 250]
female = [120, 240, 180]

# data tramsaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 300, 400]
product_b = [150, 250, 350]

# data quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1 grafik stacked vertical bar chart
st.subheader("1. Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label="Male", color="darkblue")
ax.bar(x, female, bottom=male, label='Female', color="darkred")

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 2 grafik stacked vertical bar chart dengan Matplotlib
st.subheader("2. Stacked Vertical Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label="product_a", color="green")
ax.bar(x, product_b, bottom=product_a, label='product_b' , color="yellow")

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3 Kustomisasi grafik stacked vertical bar chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')
st.pyplot(fig)

# 4. grafik multiple stacked vertical bar chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

ax.bar(x - width/2, q1_male, label= 'q1_male', color='darkblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label='q1_female', color='darkorange', width=width)

ax.bar(x + width/2, q2_male, label= 'q2_male', color='darkred', width=width)
ax.bar(x + width/2, q2_female, bottom= q2_male, label='q2_female', color='yellow', width=width)

ax.set_title('Population by Gender and Store (Multiple Quarter)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)