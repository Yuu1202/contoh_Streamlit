"""
====================================================
STREAMLIT DEMO - LAYOUT & CONTAINER
====================================================
Fitur yang dibahas:
- st.columns()
- st.container()
- st.empty()
- st.expander()
- st.tabs()
- st.sidebar
- st.popover()
- st.dialog()
- st.spinner()
- st.status()
- st.progress()
- st.toast()
- st.balloons() / st.snow()
====================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Layout & Container", page_icon="🧱", layout="wide")

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.image("https://picsum.photos/200/80?grayscale", use_container_width=True)
    st.title("🧱 Layout Demo")
    st.divider()

    st.subheader("⚙️ Pengaturan")
    tema = st.selectbox("Tema warna:", ["Biru", "Hijau", "Merah"])
    tampilkan_kode = st.toggle("Tampilkan hint kode", value=True)

    st.divider()
    st.subheader("👤 Profil")
    st.text("Nama: Admin")
    st.text("Role: Developer")
    st.text("Versi: 1.0.0")

    st.divider()
    st.caption("Streamlit Layout & Container Demo")

# ─────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────
st.title("🧱 Streamlit Layout & Container")
st.write("Semua cara mengatur tata letak (layout) dan kontainer di Streamlit.")
st.divider()

# ─────────────────────────────────────────────
# 1. COLUMNS
# ─────────────────────────────────────────────
st.header("1. st.columns()")

# Kolom sama rata
st.subheader("Kolom 3 sama rata")
c1, c2, c3 = st.columns(3)
c1.metric("🛒 Pesanan", "1,284", "+12%")
c2.metric("👥 Pengguna", "5,921", "+8%")
c3.metric("💰 Revenue", "Rp 182 jt", "+23%")

if tampilkan_kode:
    st.code("c1, c2, c3 = st.columns(3)", language="python")

# Kolom rasio berbeda
st.subheader("Kolom rasio 2:1:1")
col_main, col_side1, col_side2 = st.columns([2, 1, 1])

with col_main:
    st.info("Kolom lebar (rasio 2) — cocok untuk konten utama")
    df_mini = pd.DataFrame({"X": range(5), "Y": np.random.randint(1, 10, 5)})
    st.line_chart(df_mini.set_index("X"), height=150)

with col_side1:
    st.warning("Kolom kecil (rasio 1)")
    for i in range(3):
        st.metric(f"KPI {i+1}", np.random.randint(50, 200))

with col_side2:
    st.error("Kolom kecil (rasio 1)")
    st.write("Bisa diisi info, tombol, atau widget lain.")
    st.button("Aksi 1", use_container_width=True)
    st.button("Aksi 2", use_container_width=True)

if tampilkan_kode:
    st.code("col_main, col_side1, col_side2 = st.columns([2, 1, 1])", language="python")

# Kolom dengan gap
st.subheader("Kolom dengan gap='large'")
col_gap1, col_gap2 = st.columns(2, gap="large")
col_gap1.success("Kolom kiri — gap besar antar kolom")
col_gap2.success("Kolom kanan — gap besar antar kolom")

st.divider()

# ─────────────────────────────────────────────
# 2. CONTAINER
# ─────────────────────────────────────────────
st.header("2. st.container()")

with st.container(border=True):
    st.subheader("📦 Container dengan Border")
    st.write("Container membungkus elemen menjadi satu grup visual.")
    col1, col2 = st.columns(2)
    col1.metric("Item A", "42", "+5")
    col2.metric("Item B", "87", "-3")
    st.bar_chart({"Nilai A": [10, 20, 30], "Nilai B": [15, 25, 20]}, height=150)

# Container tanpa border tapi dengan height (scrollable)
with st.container(height=200, border=True):
    st.write("📜 **Container scrollable** (height=200):")
    for i in range(1, 20):
        st.write(f"Baris data ke-{i} — Lorem ipsum dolor sit amet...")

if tampilkan_kode:
    st.code("""
with st.container(border=True):
    st.write("Konten dalam container")

with st.container(height=200):
    # Jika konten melebihi height, muncul scrollbar
    for i in range(20):
        st.write(f"Baris {i}")
""", language="python")

st.divider()

# ─────────────────────────────────────────────
# 3. EMPTY
# ─────────────────────────────────────────────
st.header("3. st.empty()")
st.write("Placeholder dinamis yang bisa diisi/diupdate saat runtime.")

placeholder = st.empty()

if st.button("▶️ Jalankan Counter"):
    for i in range(1, 6):
        placeholder.metric("Counter", i, f"+1 (detik ke-{i})")
        time.sleep(0.8)
    placeholder.success("✅ Counter selesai!")

if tampilkan_kode:
    st.code("""
placeholder = st.empty()
for i in range(5):
    placeholder.metric("Counter", i)
    time.sleep(1)
placeholder.success("Selesai!")
""", language="python")

st.divider()

# ─────────────────────────────────────────────
# 4. EXPANDER
# ─────────────────────────────────────────────
st.header("4. st.expander()")

with st.expander("📖 Lihat Penjelasan Lengkap", expanded=False):
    st.write("""
    `st.expander()` berguna untuk menyembunyikan konten panjang yang opsional,
    seperti dokumentasi, detail teknis, atau penjelasan tambahan.
    """)
    st.code("with st.expander('Judul'): st.write('Konten tersembunyi')", language="python")

with st.expander("📊 Detail Data Penjualan", expanded=True):
    df_detail = pd.DataFrame({
        "Produk": ["A", "B", "C", "D"],
        "Stok": [120, 45, 300, 80],
        "Terjual": [95, 30, 250, 60]
    })
    st.dataframe(df_detail, use_container_width=True, hide_index=True)

with st.expander("⚙️ Konfigurasi Lanjutan"):
    st.slider("Learning Rate", 0.0001, 0.1, 0.001, format="%.4f")
    st.number_input("Epochs", 1, 1000, 100)
    st.selectbox("Optimizer", ["Adam", "SGD", "RMSprop"])

st.divider()

# ─────────────────────────────────────────────
# 5. TABS
# ─────────────────────────────────────────────
st.header("5. st.tabs()")

tab1, tab2, tab3, tab4 = st.tabs(["📈 Grafik", "📋 Tabel", "🗺️ Peta", "📝 Log"])

with tab1:
    st.subheader("Grafik Tren Bulanan")
    data_chart = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["Produk A", "Produk B", "Produk C"]
    )
    st.area_chart(data_chart)

with tab2:
    st.subheader("Tabel Transaksi")
    df_transaksi = pd.DataFrame({
        "ID": range(1, 11),
        "Pelanggan": [f"Customer {i}" for i in range(1, 11)],
        "Nominal": np.random.randint(50000, 500000, 10),
        "Status": np.random.choice(["Sukses", "Pending", "Gagal"], 10)
    })
    st.dataframe(df_transaksi, use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Lokasi Cabang (Ilustrasi)")
    df_lokasi = pd.DataFrame({
        "lat": [-7.25, -6.21, -6.91, -8.65],
        "lon": [112.75, 106.85, 107.61, 115.22],
        "cabang": ["Surabaya", "Jakarta", "Bandung", "Bali"]
    })
    st.map(df_lokasi)

with tab4:
    st.subheader("Log Aktivitas")
    log_entries = [
        "2024-01-15 08:00 — Sistem dimulai",
        "2024-01-15 08:05 — User admin login",
        "2024-01-15 09:10 — Data diperbarui",
        "2024-01-15 11:30 — Laporan digenerate",
        "2024-01-15 17:00 — Sistem dimatikan",
    ]
    for log in log_entries:
        st.code(log)

st.divider()

# ─────────────────────────────────────────────
# 6. POPOVER
# ─────────────────────────────────────────────
st.header("6. st.popover()")
st.write("Popup kecil yang muncul saat tombol diklik.")

col_pop1, col_pop2 = st.columns(2)
with col_pop1:
    with st.popover("ℹ️ Info Detail"):
        st.subheader("Detail Produk")
        st.write("**Nama:** Widget Pro Max")
        st.write("**Harga:** Rp 299.000")
        st.write("**Stok:** 42 unit")
        st.image("https://picsum.photos/200/100", use_container_width=True)

with col_pop2:
    with st.popover("⚙️ Filter Data"):
        kategori_filter = st.selectbox("Kategori:", ["Semua", "A", "B", "C"])
        status_filter = st.multiselect("Status:", ["Aktif", "Nonaktif", "Pending"])
        st.button("Terapkan Filter", use_container_width=True, type="primary")

st.divider()

# ─────────────────────────────────────────────
# 7. DIALOG (MODAL)
# ─────────────────────────────────────────────
st.header("7. @st.dialog()")
st.write("Dialog modal yang muncul di atas konten halaman.")

@st.dialog("🗑️ Konfirmasi Hapus")
def dialog_hapus():
    st.warning("Apakah Anda yakin ingin menghapus item ini? Tindakan ini tidak bisa dibatalkan.")
    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("Ya, Hapus", type="primary", use_container_width=True):
            st.session_state["hasil_dialog"] = "dihapus"
            st.rerun()
    with col_no:
        if st.button("Batal", use_container_width=True):
            st.session_state["hasil_dialog"] = "dibatalkan"
            st.rerun()

if st.button("🗑️ Hapus Data"):
    dialog_hapus()

if "hasil_dialog" in st.session_state:
    aksi = st.session_state["hasil_dialog"]
    if aksi == "dihapus":
        st.error(f"✅ Item berhasil {aksi}.")
    else:
        st.info(f"Aksi {aksi}.")

st.divider()

# ─────────────────────────────────────────────
# 8. SPINNER & STATUS
# ─────────────────────────────────────────────
st.header("8. st.spinner() dan st.status()")

col_sp1, col_sp2 = st.columns(2)

with col_sp1:
    st.subheader("st.spinner()")
    if st.button("⏳ Proses dengan Spinner"):
        with st.spinner("Memuat data, harap tunggu..."):
            time.sleep(2)
        st.success("✅ Data berhasil dimuat!")

with col_sp2:
    st.subheader("st.status()")
    if st.button("🔄 Proses dengan Status"):
        with st.status("Menjalankan pipeline...") as status:
            st.write("📡 Menghubungkan ke server...")
            time.sleep(1)
            st.write("📥 Mengunduh data...")
            time.sleep(1)
            st.write("🔧 Memproses data...")
            time.sleep(1)
            status.update(label="✅ Pipeline selesai!", state="complete", expanded=True)

st.divider()

# ─────────────────────────────────────────────
# 9. PROGRESS BAR
# ─────────────────────────────────────────────
st.header("9. st.progress()")

if st.button("📊 Jalankan Progress"):
    progress_bar = st.progress(0, text="Memulai proses...")
    for pct in range(0, 101, 5):
        time.sleep(0.05)
        progress_bar.progress(pct, text=f"Memproses... {pct}%")
    progress_bar.empty()
    st.success("✅ Proses selesai 100%!")

if tampilkan_kode:
    st.code("""
bar = st.progress(0)
for i in range(0, 101, 10):
    bar.progress(i, text=f"{i}%")
    time.sleep(0.1)
""", language="python")

st.divider()

# ─────────────────────────────────────────────
# 10. TOAST, BALLOONS, SNOW
# ─────────────────────────────────────────────
st.header("10. st.toast(), st.balloons(), st.snow()")

col_eff1, col_eff2, col_eff3 = st.columns(3)

with col_eff1:
    if st.button("🍞 Tampilkan Toast", use_container_width=True):
        st.toast("🎉 Operasi berhasil!", icon="✅")
        time.sleep(0.3)
        st.toast("📧 Email terkirim!", icon="📨")

with col_eff2:
    if st.button("🎈 Balon!", use_container_width=True):
        st.balloons()

with col_eff3:
    if st.button("❄️ Salju!", use_container_width=True):
        st.snow()

st.divider()

# ─────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────
st.header("📋 Ringkasan Layout & Container")
ringkasan = pd.DataFrame({
    "Komponen": [
        "st.sidebar", "st.columns()", "st.container()", "st.empty()",
        "st.expander()", "st.tabs()", "st.popover()", "@st.dialog()",
        "st.spinner()", "st.status()", "st.progress()",
        "st.toast()", "st.balloons()", "st.snow()"
    ],
    "Fungsi": [
        "Panel samping untuk navigasi & pengaturan",
        "Tata letak kolom horizontal",
        "Grup elemen dalam satu kotak (bisa border/scroll)",
        "Placeholder dinamis yang bisa diupdate",
        "Konten yang bisa disembunyikan/dibuka",
        "Navigasi tab horizontal",
        "Popup kecil saat tombol diklik",
        "Modal/dialog di atas halaman",
        "Animasi loading bulat",
        "Status pipeline langkah demi langkah",
        "Bar kemajuan proses",
        "Notifikasi pop-up singkat",
        "Efek balon melayang saat sukses",
        "Efek salju turun saat sukses"
    ]
})
st.dataframe(ringkasan, use_container_width=True, hide_index=True)