import streamlit as st
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import time
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Cyber Smart City Jakarta", layout="wide")

P0 = 10.56

# =========================
# CYBER CSS + HOLOGRAM
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #050510;
    color: #00f5ff;
}

/* Hologram header */
.holo {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#00f5ff;
    text-shadow:0 0 10px #00f5ff, 0 0 20px #00f5ff, 0 0 40px #9d4edd;
    animation: flicker 2s infinite alternate;
}

@keyframes flicker {
  from {opacity:0.8;}
  to {opacity:1;}
}

/* Metric glow */
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
# SOUND EFFECT FUNCTION
# =========================
def play_sound():
    beep = """
    <audio autoplay>
    <source src="https://www.soundjay.com/button/sounds/button-16.mp3" type="audio/mpeg">
    </audio>
    """
    st.markdown(beep, unsafe_allow_html=True)

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
# TAB 1 - PREDIKSI + SOUND
# =========================
with tab1:
    tahun = st.slider("Tahun Prediksi", 2020, 2100, 2035)
    r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    play_sound()
    with st.spinner("⚡ Cyber calculation running..."):
        time.sleep(1)

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Populasi", f"{Pt:.2f} Juta")
    col2.metric("Kenaikan", f"{kenaikan:.2f} Juta")
    col3.metric("Pertumbuhan", f"{persen:.2f}%")

# =========================
# TAB 2 - NEON GLOW GRAPH
# =========================
with tab2:
    tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)
    r_grafik = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92, key="grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    populasi = P0 * (1 + r_grafik) ** (tahun_range - 2020)

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#050510')
    ax.set_facecolor('#050510')

    # Neon glow effect (plot multiple lines)
    for lw, alpha in [(10,0.05),(6,0.1),(4,0.3)]:
        ax.plot(tahun_range, populasi, color='#00f5ff', linewidth=lw, alpha=alpha)

    ax.plot(tahun_range, populasi, color='#00f5ff', linewidth=2)

    ax.set_title("Neon Population Growth", color='#00f5ff')
    ax.set_xlabel("Tahun", color='#00f5ff')
    ax.set_ylabel("Populasi (Juta)", color='#00f5ff')
    ax.tick_params(colors='#00f5ff')

    st.pyplot(fig)

# =========================
# TAB 3 - TARGET
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
# TAB 4 - AI RISK SCORE
# =========================
with tab4:
    tahun_ai = st.slider("Tahun Analisis", 2020, 2100, 2045, key="ai")
    r_ai = st.slider("Pertumbuhan (%)", 0.5, 1.5, 0.92, key="rai") / 100

    Pt_ai = P0 * (1 + r_ai) ** (tahun_ai - 2020)

    # Risk Score Algorithm
    risk_score = (Pt_ai - 10.56) * 10

    st.write(f"Populasi Prediksi: {Pt_ai:.2f} Juta Jiwa")
    st.write(f"Risk Score: {risk_score:.1f}")

    if risk_score < 10:
        st.success("🟢 Risiko Rendah – Kota stabil & terkendali.")
    elif risk_score < 25:
        st.warning("🟡 Risiko Sedang – Perlu peningkatan infrastruktur.")
    elif risk_score < 40:
        st.error("🟠 Risiko Tinggi – Tekanan urban meningkat signifikan.")
    else:
        st.error("🔴 KRITIS – Overpopulasi ekstrem, perlu kebijakan besar.")
