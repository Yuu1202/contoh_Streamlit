import streamlit as st

# Mengatur konfigurasi halaman utama
st.set_page_config(
    page_title="Aplikasi Dashboard Utama",
    page_icon="👋",
    layout="wide"
)

# Konten di halaman utama
st.title("Selamat Datang di Aplikasi Streamlit Saya! 🚀")
st.write("""
    Ini adalah halaman utama (Home). Silakan gunakan menu di **sidebar sebelah kiri** 
    untuk berpindah ke halaman-halaman analisis lainnya.
""")

# Kamu juga bisa menambahkan ringkasan atau panduan di sini
st.info("Pilih salah satu menu di samping untuk memulai!")