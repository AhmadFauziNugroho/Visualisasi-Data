import streamlit as st
import pandas as pd
import plotly.express as px
from typing import List
import os

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Dashboard APBD Jawa Barat 2020",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FUNGSI UNTUK MEMUAT CSS EKSTERNAL
def local_css(file_name: str):
    """Memuat file CSS lokal ke dalam aplikasi Streamlit."""
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"File CSS '{file_name}' tidak ditemukan.")

# FUNGSI DATA
@st.cache_data
def load_data(file_path: str) -> pd.DataFrame:
    """Memuat dan membersihkan data APBD dari file Excel."""
    try:
        df = pd.read_excel(file_path)
        
        # Konversi nilai anggaran ke numerik
        df['Nilaianggaran'] = pd.to_numeric(df['Nilaianggaran'], errors='coerce').fillna(0)
        
        # Pembersihan kolom teks
        text_cols = ['Namapemda', 'standarutama', 'standarjenis', 'Namaakunobjek']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().replace(['nan', 'None', ''], 'Lainnya')
        
        return df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return pd.DataFrame(columns=['Namapemda', 'standarutama', 'standarjenis', 'Namaakunobjek', 'Nilaianggaran'])

def filter_data(df: pd.DataFrame, tipe: List[str], daerah: List[str]) -> pd.DataFrame:
    """Memfilter dataframe berdasarkan input pengguna."""
    df_filtered = df.copy()
    if tipe:
        df_filtered = df_filtered[df_filtered['standarutama'].isin(tipe)]
    if daerah:
        df_filtered = df_filtered[df_filtered['Namapemda'].isin(daerah)]
    return df_filtered

# KOMPONEN UI
def render_metric_card(title: str, value: str):
    """Render kartu metrik menggunakan class CSS dari style.css."""
    st.markdown(
        f'<div class="metric-box">'
        f'<div class="metric-title">{title}</div>'
        f'<div class="metric-value">{value}</div>'
        f'</div>', 
        unsafe_allow_html=True
    )

def format_triliun(value: float) -> str:
    """Format angka ke satuan Triliun Rupiah."""
    return f"Rp {value/1e12:.2f} T"

# MAIN APPLICATION
def main():
    # 1. Load External CSS
    local_css("style.css")
    
    # 2. Load Data
    DATA_PATH = './Data_APBD_2020_Jawa_Barat.xlsx'
    df = load_data(DATA_PATH)
    
    if df.empty:
        st.warning("Data tidak tersedia. Pastikan file Excel berada di direktori yang benar.")
        return

    # 3. Header Section
    st.markdown('<div class="main-title">📊 Dashboard APBD Jawa Barat 2020</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Analisis Distribusi Anggaran, Pendapatan, dan Keseimbangan Fiskal</div>', unsafe_allow_html=True)

    # 4. Sidebar Filters
    st.sidebar.header("🔍 Filter Global")
    tipe_options = df['standarutama'].unique()
    tipe_anggaran = st.sidebar.multiselect("Tipe Anggaran Utama", tipe_options, default=tipe_options)
    
    daerah_options = sorted(df['Namapemda'].unique())
    daerah_selected = st.sidebar.multiselect("Pilih Daerah (Kosongkan untuk Semua)", daerah_options)

    # 5. Data Filtering
    df_filtered = filter_data(df, tipe_anggaran, daerah_selected)

    # 6. Key Metrics
    m1, m2, m3, m4 = st.columns(4)
    total_anggaran = df_filtered['Nilaianggaran'].sum()
    total_belanja = df_filtered[df_filtered['standarutama'].str.contains('Belanja', na=False)]['Nilaianggaran'].sum()
    total_pendapatan = df_filtered[df_filtered['standarutama'].str.contains('Pendapatan', na=False)]['Nilaianggaran'].sum()
    
    with m1: render_metric_card("Total Anggaran", format_triliun(total_anggaran))
    with m2: render_metric_card("Total Belanja", format_triliun(total_belanja))
    with m3: render_metric_card("Total Pendapatan", format_triliun(total_pendapatan))
    with m4: render_metric_card("Jumlah Entitas", f"{df_filtered['Namapemda'].nunique()} Daerah")

    st.markdown("<br>", unsafe_allow_html=True)

    # 7. Tabs Navigation
    tabs = st.tabs([
        "📈 Overview", "📍 Belanja Daerah", "📊 Jenis Belanja", 
        "💰 Pendapatan", "⚖️ Fiskal", "📋 Detail", "🔥 Heatmap"
    ])

    # --- TAB 1: OVERVIEW ---
    with tabs[0]:
        st.markdown('<div class="section-title">Komposisi Anggaran Utama</div>', unsafe_allow_html=True)
        col_chart, col_info = st.columns([2, 1])
        komposisi = df_filtered.groupby('standarutama')['Nilaianggaran'].sum().reset_index()
        
        with col_chart:
            fig = px.pie(komposisi, values='Nilaianggaran', names='standarutama', hole=0.5, 
                         color_discrete_sequence=px.colors.qualitative.Safe)
            fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
            
        with col_info:
            st.markdown("<br>"*2, unsafe_allow_html=True)
            for _, row in komposisi.iterrows():
                st.write(f"**{row['standarutama']}**")
                st.info(format_triliun(row['Nilaianggaran']))

    # --- TAB 2: BELANJA DAERAH ---
    with tabs[1]:
        st.markdown('<div class="section-title">Perbandingan Belanja antar Daerah</div>', unsafe_allow_html=True)
        belanja_df = df_filtered[
            (df_filtered['standarutama'].str.contains('Belanja', na=False)) & 
            (df_filtered['Namapemda'] != 'Provinsi Jawa Barat')
        ]
        if not belanja_df.empty:
            belanja = belanja_df.groupby('Namapemda')['Nilaianggaran'].sum().sort_values(ascending=True)
            fig = px.bar(belanja, x='Nilaianggaran', y=belanja.index, orientation='h', 
                         color='Nilaianggaran', color_continuous_scale='Blues')
            fig.update_layout(height=600, coloraxis_showscale=False, yaxis_title=None)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Data belanja tidak ditemukan untuk filter ini.")

    # --- TAB 3: JENIS BELANJA ---
    with tabs[2]:
        st.markdown('<div class="section-title">Analisis Jenis Belanja</div>', unsafe_allow_html=True)
        belanja_jenis_df = df_filtered[df_filtered['standarutama'].str.contains('Belanja', na=False)]
        
        if not belanja_jenis_df.empty:
            c_left, c_right = st.columns([1, 1.5])
            with c_left:
                st.markdown('<div class="insight-card"><div class="insight-header">🔝 5 Jenis Belanja Terbesar</div>', unsafe_allow_html=True)
                top_jenis = belanja_jenis_df.groupby('standarjenis')['Nilaianggaran'].sum().nlargest(5).reset_index()
                top_jenis['Nilai'] = top_jenis['Nilaianggaran'].apply(format_triliun)
                st.table(top_jenis[['standarjenis', 'Nilai']])
                st.markdown('</div>', unsafe_allow_html=True)
                st.info("💡 Grafik menunjukkan perbandingan total anggaran per kategori belanja.")

            with c_right:
                total_per_jenis = belanja_jenis_df.groupby('standarjenis')['Nilaianggaran'].sum().sort_values(ascending=True).reset_index()
                fig_bar = px.bar(total_per_jenis, x='Nilaianggaran', y='standarjenis', orientation='h', 
                                 color='Nilaianggaran', color_continuous_scale='Viridis')
                fig_bar.update_layout(height=500, coloraxis_showscale=False, margin=dict(l=0, r=20, t=20, b=20))
                st.plotly_chart(fig_bar, use_container_width=True)

    # --- TAB 4: PENDAPATAN ---
    with tabs[3]:
        st.markdown('<div class="section-title">Komposisi Pendapatan Daerah</div>', unsafe_allow_html=True)
        pend_df = df_filtered[
            (df_filtered['standarutama'].str.contains('Pendapatan', na=False)) & 
            (df_filtered['Namapemda'] != 'Provinsi Jawa Barat')
        ]
        
        if not pend_df.empty:
            comp_pend = pend_df.groupby(['Namapemda', 'standarjenis'])['Nilaianggaran'].sum().reset_index()
            
            # Hitung Rasio PAD
            pad_val = comp_pend[comp_pend['standarjenis'].str.contains('ASLI DAERAH|PAD', na=False, case=False)].groupby('Namapemda')['Nilaianggaran'].sum().reset_index()
            total_pend = comp_pend.groupby('Namapemda')['Nilaianggaran'].sum().reset_index()
            ratio_df = pd.merge(pad_val, total_pend, on='Namapemda', suffixes=('_PAD', '_Total'))
            ratio_df['Rasio_PAD'] = (ratio_df['Nilaianggaran_PAD'] / ratio_df['Nilaianggaran_Total']) * 100
            ratio_df = ratio_df.sort_values('Rasio_PAD', ascending=False)

            c_l, c_r = st.columns([1, 1.5])
            with c_l:
                st.markdown('<div class="insight-card"><div class="insight-header">🏆 Top 5 Daerah Mandiri</div>', unsafe_allow_html=True)
                st.dataframe(ratio_df[['Namapemda', 'Rasio_PAD']].head(5).style.format({'Rasio_PAD': '{:.2f}%'}), 
                             hide_index=True, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with c_r:
                fig_stack = px.bar(comp_pend, x='Namapemda', y='Nilaianggaran', color='standarjenis', barmode='stack')
                fig_stack.update_layout(xaxis_tickangle=-45, height=500, legend=dict(orientation="h", y=1.1))
                st.plotly_chart(fig_stack, use_container_width=True)
        else:
            st.warning("Data pendapatan tidak tersedia.")

    # --- TAB 5: FISKAL ---
    with tabs[4]:
        st.markdown('<div class="section-title">Analisis Keseimbangan & Pembiayaan</div>', unsafe_allow_html=True)
        summary = df_filtered[df_filtered['Namapemda'] != 'Provinsi Jawa Barat'].groupby(['Namapemda', 'standarutama'])['Nilaianggaran'].sum().unstack(fill_value=0)
        
        cols = summary.columns
        c_pend = [c for c in cols if 'Pendapatan' in c]
        c_belanja = [c for c in cols if 'Belanja' in c]
        
        if c_pend and c_belanja:
            summary['Total_Pendapatan'] = summary[c_pend].sum(axis=1)
            summary['Total_Belanja'] = summary[c_belanja].sum(axis=1)
            summary['Surplus/Defisit'] = summary['Total_Pendapatan'] - summary['Total_Belanja']
            summary = summary.reset_index()
            
            fig_bubble = px.scatter(summary, x='Total_Pendapatan', y='Total_Belanja', 
                                    size=summary['Total_Pendapatan'].abs()/1e10, color='Surplus/Defisit', 
                                    hover_name='Namapemda', color_continuous_scale='RdYlGn')
            
            max_val = max(summary['Total_Pendapatan'].max(), summary['Total_Belanja'].max())
            fig_bubble.add_shape(type="line", x0=0, y0=0, x1=max_val, y1=max_val, line=dict(color="black", dash="dash"))
            st.plotly_chart(fig_bubble, use_container_width=True)

    # --- TAB 6: DETAIL ---
    with tabs[5]:
        st.markdown('<div class="section-title">Eksplorasi Data Mentah</div>', unsafe_allow_html=True)
        st.dataframe(df_filtered, use_container_width=True)

    # --- TAB 7: HEATMAP ---
    with tabs[6]:
        st.markdown('<div class="section-title">Heatmap Intensitas Anggaran</div>', unsafe_allow_html=True)
        heatmap_df = df_filtered[
            (df_filtered['standarutama'].str.contains('Belanja', na=False)) & 
            (df_filtered['Namapemda'] != 'Provinsi Jawa Barat')
        ]
        if not heatmap_df.empty:
            pivot_df = heatmap_df.pivot_table(index='Namapemda', columns='standarjenis', values='Nilaianggaran', aggfunc='sum').fillna(0)
            fig_heat = px.imshow(pivot_df, color_continuous_scale='Viridis', aspect="auto")
            st.plotly_chart(fig_heat, use_container_width=True)

    # Footer
    st.divider()
    st.markdown("<center style='color:#94a3b8;'>Dashboard APBD Jawa Barat 2020 • Modular Version</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()