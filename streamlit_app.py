import streamlit as st
import numpy as np
import math
import pandas as pd

# =========================
# CONFIG RESPONSIVE
# =========================
st.set_page_config(
    page_title="Jakarta Executive Population Simulator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

P0 = 10.56

# =========================
# RESPONSIVE CSS
# =========================
st.markdown("""
<style>

/* Center Content Max Width */
.main .block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Background */
.stApp {
    background-color: #f4f6f9;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #0b3c5d;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 16px;
    color: #555;
    margin-bottom: 20px;
}

/* Card */
.section-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

/* Metric Style */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.05);
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-title {
        font-size: 22px;
    }
    .subtitle {
        font-size: 14px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='main-title'>🌆 JAKARTA EXECUTIVE POPULATION SIMULATOR</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Simulasi Pertumbuhan Penduduk Berbasis Model Eksponensial & Logaritma</div>", unsafe_allow_html=True)
st.divider()

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
    with st.container():
        tahun = st.slider("Tahun Prediksi", 2020, 2100, 2035)
        r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

        t = tahun - 2020
        Pt = P0 * (1 + r) ** t
        kenaikan = Pt - P0
        persen = (kenaikan / P0) * 100

        st.divider()

        col1, col2, col3 = st.columns(3)
        col1.metric("Prediksi Populasi", f"{Pt:.2f} Juta")
        col2.metric("Total Kenaikan", f"{kenaikan:.2f} Juta")
        col3.metric("Pertumbuhan (%)", f"{persen:.2f}%")

# =========================
# TAB 2 - GRAFIK
# =========================
with tab2:
    with st.container():
        tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)
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
# TAB 3 - TARGET
# =========================
with tab3:
    with st.container():
        target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)
        r_target = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="target") / 100

        if target > P0:
            t = math.log(target / P0) / math.log(1 + r_target)
            tahun_target = 2020 + t
            st.success(f"Target diperkirakan tercapai pada tahun {int(tahun_target)}")
            st.info(f"Hasil logaritma: t ≈ {t:.2f} tahun")
        else:
            st.error("Target harus lebih besar dari populasi awal.")

# =========================
# TAB 4 - DAMPAK
# =========================
with tab4:
    with st.container():
        tahun_dampak = st.slider("Tahun Dampak", 2020, 2100, 2045)
        r_dampak = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="dampak") / 100

        t = tahun_dampak - 2020
        Pt = P0 * (1 + r_dampak) ** t

        st.subheader(f"Perkiraan Populasi Tahun {tahun_dampak}: {Pt:.2f} Juta Jiwa")

        if Pt < 11:
            st.info("Kondisi relatif stabil.")
        elif Pt < 13:
            st.warning("Potensi peningkatan kepadatan & transportasi.")
        else:
            st.error("Tekanan tinggi terhadap infrastruktur dan lingkungan.")
