import streamlit as st
import numpy as np
import math
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Jakarta Executive Population Simulator",
    layout="wide"
)

P0 = 10.56

# =========================
# ELEGANT MODERN THEME
# =========================
st.markdown("""
<style>

/* Background clean elegan */
.stApp {
    background-color: #f4f6f9;
}

/* Header Style */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #0b3c5d;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

/* Section Card */
.section-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Accent line */
hr {
    border: 2px solid #d4af37;
}

/* Metric spacing */
[data-testid="metric-container"] {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='main-title'>🌆 JAKARTA EXECUTIVE POPULATION SIMULATOR</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analisis Pertumbuhan Penduduk Berbasis Model Eksponensial & Logaritma</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# TAB NAVIGATION
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Prediksi",
    "📈 Grafik",
    "🧮 Target",
    "🌍 Dampak Kota"
])

# =========================
# TAB 1 - PREDIKSI
# =========================
with tab1:
    st.markdown("### 📊 Simulasi Prediksi Populasi")

    col1, col2 = st.columns(2)

    with col1:
        tahun = st.slider("Tahun Prediksi", 2020, 2100, 2035)

    with col2:
        r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    st.divider()

    k1, k2, k3 = st.columns(3)
    k1.metric("Prediksi Populasi", f"{Pt:.2f} Juta Jiwa")
    k2.metric("Total Kenaikan", f"{kenaikan:.2f} Juta Jiwa")
    k3.metric("Persentase Pertumbuhan", f"{persen:.2f}%")

# =========================
# TAB 2 - GRAFIK
# =========================
with tab2:
    st.markdown("### 📈 Visualisasi Pertumbuhan")

    col1, col2 = st.columns(2)

    with col1:
        tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)

    with col2:
        r_grafik = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92, key="grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    t_range = tahun_range - 2020
    populasi = P0 * (1 + r_grafik) ** t_range

    df = pd.DataFrame({
        "Tahun": tahun_range,
        "Populasi (Juta Jiwa)": populasi
    })

    st.line_chart(df.set_index("Tahun"), use_container_width=True)

# =========================
# TAB 3 - TARGET LOGARITMA
# =========================
with tab3:
    st.markdown("### 🎯 Analisis Target Populasi")

    col1, col2 = st.columns(2)

    with col1:
        target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)

    with col2:
        r_target = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="target") / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r_target)
        tahun_target = 2020 + t
        st.success(f"Target diperkirakan tercapai pada tahun {int(tahun_target)}")
        st.info(f"Hasil perhitungan logaritma: t ≈ {t:.2f} tahun")
    else:
        st.error("Target harus lebih besar dari populasi awal 2020.")

# =========================
# TAB 4 - DAMPAK
# =========================
with tab4:
    st.markdown("### 🌍 Simulasi Dampak Perkotaan")

    col1, col2 = st.columns(2)

    with col1:
        tahun_dampak = st.slider("Tahun Dampak", 2020, 2100, 2045)

    with col2:
        r_dampak = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="dampak") / 100

    t = tahun_dampak - 2020
    Pt = P0 * (1 + r_dampak) ** t

    st.subheader(f"Perkiraan Populasi Tahun {tahun_dampak}: {Pt:.2f} Juta Jiwa")

    if Pt < 11:
        st.info("Kondisi relatif stabil dengan tekanan infrastruktur rendah.")
    elif Pt < 13:
        st.warning("Potensi peningkatan kepadatan dan kebutuhan transportasi massal.")
    else:
        st.error("Tekanan tinggi terhadap transportasi, hunian, dan lingkungan.")
        
