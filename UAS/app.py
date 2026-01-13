import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# KONFIGURASI STREAMLIT
st.set_page_config(
    page_title="Dashboard APBD Jawa Barat 2020",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# STYLING
st.markdown("""
<style>
/* Global */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Title */
.main-title {
    font-size: 2.6em;
    font-weight: 700;
    color: #0f172a;
    text-align: center;
}
.subtitle {
    font-size: 1.05em;
    color: #64748b;
    text-align: center;
    margin-bottom: 30px;
}

/* Metric Card */
.metric-box {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.04);
    text-align: center;
}
.metric-title {
    font-size: 0.9em;
    color: #475569;
}
.metric-value {
    font-size: 1.7em;
    font-weight: 700;
    color: #1e293b;
}

/* Section Title */
.section-title {
    font-size: 1.4em;
    font-weight: 600;
    margin-bottom: 10px;
    color: #1e293b;
}
</style>
""", unsafe_allow_html=True)

# LOAD DATA
@st.cache_data
def load_data():
    return pd.read_excel('./Data_APBD_2020_Jawa_Barat.xlsx')

df = load_data()
df['Nilaianggaran'] = pd.to_numeric(df['Nilaianggaran'], errors='coerce')

# HEADER
st.markdown('<div class="main-title">📊 APBD Jawa Barat 2020</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Distribusi dan Analisis Pendapatan, Belanja, dan Pembiayaan Daerah</div>',
    unsafe_allow_html=True
)

# SIDEBAR
st.sidebar.header("🔍 Filter Data")

tipe_anggaran = st.sidebar.multiselect(
    "Tipe Anggaran",
    df['standarutama'].unique(),
    df['standarutama'].unique()
)

daerah = st.sidebar.multiselect(
    "Daerah",
    sorted(df['Namapemda'].unique()),
    []
)

df_filtered = df.copy()

if tipe_anggaran:
    df_filtered = df_filtered[df_filtered['standarutama'].isin(tipe_anggaran)]

if daerah:
    df_filtered = df_filtered[df_filtered['Namapemda'].isin(daerah)]


# METRICS
st.markdown("### 📈 Ringkasan Utama")

c1, c2, c3, c4 = st.columns(4)

def metric_card(col, title, value):
    col.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

metric_card(c1, "Total Anggaran", f"Rp {df_filtered['Nilaianggaran'].sum()/1e12:.2f} T")
metric_card(c2, "Total Belanja", f"Rp {df_filtered[df_filtered['standarutama'].str.contains('Belanja')]['Nilaianggaran'].sum()/1e12:.2f} T")
metric_card(c3, "Total Pendapatan", f"Rp {df_filtered[df_filtered['standarutama'].str.contains('Pendapatan')]['Nilaianggaran'].sum()/1e12:.2f} T")
metric_card(c4, "Jumlah Daerah", f"{df_filtered['Namapemda'].nunique()} Daerah")

st.divider()

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "💰 Belanja Daerah",
    "🏛️ Jenis Belanja",
    "📋 Detail Data"
])

# TAB 1: OVERVIEW
with tab1:
    st.markdown('<div class="section-title">Komposisi Anggaran Utama</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    komposisi = df_filtered.groupby('standarutama')['Nilaianggaran'].sum().reset_index()
    komposisi['Persentase'] = komposisi['Nilaianggaran'] / komposisi['Nilaianggaran'].sum() * 100

    with col1:
        fig = px.pie(
            komposisi,
            values='Nilaianggaran',
            names='standarutama',
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        komposisi['Nilai'] = komposisi['Nilaianggaran'].apply(lambda x: f"Rp {x/1e12:.2f} T")
        st.dataframe(
            komposisi[['standarutama', 'Nilai']],
            use_container_width=True,
            hide_index=True
        )

# TAB 2: BELANJA PER DAERAH
with tab2:
    st.markdown('<div class="section-title">Belanja Kabupaten / Kota</div>', unsafe_allow_html=True)

    belanja_df = df_filtered[
        (df_filtered['standarutama'].str.contains('Belanja', na=False)) &
        (df_filtered['Namapemda'] != 'Provinsi Jawa Barat')
    ]

    belanja = belanja_df.groupby('Namapemda')['Nilaianggaran'].sum().sort_values(ascending=False)

    top_n = st.slider("Top N Daerah", 5, len(belanja), 10)

    fig = go.Figure(go.Bar(
        x=belanja.head(top_n)/1e12,
        y=belanja.head(top_n).index,
        orientation='h',
        marker=dict(color=belanja.head(top_n).values, colorscale='Blues')
    ))

    fig.update_layout(
        height=520,
        xaxis_title="Triliun Rupiah",
        yaxis_title="Daerah",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# TAB 3: JENIS BELANJA
with tab3:
    st.markdown('<div class="section-title">Belanja Berdasarkan Jenis</div>', unsafe_allow_html=True)

    jenis = df_filtered[
        df_filtered['standarutama'].str.contains('Belanja', na=False)
    ].groupby('standarjenis')['Nilaianggaran'].sum().sort_values()

    fig = go.Figure(go.Bar(
        x=jenis/1e12,
        y=jenis.index,
        orientation='h',
        marker=dict(color=jenis.values, colorscale='Viridis')
    ))

    fig.update_layout(template="plotly_white", height=600)
    st.plotly_chart(fig, use_container_width=True)

# TAB 4: DETAIL DATA
with tab4:
    df_disp = df_filtered.copy()
    df_disp['Nilaianggaran'] = df_disp['Nilaianggaran'].apply(lambda x: f"Rp {x/1e9:.2f} M")

    st.dataframe(
        df_disp[['Namapemda','standarutama','standarjenis','Namaakunobjek','Nilaianggaran']],
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "📥 Download CSV",
        df_disp.to_csv(index=False),
        f"APBD_Jawa_Barat_2020_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        "text/csv"
    )

# FOOTER
st.divider()
st.markdown(
    "<center style='color:#94a3b8;'>Dashboard APBD Jawa Barat 2020 • Streamlit</center>",
    unsafe_allow_html=True
)
