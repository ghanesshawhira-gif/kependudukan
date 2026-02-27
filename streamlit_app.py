import streamlit as st
import numpy as np
import math
import pandas as pd

st.set_page_config(page_title="Smart City Jakarta 2045", layout="wide")

P0 = 10.56

st.title("🌆 SMART CITY JAKARTA 2045")
st.write("Simulasi Pertumbuhan Penduduk Berbasis Eksponensial & Logaritma")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Prediksi",
    "📈 Grafik",
    "🧮 Target",
    "🌍 Dampak"
])

# ======================
# PREDIKSI
# ======================
with tab1:
    tahun = st.slider("Tahun Prediksi", 2020, 2100, 2035)
    r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92) / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t

    st.metric("Prediksi Populasi", f"{Pt:.2f} Juta Jiwa")

# ======================
# GRAFIK (Tanpa Plotly)
# ======================
with tab2:
    tahun_akhir = st.slider("Tahun Akhir Grafik", 2025, 2100, 2045)
    r = st.slider("Pertumbuhan Grafik (%)", 0.5, 1.5, 0.92, key="grafik") / 100

    tahun_range = np.arange(2020, tahun_akhir + 1)
    t_range = tahun_range - 2020
    populasi = P0 * (1 + r) ** t_range

    df = pd.DataFrame({
        "Tahun": tahun_range,
        "Populasi (Juta Jiwa)": populasi
    })

    st.line_chart(df.set_index("Tahun"))

# ======================
# TARGET LOGARITMA
# ======================
with tab3:
    target = st.number_input("Target Populasi (Juta Jiwa)", 11.0, 20.0, 12.0)
    r = st.slider("Tingkat Pertumbuhan (%)", 0.5, 1.5, 0.92, key="target") / 100

    if target > P0:
        t = math.log(target / P0) / math.log(1 + r)
        tahun_target = 2020 + t
        st.success(f"Target tercapai sekitar tahun {int(tahun_target)}")
    else:
        st.error("Target harus lebih besar dari populasi awal.")

# ======================
# DAMPAK
# ======================
with tab4:
    tahun = st.slider("Tahun Dampak", 2020, 2100, 2045, key="dampak")
    r = st.slider("Pertumbuhan Dampak (%)", 0.5, 1.5, 0.92, key="r_dampak") / 100

    t = tahun - 2020
    Pt = P0 * (1 + r) ** t

    st.subheader(f"Perkiraan Populasi: {Pt:.2f} Juta Jiwa")

    if Pt < 11:
        st.info("Infrastruktur relatif stabil.")
    elif Pt < 13:
        st.warning("Potensi peningkatan kemacetan & kebutuhan hunian.")
    else:
        st.error("Tekanan besar pada transportasi dan infrastruktur.")
