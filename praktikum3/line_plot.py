import streamlit as st
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,18,20,22,30,25,40,45,23,11]
product_B_sales = [15,25,20,7,12,45,12,14,55,23,45,66]
product_C_sales = [30,12,22,14,12,15,23,67,44,66,11,22]
product_D_sales = [10,20,1,25,77,55,33,53,72,34,64,12]

st.title("visualisasi penjualan produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("pilih Tipe Visualisasi", ("Single Line Plot",
                                                         "Multiple & Customization",
                                                         "Jenis Garus untuk Menunjukan Tren",
                                                         "Subplot"))


st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
            - KAYS ELHAQ RABBANI (0110222218)
            - AHMAD FAUZI NUGROHO (0110222293)
            - MUHAMMAD AL FARUQ (0110122057)
""")


def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A")
    ax.set_title("Penjualan Product A per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    ax.legend()
    st.pyplot(fig)

def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color="blue", linestyle= '--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color="green", linestyle= '-', marker='x')
    ax.set_title("Penjualan Product per Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label="Product C", color="yellow", linestyle= '-.')
    axs.plot(months, product_D_sales, label="Product D", color="red", linestyle= ':')
    axs.set_title("Penjualan Product per Bulan")
    axs.set_xlabel("Bulan")
    axs.set_ylabel("Penjualan")
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    axs[0].plot(months, product_C_sales, label = 'product C', color ='green', marker='d')
    axs[0].set_title('Penjualan Product C Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(months, product_D_sales, label = 'product D', color ='orange', marker='s')
    axs[1].set_title('Penjualan Product D Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Single Line Plot":
    line_plot()
elif option =="Multiple & Customization":
    customize_line_plot()
elif option == "Jenis Garus untuk Menunjukan Tren":
    tren_line_plot()
elif option == 'Subplot':
    subplots()