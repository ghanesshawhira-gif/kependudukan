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

P0 = 10.56  # juta jiwa tahun 2020

# ==============================
# CSS AMAN & STABIL
# ==============================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}
h1, h2, h3 {
    color: #00f5ff;
}
.css-1d391kg {
    background-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================

st.markdown("<h1 style='text-align:center;'>🌆 SMART CITY JAKARTA 2045</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Simulasi Pertumbuhan Penduduk Berbasis Eksponensial & Logaritma</p>", unsafe_allow_html=True)
st.divider()

# ==============================
# TAB MENU
# ==============================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Dashboard",
    "📊 Prediksi",
    "📈 Visualisasi",
    "🧮 Target",
    "🌍 Dampak"
])

# ==============================
# DASHBOARD
# ==============================

with tab1:
    st.latex(r"P(t) = 10.56(1 + r)^t")
    st.write("Model pertumbuhan eksponensial untuk simulasi populasi Jakarta.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Populasi Awal (2020)", "10.56 Juta")
    col2.metric("Rata-rata Pertumbuhan", "0.92%")
    col3.metric("Jenis Model", "Eksponensial")

# ==============================
# PREDIKSI
# ==============================

with tab2:
    tahun_pred = st.slider("Pilih Tahun Prediksi", 2020, 2100, 2035, key="prediksi")
    r_pred = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="r_pred") / 100

    t = tahun_pred - 2020
    Pt = P0 * (1 + r_pred) ** t
    kenaikan = Pt - P0
    persen = (kenaikan / P0) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Prediksi Populasi", f"{Pt:.2f} Juta")
    col2.metric("Kenaikan", f"{kenaikan:.2f} Juta")
    col3.metric("Total Pertumbuhan", f"{persen:.2f}%")

# ==============================
# VISUALISASI
# ==============================

with tab3:
    tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045, key="grafik")
    r_grafik = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92, key="r_grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    t_range = tahun_range - 2020
    populasi = P0 * (1 + r_grafik) ** t_range

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=tahun_range,
        y=populasi,
        mode="lines+markers",
        line=dict(width=3)
    ))

    fig.update_layout(
        template="plotly_dark",
        title="Proyeksi Pertumbuhan Jakarta",
        xaxis_title="Tahun",
        yaxis_title="Populasi (Juta Jiwa)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==============================
# TARGET LOGARITMA
# ==============================

with tab4:
    target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)
    r_target = st.slider("Tingkat Pertumbuhan Target (%)", 0.5, 1.5, 0.92, key="r_target") / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r_target)
        tahun_target = 2020 + t
        st.success(f"🎯 Target tercapai sekitar tahun {int(tahun_target)}")
        st.info(f"Hasil logaritma: t ≈ {t:.2f} tahun")
    else:
        st.error("Target harus lebih besar dari populasi awal.")

# ==============================
# DAMPAK SOSIAL
# ==============================

with tab5:
    tahun_dampak = st.slider("Simulasi Tahun Dampak", 2020, 2100, 2045, key="dampak")
    r_dampak = st.slider("Pertumbuhan Dampak (%)", 0.5, 1.5, 0.92, key="r_dampak") / 100

    t = tahun_dampak - 2020
    Pt = P0 * (1 + r_dampak) ** t

    st.subheader(f"Perkiraan Populasi {tahun_dampak}: {Pt:.2f} Juta Jiwa")

    if Pt < 11:
        st.info("Infrastruktur relatif stabil.")
    elif Pt < 13:
        st.warning("Potensi peningkatan kemacetan & kebutuhan hunian.")
    else:
        st.error("Tekanan besar pada transportasi dan infrastruktur.")
