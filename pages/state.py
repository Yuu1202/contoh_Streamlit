import streamlit as st
import pandas as pd
import time
import numpy as np

st.set_page_config(page_title="Logic & Performance", layout="wide")

st.title("Jantung Streamlit: Caching & State 🧠")
st.write("Dua fitur inilah yang membedakan script Python biasa dengan Web App yang powerful.")

# ─────────────────────────────────────────────────────────
# 1. CACHING (Optimasi Performa)
# ─────────────────────────────────────────────────────────
st.header("1. st.cache_data (Gudang Data)")
st.write("Digunakan untuk menyimpan hasil fungsi yang 'mahal' atau berat.")

@st.cache_data
def ambil_data_raksasa():
    # Simulasi proses berat (seperti koneksi database atau API)
    time.sleep(3) 
    data = pd.DataFrame(
        np.random.randn(10, 5),
        columns=[f'Kolom {i+1}' for i in range(5)]
    )
    return data

st.write("Klik tombol di bawah. Pertama kali akan butuh 3 detik, kedua kali akan instan!")

if st.button("Ambil Data"):
    start = time.time()
    df = ambil_data_raksasa()
    st.dataframe(df)
    st.success(f"Selesai dalam {time.time() - start:.2f} detik")

st.divider()

# ─────────────────────────────────────────────────────────
# 2. SESSION STATE (Memori Aplikasi)
# ─────────────────────────────────────────────────────────
st.header("2. st.session_state (Catatan User)")
st.write("Digunakan agar aplikasi ingat pilihan user saat script dijalankan ulang.")

# Inisialisasi state agar tidak error
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

item_baru = st.text_input("Masukkan barang ke keranjang belanja:")

if st.button("Tambah ke Keranjang"):
    if item_baru:
        st.session_state.keranjang.append(item_baru)
        st.toast(f"{item_baru} ditambahkan!")

st.subheader("Isi Keranjang Anda saat ini:")
if st.session_state.keranjang:
    for i, item in enumerate(st.session_state.keranjang):
        st.write(f"{i+1}. {item}")
else:
    st.write("Keranjang masih kosong.")

if st.button("Kosongkan Keranjang"):
    st.session_state.keranjang = []
    st.rerun()