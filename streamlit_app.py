st.markdown("""
<style>

/* Background terang elegan */
.stApp {
    background-color: #f4f6f9;
}

/* Konten utama */
.main .block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Judul */
.main-title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #0b3c5d;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 15px;
    color: #333333;
    margin-bottom: 20px;
}

/* Semua teks default jadi gelap */
html, body, [class*="css"]  {
    color: #1f2937;
}

/* Card */
.section-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

/* Metric */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.05);
}

/* Mobile font adjustment */
@media (max-width: 768px) {
    .main-title {
        font-size: 20px;
    }
    .subtitle {
        font-size: 13px;
    }
}

</style>
""", unsafe_allow_html=True)
