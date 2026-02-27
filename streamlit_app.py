import streamlit as st
import numpy as np
import math
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Dashboard Monitoring Kependudukan Jakarta",
    layout="wide"
)

P0 = 10.56  # juta jiwa tahun 2020

# =========================
# TEMA PEMERINTAH
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f4f6f9;
}

h1 {
    color: #1f4e79;
    text-align: center;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>🏛 DASHBOARD MONITORING KEPENDUDUKAN JAKARTA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Sistem Pemantauan Pertumbuhan Penduduk Berbasis Model Eksponensial</p>", unsafe_allow_html=True)
st.divider()

# =========================
# TAB MENU
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Ringkasan Indikator",
    "📈 Monitoring Grafik",
    "🧮 Analisis Target",
    "🌍 Analisis Dampak"
])

# =========================
# TAB 1 - RINGKASAN INDIKATOR
# =========================
with tab1:
    st.subheader("📊 Ringkasan Indikator Kependudukan")

    col1, col2 = st.columns(2)

    with col1:
        tahun = st.slider("Tahun Evaluasi", 2020, 2100, 2035)

    with col2:
        r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    st.divider()

    k1, k2, k3 = st.columns(3)
    k1.metric("Populasi Tahun Dipilih", f"{Pt:.2f} Juta Jiwa")
    k2.metric("Kenaikan dari 2020", f"{kenaikan:.2f} Juta Jiwa")
    k3.metric("Total Pertumbuhan", f"{persen:.2f}%")

# =========================
# TAB 2 - MONITORING GRAFIK
# =========================
with tab2:
    st.subheader("📈 Monitoring Pertumbuhan Tahunan")

    tahun_akhir = st.slider("Tahun Akhir Monitoring", 2025, 2100, 2045)
    r_grafik = st.slider("Pertumbuhan Tahunan (%)", 0.5, 1.5, 0.92, key="grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    t_range = tahun_range - 2020
    populasi = P0 * (1 + r_grafik) ** t_range

    df = pd.DataFrame({
        "Tahun": tahun_range,
        "Populasi (Juta Jiwa)": populasi
    })

    st.line_chart(df.set_index("Tahun"), use_container_width=True)

# =========================
# TAB 3 - ANALISIS TARGET
# =========================
with tab3:
    st.subheader("🧮 Analisis Target Kependudukan")

    col1, col2 = st.columns(2)

    with col1:
        target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)

    with col2:
        r_target = st.slider("Pertumbuhan (%)", 0.5, 1.5, 0.92, key="target") / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r_target)
        tahun_target = 2020 + t
        st.success(f"Target diperkirakan tercapai pada tahun {int(tahun_target)}")
        st.info(f"Hasil perhitungan logaritma: t ≈ {t:.2f} tahun")
    else:
        st.error("Target harus lebih besar dari populasi awal tahun 2020.")

# =========================
# TAB 4 - ANALISIS DAMPAK
# =========================
with tab4:
    st.subheader("🌍 Analisis Dampak Perencanaan Wilayah")

    col1, col2 = st.columns(2)

    with col1:
        tahun_dampak = st.slider("Tahun Proyeksi", 2020, 2100, 2045)

    with col2:
        r_dampak = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="dampak") / 100

    t = tahun_dampak - 2020
    Pt = P0 * (1 + r_dampak) ** t

    st.subheader(f"Perkiraan Populasi: {Pt:.2f} Juta Jiwa")

    if Pt < 11:
        st.info("Kapasitas infrastruktur masih dalam batas aman.")
    elif Pt < 13:
        st.warning("Perlu peningkatan transportasi massal dan hunian vertikal.")
    else:
        st.error("Diperlukan kebijakan strategis untuk mengendalikan kepadatan dan beban infrastruktur.")
