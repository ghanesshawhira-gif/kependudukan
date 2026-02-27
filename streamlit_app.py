import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

# ==============================
# CONFIG
# ==============================

st.set_page_config(
    page_title="Smart City Jakarta 2045",
    page_icon="🌆",
    layout="wide"
)

P0 = 10.56
r_default = 0.0092

# ==============================
# CUSTOM CSS FUTURISTIK
# ==============================

st.markdown("""
<style>

/* Background Gradient Futuristik */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Glass Effect Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,255,255,0.3);
    margin-bottom: 20px;
}

/* Judul */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    background: -webkit-linear-gradient(#00f5ff, #9d4edd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #dcdcdc;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================

st.markdown('<div class="title">🌆 SMART CITY JAKARTA 2045</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simulasi Pertumbuhan Penduduk Berbasis Eksponensial & Logaritma</div>', unsafe_allow_html=True)

st.divider()

# ==============================
# TAB NAVIGATION MODERN
# ==============================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Dashboard",
    "📊 Prediksi",
    "📈 Visualisasi",
    "🧮 Target Logaritma",
    "🌍 Dampak Kota"
])

# ==============================
# TAB 1 - DASHBOARD
# ==============================

with tab1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.latex(r"P(t) = 10.56(1 + r)^t")
    st.write("Model pertumbuhan eksponensial untuk memprediksi populasi Jakarta.")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Populasi 2020", "10.56 Juta")
    col2.metric("Pertumbuhan Rata-rata", "0.92%")
    col3.metric("Jenis Model", "Eksponensial")

# ==============================
# TAB 2 - PREDIKSI
# ==============================

with tab2:
    tahun = st.slider("Pilih Tahun", 2020, 2100, 2035)
    r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Prediksi Populasi", f"{Pt:.2f} Juta")
    col2.metric("Kenaikan", f"{kenaikan:.2f} Juta")
    col3.metric("Total Pertumbuhan", f"{persen:.2f}%")

# ==============================
# TAB 3 - VISUALISASI
# ==============================

with tab3:
    tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)
    r = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92) / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    t_range = tahun_range - 2020
    populasi = P0 * (1 + r) ** t_range

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tahun_range,
        y=populasi,
        mode="lines+markers",
        line=dict(width=4),
        name="Populasi"
    ))

    fig.update_layout(
        template="plotly_dark",
        title="Proyeksi Pertumbuhan Jakarta",
        xaxis_title="Tahun",
        yaxis_title="Populasi (Juta Jiwa)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==============================
# TAB 4 - TARGET LOGARITMA
# ==============================

with tab4:
    target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)
    r = st.slider("Tingkat Pertumbuhan Target (%)", 0.5, 1.5, 0.92) / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r)
        tahun_target = 2020 + t
        st.success(f"🎯 Target tercapai sekitar tahun {int(tahun_target)}")
        st.info(f"Hasil logaritma: t ≈ {t:.2f} tahun")
    else:
        st.error("Target harus lebih besar dari populasi awal.")

# ==============================
# TAB 5 - DAMPAK KOTA
# ==============================

with tab5:
    tahun = st.slider("Simulasi Tahun Dampak", 2020, 2100, 2045)
    r = st.slider("Pertumbuhan (%) Dampak", 0.5, 1.5, 0.92) / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t

    st.subheader(f"Perkiraan Populasi {tahun}: {Pt:.2f} Juta Jiwa")

    if Pt < 11:
        st.info("Kondisi relatif stabil. Infrastruktur masih terkendali.")
    elif Pt < 13:
        st.warning("Potensi peningkatan kemacetan & kebutuhan hunian vertikal.")
    else:
        st.error("Tekanan besar pada transportasi, lingkungan, dan infrastruktur.")
