import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

suhu = [20, 21, 22, 23, 24, 25, 26, 27, 28]
penjualan = [100, 200, 300, 400, 500, 600, 700, 800, 900]
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekends = [70, 80, 90, 100, 110, 120, 130, 140, 150]

data = {
    'Suhu' : [20, 21, 22, 23, 24, 25, 26, 27, 28],
    'Penjualan_Strawberry' : [60, 70, 75, 80, 85, 90, 95, 100, 105],
    'Penjualan_Cokelat' : [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanilla' : [70, 80, 90, 100, 110, 120, 130, 140, 150],
    'Kelembaban' : [50, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

st.title("Visualisasi Scatter Plot Penjualan Es Krim")
st.sidebar.header("Pengaturan Visualisasi")

option = st.sidebar.selectbox(
    "pilih scatter plot",
    (
        "Basic",
        "Kustom",
        "Multiple",
        "Analisis"
    )
)

st.caption ("Praktikum 5 - Scatter Plot")
st.markdown("""
Kelompok 30:
- KAYS ELHAQ RABBANI (0110222218)
- AHMAD FAUZI NUGROHO (0110222293)
- MUHAMMAD AL FARUQ (0110122057)            
""")


def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax= plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('hubungan penjualan es krim dengan suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax= plt.subplots()
    ax.scatter(suhu, penjualan, color= "darkblue", s=100, edgecolors='black', alpha=0.7)
    ax.set_title('hubungan penjualan es krim dengan suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan')
    ax.grid(True)
    st.pyplot(fig)

def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax= plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color="darkblue", label="Weekdays", s=80)
    ax.scatter(suhu, penjualan_weekends, color="darkred", label="Weekends", s=80)
    ax.set_title("hubungan penjualan es krim dengan suhu")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan")
    ax.grid(True)
    st.pyplot(fig)

def analisis_scatter():
    st.subheader("4. Analisis Scatter Plot")
    
    jenis_eskrim = st.selectbox("Pilih Rasa Eskrimnya BOIII", ['Cokelat', 'Vanilla', 'Strawberry'])

    if jenis_eskrim == 'Cokelat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanilla':
        penjualan = df['Penjualan_Vanilla']
    else:
        penjualan = df['Penjualan_Strawberry']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembaban'], s=100, cmap='coolwarm', alpha=0.7)

    ax.set_title(f'hubungan penjualan {jenis_eskrim} vs Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelembaban (%)')

    st.pyplot(fig)
    
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik menunjukan hubungan anara suhum kelembaban dan penjualan es krim jenis **{jenis_eskrim}**')

if option == "Basic":
    basic_scatter()
elif option == "Kustom":
    custom_scatter()
elif option == "Multiple":
    multiple_scatter()
else:
    analisis_scatter()