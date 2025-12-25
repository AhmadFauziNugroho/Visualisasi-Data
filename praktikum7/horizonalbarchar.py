import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Praktikum 7 VISDAT")
st.write("Kelompok: 30")
st.markdown("""
- KAYS ELHAQ RABBANI (0110222218)
- AHMAD FAUZI NUGROHO (0110222293)
- MUHAMMAD AL FARUQ (0110122057)
""")

brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 370, 380, 390]
sales_2024 = [410, 420, 430, 440]

y = np.arange(len(brands))
bar_width = 0.4

kategori = st.selectbox(
    "Pilih kategori visualisasi",
    ['basic', 'kustom', 'multiple']
)

if kategori == "basic":
    st.subheader("Horizontal Bar Chart Sederhana")
    fig1, ax1 = plt.subplots()
    ax1.barh(y, sales_2023, color='lightblue')
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands) # Menggunakan yticklabels
    ax1.set_title('Horizontal Bar Chart - 2023')
    ax1.set_xlabel('Sales')
    ax1.set_ylabel('Brands')
    st.pyplot(fig1) # Gunakan st.pyplot

    st.subheader("Stacked Horizontal Bar Chart")
    fig2, ax2 = plt.subplots()
    ax2.barh(y, sales_2023, color='lightgreen', label='2023')
    ax2.barh(y, sales_2024, color='darkblue', label='2024', left=sales_2023)
    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_title('Stacked Horizontal Bar Chart - 2023 & 2024')
    ax2.set_xlabel('Sales')
    ax2.set_ylabel('Brands')
    ax2.legend()
    st.pyplot(fig2)

elif kategori == "kustom":
    st.subheader("Horizontal Bar Chart Kustom")
    fig3, ax3 = plt.subplots()
    ax3.barh(y, sales_2023, color='lightblue', edgecolor='black')
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Horizontal Bar Chart dengan Label Nilai')
    ax3.set_xlabel('Sales')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    # Menambahkan label teks di ujung bar
    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va='center')
    st.pyplot(fig3)

    st.subheader("Kustomisasi Stacked Horizontal Bar Chart")
    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, color='lightgreen', label='2023', edgecolor='black')
    ax4.barh(y, sales_2024, color='darkblue', label='2024', left=sales_2023, edgecolor='black')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.grid(axis='x', linestyle='--', alpha=0.6)
    ax4.legend()
    st.pyplot(fig4)

else:
    st.subheader("Multiple Bar Chart (Side-by-Side)")
    fig5, ax5 = plt.subplots()
    # Logika bar side-by-side (mengurangi/menambah y dengan bar_width)
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label='2023')
    ax5.barh(y + bar_width/2, sales_2024, height=bar_width, label='2024')
    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_title('Multiple Bar Chart Side-by-Side')
    ax5.grid(axis='x', linestyle='--', alpha=0.6)
    ax5.legend()    
    st.pyplot(fig5)

    st.subheader("Multiple Stacked Horizontal Bar Chart")
    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, label='2024', left=sales_2023)
    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.grid(axis='x', linestyle='--', alpha=0.6)
    ax6.legend()
    st.pyplot(fig6)