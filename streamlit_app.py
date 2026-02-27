import streamlit as st
import numpy as np
import math
import pandas as pd
import time

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Cyber Smart City Jakarta", layout="wide")

P0 = 10.56

# =========================
# CYBER CSS (NO EXTRA LIB)
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #050510;
    color: #00f5ff;
}

/* Hologram Header */
.holo {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#00f5ff;
    text-shadow:0 0 10px #00f5ff, 0 0 30px #9d4edd;
    animation:flicker 2s infinite alternate;
}

@keyframes flicker {
  from {opacity:0.85;}
  to {opacity:1;}
}

/* Metric Glow */
[data-testid="metric-container"] {
    background:#0f0f1a;
    border:1px solid #00f5ff;
    border-radius:12px;
    box-shadow:0 0 15px #00f5ff;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="holo">⚡ CYBER SMART CITY JAKARTA 2045</div>', unsafe_allow_html=True)
st.markdown("<center>AI Powered Urban Growth Simulator</center>", unsafe_allow_html=True)
st.divider()

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Prediksi",
    "📈 Neon Grafik",
    "🧮 Target",
    "🧠 AI Risk Analysis"
])

# =========================
# TAB 1 - PREDIKSI
# =========================
with tab1:
    tahun = st.slider("Tahun Prediksi", 2020, 2100, 2035)
    r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    with st.spinner("⚡ Cyber calculation running..."):
        time.sleep(1)

    Pt = P0 * (1 + r) ** (tahun - 2020)
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Populasi", f"{Pt:.2f} Juta")
    col2.metric("Kenaikan", f"{kenaikan:.2f} Juta")
    col3.metric("Pertumbuhan", f"{persen:.2f}%")

# =========================
# TAB 2 - NEON STYLE GRAPH (SAFE)
# =========================
with tab2:
    tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)
    r_grafik = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92, key="grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    populasi = P0 * (1 + r_grafik) ** (tahun_range - 2020)

    df = pd.DataFrame({
        "Tahun": tahun_range,
        "Populasi (Juta Jiwa)": populasi
    })

    st.line_chart(df.set_index("Tahun"), use_container_width=True)

# =========================
# TAB 3 - TARGET LOG
# =========================
with tab3:
    target = st.number_input("Target Populasi", 11.0, 20.0, 12.0)
    r_target = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="target") / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r_target)
        tahun_target = 2020 + t
        st.success(f"Target tercapai sekitar tahun {int(tahun_target)}")
    else:
        st.error("Target harus lebih besar dari populasi awal.")

# =========================
# TAB 4 - AI RISK ANALYSIS
# =========================
with tab4:
    tahun_ai = st.slider("Tahun Analisis", 2020, 2100, 2045, key="ai")
    r_ai = st.slider("Pertumbuhan (%)", 0.5, 1.5, 0.92, key="rai") / 100

    Pt_ai = P0 * (1 + r_ai) ** (tahun_ai - 2020)
    risk_score = (Pt_ai - 10.56) * 10

    st.write(f"Populasi Prediksi: {Pt_ai:.2f} Juta Jiwa")
    st.write(f"Risk Score: {risk_score:.1f}")

    if risk_score < 10:
        st.success("🟢 Risiko Rendah – Kota stabil.")
    elif risk_score < 25:
        st.warning("🟡 Risiko Sedang – Perlu peningkatan infrastruktur.")
    elif risk_score < 40:
        st.error("🟠 Risiko Tinggi – Tekanan urban meningkat.")
    else:
        st.error("🔴 KRITIS – Overpopulasi ekstrem.")
