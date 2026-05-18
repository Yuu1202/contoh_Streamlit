"""
====================================================
STREAMLIT DEMO - INPUT WIDGETS
====================================================
Fitur yang dibahas:
- st.button()
- st.download_button()
- st.checkbox()
- st.toggle()
- st.radio()
- st.selectbox()
- st.multiselect()
- st.slider()
- st.select_slider()
- st.text_input()
- st.text_area()
- st.number_input()
- st.date_input()
- st.time_input()
- st.color_picker()
- st.file_uploader()
- st.form()
====================================================
"""

import streamlit as st
import pandas as pd
from datetime import date, time

st.set_page_config(page_title="Input Widgets", page_icon="🎛️", layout="wide")

st.title("🎛️ Streamlit Input Widgets")
st.write("Semua widget input yang tersedia di Streamlit untuk berinteraksi dengan pengguna.")
st.divider()

# ─────────────────────────────────────────────
# 1. BUTTON
# ─────────────────────────────────────────────
st.header("1. st.button()")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Tombol Biasa"):
        st.success("Tombol biasa diklik!")

with col2:
    if st.button("⚠️ Tombol Bahaya", type="primary"):
        st.error("Ini tombol primary (menonjol)!")

with col3:
    if st.button("🔁 Proses Ulang", use_container_width=True):
        st.info("Lebar penuh container.")

st.divider()

# ─────────────────────────────────────────────
# 2. DOWNLOAD BUTTON
# ─────────────────────────────────────────────
st.header("2. st.download_button()")

df_sample = pd.DataFrame({
    "Nama": ["Alice", "Bob", "Charlie"],
    "Nilai": [90, 85, 78]
})
csv_data = df_sample.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="data_siswa.csv",
    mime="text/csv"
)

st.divider()

# ─────────────────────────────────────────────
# 3. CHECKBOX & TOGGLE
# ─────────────────────────────────────────────
st.header("3. st.checkbox() dan st.toggle()")

col_a, col_b = st.columns(2)
with col_a:
    setuju = st.checkbox("✅ Saya setuju dengan syarat dan ketentuan")
    if setuju:
        st.success("Terima kasih, Anda telah menyetujui!")
    tampilkan_data = st.checkbox("Tampilkan data tabel", value=True)
    if tampilkan_data:
        st.dataframe(df_sample, use_container_width=True)

with col_b:
    mode_gelap = st.toggle("🌙 Mode Gelap")
    if mode_gelap:
        st.info("Mode gelap aktif (ilustrasi).")
    notifikasi = st.toggle("🔔 Aktifkan Notifikasi", value=True)
    st.write(f"Notifikasi: {'Aktif' if notifikasi else 'Nonaktif'}")

st.divider()

# ─────────────────────────────────────────────
# 4. RADIO
# ─────────────────────────────────────────────
st.header("4. st.radio()")

col_r1, col_r2 = st.columns(2)
with col_r1:
    metode = st.radio(
        "Pilih metode pembayaran:",
        options=["💳 Kartu Kredit", "🏦 Transfer Bank", "🔄 Dompet Digital", "💵 Tunai"],
        index=0
    )
    st.write(f"Dipilih: **{metode}**")

with col_r2:
    tampilan = st.radio(
        "Tampilan grafik:",
        options=["Line", "Bar", "Area"],
        horizontal=True   # ditampilkan horizontal
    )
    st.write(f"Tampilan: **{tampilan}**")

st.divider()

# ─────────────────────────────────────────────
# 5. SELECTBOX & MULTISELECT
# ─────────────────────────────────────────────
st.header("5. st.selectbox() dan st.multiselect()")

col_s1, col_s2 = st.columns(2)
with col_s1:
    kota = st.selectbox(
        "🏙️ Pilih kota:",
        options=["Surabaya", "Jakarta", "Bandung", "Yogyakarta", "Bali", "Medan"],
        index=0
    )
    st.write(f"Kota terpilih: **{kota}**")

with col_s2:
    hobi = st.multiselect(
        "🎯 Pilih hobi (bisa lebih dari satu):",
        options=["Membaca", "Gaming", "Memasak", "Olahraga", "Coding", "Musik", "Traveling"],
        default=["Coding", "Membaca"]
    )
    st.write(f"Hobi: {', '.join(hobi) if hobi else 'Belum dipilih'}")

st.divider()

# ─────────────────────────────────────────────
# 6. SLIDER & SELECT SLIDER
# ─────────────────────────────────────────────
st.header("6. st.slider() dan st.select_slider()")

col_sl1, col_sl2 = st.columns(2)

with col_sl1:
    umur = st.slider("🎂 Umur:", min_value=1, max_value=100, value=25, step=1)
    st.write(f"Umur: **{umur} tahun**")

    rentang_harga = st.slider(
        "💰 Rentang harga (Rp):",
        min_value=0, max_value=1_000_000,
        value=(100_000, 500_000), step=50_000,
        format="Rp %d"
    )
    st.write(f"Harga: Rp {rentang_harga[0]:,} — Rp {rentang_harga[1]:,}")

with col_sl2:
    ukuran = st.select_slider(
        "👕 Ukuran baju:",
        options=["XS", "S", "M", "L", "XL", "XXL"],
        value="M"
    )
    st.write(f"Ukuran: **{ukuran}**")

    kecepatan = st.select_slider(
        "⚡ Kecepatan koneksi:",
        options=["1 Mbps", "5 Mbps", "10 Mbps", "50 Mbps", "100 Mbps", "1 Gbps"],
        value="10 Mbps"
    )
    st.write(f"Kecepatan: **{kecepatan}**")

st.divider()

# ─────────────────────────────────────────────
# 7. TEXT INPUT & TEXT AREA
# ─────────────────────────────────────────────
st.header("7. st.text_input() dan st.text_area()")

col_t1, col_t2 = st.columns(2)
with col_t1:
    nama = st.text_input("👤 Nama lengkap:", placeholder="Masukkan nama Anda...")
    email = st.text_input("📧 Email:", placeholder="contoh@email.com")
    password = st.text_input("🔒 Password:", type="password")

    if nama:
        st.write(f"Halo, **{nama}**!")

with col_t2:
    pesan = st.text_area(
        "💬 Pesan / Deskripsi:",
        placeholder="Tulis pesan Anda di sini...",
        height=150
    )
    st.write(f"Jumlah karakter: **{len(pesan)}**")

st.divider()

# ─────────────────────────────────────────────
# 8. NUMBER INPUT
# ─────────────────────────────────────────────
st.header("8. st.number_input()")

col_n1, col_n2 = st.columns(2)
with col_n1:
    qty = st.number_input("🛒 Jumlah barang:", min_value=1, max_value=100, value=1, step=1)
    harga_satuan = st.number_input("💵 Harga satuan (Rp):", min_value=0, value=50000, step=1000)
    total = qty * harga_satuan
    st.success(f"Total: **Rp {total:,}**")

with col_n2:
    suhu = st.number_input("🌡️ Suhu (°C):", min_value=-50.0, max_value=100.0, value=36.5, step=0.1, format="%.1f")
    if suhu >= 37.5:
        st.error(f"⚠️ Suhu {suhu}°C — kemungkinan demam!")
    else:
        st.info(f"Suhu {suhu}°C — normal.")

st.divider()

# ─────────────────────────────────────────────
# 9. DATE & TIME INPUT
# ─────────────────────────────────────────────
st.header("9. st.date_input() dan st.time_input()")

col_d1, col_d2 = st.columns(2)
with col_d1:
    tanggal_lahir = st.date_input(
        "📅 Tanggal lahir:",
        value=date(1995, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )
    st.write(f"Tanggal lahir: **{tanggal_lahir.strftime('%d %B %Y')}**")

    rentang_tanggal = st.date_input(
        "📆 Rentang tanggal perjalanan:",
        value=(date(2024, 6, 1), date(2024, 6, 7))
    )
    st.write(f"Perjalanan: {rentang_tanggal}")

with col_d2:
    jam_mulai = st.time_input("⏰ Jam mulai:", value=time(8, 0))
    jam_selesai = st.time_input("⏱️ Jam selesai:", value=time(17, 0))
    st.write(f"Jadwal: **{jam_mulai.strftime('%H:%M')}** — **{jam_selesai.strftime('%H:%M')}**")

st.divider()

# ─────────────────────────────────────────────
# 10. COLOR PICKER
# ─────────────────────────────────────────────
st.header("10. st.color_picker()")

col_c1, col_c2 = st.columns(2)
with col_c1:
    warna_utama = st.color_picker("🎨 Pilih warna utama:", value="#4f9cf9")
    st.markdown(
        f'<div style="background:{warna_utama}; padding:20px; border-radius:8px; color:white; font-weight:bold;">Warna Utama: {warna_utama}</div>',
        unsafe_allow_html=True
    )

with col_c2:
    warna_aksen = st.color_picker("✨ Pilih warna aksen:", value="#f97316")
    st.markdown(
        f'<div style="background:{warna_aksen}; padding:20px; border-radius:8px; color:white; font-weight:bold;">Warna Aksen: {warna_aksen}</div>',
        unsafe_allow_html=True
    )

st.divider()

# ─────────────────────────────────────────────
# 11. FILE UPLOADER
# ─────────────────────────────────────────────
st.header("11. st.file_uploader()")

col_f1, col_f2 = st.columns(2)

with col_f1:
    file_csv = st.file_uploader("📂 Upload file CSV:", type=["csv"])
    if file_csv is not None:
        df_upload = pd.read_csv(file_csv)
        st.write(f"File: **{file_csv.name}** ({file_csv.size} bytes)")
        st.dataframe(df_upload.head(), use_container_width=True)

with col_f2:
    file_gambar = st.file_uploader("🖼️ Upload gambar:", type=["jpg", "jpeg", "png"])
    if file_gambar is not None:
        st.image(file_gambar, caption=f"Gambar: {file_gambar.name}", use_container_width=True)

st.divider()

# ─────────────────────────────────────────────
# 12. FORM (batch input)
# ─────────────────────────────────────────────
st.header("12. st.form()")
st.write("Form mengelompokkan input agar diproses sekaligus saat tombol Submit diklik.")

with st.form("form_registrasi"):
    st.subheader("📋 Form Registrasi")
    col_form1, col_form2 = st.columns(2)

    with col_form1:
        f_nama = st.text_input("Nama lengkap *", placeholder="John Doe")
        f_email = st.text_input("Email *", placeholder="john@email.com")
        f_kota = st.selectbox("Kota", ["Surabaya", "Jakarta", "Bandung", "Bali"])

    with col_form2:
        f_umur = st.number_input("Umur", min_value=1, max_value=120, value=25)
        f_gender = st.radio("Gender", ["Laki-laki", "Perempuan"], horizontal=True)
        f_tanggal = st.date_input("Tanggal bergabung")

    f_bio = st.text_area("Bio singkat", placeholder="Ceritakan tentang diri Anda...")
    f_setuju = st.checkbox("Saya menyetujui syarat dan ketentuan *")

    submitted = st.form_submit_button("📨 Daftar Sekarang", use_container_width=True, type="primary")

    if submitted:
        if not f_nama or not f_email:
            st.error("⚠️ Nama dan email wajib diisi!")
        elif not f_setuju:
            st.warning("⚠️ Harap setujui syarat dan ketentuan.")
        else:
            st.success(f"✅ Registrasi berhasil! Selamat datang, **{f_nama}**!")
            st.json({
                "nama": f_nama, "email": f_email, "kota": f_kota,
                "umur": f_umur, "gender": f_gender,
                "tanggal": str(f_tanggal), "bio": f_bio
            })

st.divider()

# ─────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────
st.header("📋 Ringkasan Input Widgets")
ringkasan = pd.DataFrame({
    "Widget": [
        "st.button()", "st.download_button()", "st.checkbox()", "st.toggle()",
        "st.radio()", "st.selectbox()", "st.multiselect()", "st.slider()",
        "st.select_slider()", "st.text_input()", "st.text_area()",
        "st.number_input()", "st.date_input()", "st.time_input()",
        "st.color_picker()", "st.file_uploader()", "st.form()"
    ],
    "Kegunaan": [
        "Tombol aksi", "Tombol unduh file", "Pilihan centang tunggal", "Toggle on/off",
        "Pilihan satu dari beberapa", "Dropdown pilihan tunggal", "Dropdown multi-pilih",
        "Geser nilai numerik/range", "Geser nilai dari opsi teks", "Input teks satu baris",
        "Input teks multi-baris", "Input angka dengan batas min/max",
        "Input tanggal / rentang tanggal", "Input jam", "Pemilih warna hex",
        "Upload file dari komputer", "Grup input dengan tombol submit"
    ]
})
st.dataframe(ringkasan, use_container_width=True, hide_index=True)