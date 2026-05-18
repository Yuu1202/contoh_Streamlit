import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Data Display Native", page_icon="📊", layout="wide")

st.title("📊 Streamlit Data Display (Native)")
st.write("Menampilkan data menggunakan fitur bawaan Streamlit tanpa library eksternal tambahan.")
st.divider()

# ─────────────────────────────────────────────
# DATA DUMMY (Hanya pakai Pandas & Numpy)
# ─────────────────────────────────────────────
np.random.seed(42)
bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
         "Jul", "Ags", "Sep", "Okt", "Nov", "Des"]

df_penjualan = pd.DataFrame({
    "Bulan": bulan,
    "Penjualan": np.random.randint(8000, 20000, 12),
    "Target":    np.random.randint(10000, 18000, 12),
    "Biaya":     np.random.randint(3000, 8000, 12),
    "Keuntungan": np.random.randint(2000, 10000, 12),
    "Kategori":  np.random.choice(["A", "B", "C"], 12)
})

df_karyawan = pd.DataFrame({
    "Nama":       ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Divisi":     ["IT", "HR", "Finance", "IT", "Marketing"],
    "Gaji":       [12000000, 9000000, 11000000, 13000000, 10000000],
    "Aktif":      [True, True, False, True, True],
    "Rating":     [4.5, 3.8, 4.1, 4.9, 3.5],
})

# ─────────────────────────────────────────────
# 1. ST.DATAFRAME & ST.DATA_EDITOR
# ─────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.header("1. st.dataframe()")
    st.write("Tabel interaktif (bisa diurutkan & difilter).")
    st.dataframe(df_penjualan, use_container_width=True, hide_index=True)

with col_right:
    st.header("2. st.data_editor()")
    st.write("Tabel yang bisa diedit langsung.")
    edited_df = st.data_editor(df_karyawan, use_container_width=True, num_rows="dynamic")

st.divider()

# ─────────────────────────────────────────────
# 2. ST.METRIC (KPI Dashboard)
# ─────────────────────────────────────────────
st.header("3. st.metric()")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Penjualan", f"Rp {df_penjualan['Penjualan'].sum():,}", "+12%")
c2.metric("Rata-rata Profit", f"Rp {int(df_penjualan['Keuntungan'].mean()):,}", "-3%")
c3.metric("Efisiensi Biaya", "85%", "+5%")
c4.metric("Kepuasan Klien", "4.8 / 5.0", "0.2")

st.divider()

# ─────────────────────────────────────────────
# 3. NATIVE CHARTS (Tanpa Plotly/Altair)
# ─────────────────────────────────────────────
st.header("4. Native Charts (Streamlit Built-in)")
st.write("Grafik ini sangat cepat dan otomatis menyesuaikan tema (Dark/Light).")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])

with tab1:
    st.subheader("Tren Penjualan vs Target")
    # Streamlit butuh index untuk sumbu X pada chart bawaan
    chart_data = df_penjualan.set_index("Bulan")[["Penjualan", "Target"]]
    st.line_chart(chart_data)

with tab2:
    st.subheader("Perbandingan Penjualan per Bulan")
    st.bar_chart(df_penjualan.set_index("Bulan")["Penjualan"])

with tab3:
    st.subheader("Distribusi Keuntungan")
    st.area_chart(df_penjualan.set_index("Bulan")["Keuntungan"])

st.divider()

# ─────────────────────────────────────────────
# 4. ST.JSON & ST.TABLE
# ─────────────────────────────────────────────
st.header("5. Format Lainnya")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("st.json()")
    st.json({"status": "Success", "code": 200, "data": {"user": "Admin", "role": "Full Access"}})

with col_b:
    st.subheader("st.table()")
    st.write("Tabel statis (cocok untuk ringkasan kecil)")
    st.table(df_karyawan.head(3))

# ─────────────────────────────────────────────
# SUMMARY TABLE
# ─────────────────────────────────────────────
st.header("📋 Ringkasan Fitur")
summary_data = {
    "Fungsi": ["st.dataframe", "st.data_editor", "st.metric", "st.line_chart", "st.json"],
    "Keunggulan": ["Interaktif", "Bisa diedit", "Indikator KPI", "Visualisasi Cepat", "Format Struktur Data"]
}
st.table(pd.DataFrame(summary_data))