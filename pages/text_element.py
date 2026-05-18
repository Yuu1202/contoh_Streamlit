"""
====================================================
STREAMLIT DEMO - TEXT ELEMENTS
====================================================
Fitur yang dibahas:
- st.title()
- st.header()
- st.subheader()
- st.text()
- st.markdown()
- st.caption()
- st.code()
- st.latex()
- st.write()
- st.divider()
====================================================
"""

import streamlit as st

st.set_page_config(page_title="Text Elements", page_icon="📝", layout="wide")

# ─────────────────────────────────────────────
# 1. TITLE
# ─────────────────────────────────────────────
st.title("📝 Streamlit Text Elements")
st.write("Halaman ini menampilkan semua elemen teks yang tersedia di Streamlit.")

st.divider()

# ─────────────────────────────────────────────
# 2. HEADER & SUBHEADER
# ─────────────────────────────────────────────
st.header("1. Header")
st.write("Digunakan untuk judul bagian utama.")

st.subheader("1.1 Subheader")
st.write("Digunakan untuk sub-bagian di bawah header.")

st.divider()

# ─────────────────────────────────────────────
# 3. TEXT BIASA
# ─────────────────────────────────────────────
st.header("2. st.text()")
st.text("Ini adalah teks biasa. Font monospace, tidak mendukung Markdown.")
st.text("Cocok untuk menampilkan data plain atau log sederhana.")

st.divider()

# ─────────────────────────────────────────────
# 4. MARKDOWN
# ─────────────────────────────────────────────
st.header("3. st.markdown()")

st.markdown("**Bold**, *Italic*, ~~Strikethrough~~, `inline code`")
st.markdown("# H1 via Markdown")
st.markdown("## H2 via Markdown")
st.markdown("### H3 via Markdown")
st.markdown("""
**List item:**
- Item A
- Item B
- Item C

**Ordered list:**
1. Pertama
2. Kedua
3. Ketiga
""")
st.markdown("> 💡 Ini adalah blockquote. Bisa digunakan untuk highlight informasi penting.")
st.markdown("[Klik di sini untuk ke Google](https://www.google.com)")

# Markdown dengan HTML (unsafe_allow_html)
st.markdown(
    '<p style="color:tomato; font-size:20px; font-weight:bold;">Teks warna merah dengan HTML</p>',
    unsafe_allow_html=True
)

st.divider()

# ─────────────────────────────────────────────
# 5. CAPTION
# ─────────────────────────────────────────────
st.header("4. st.caption()")
st.image("https://picsum.photos/400/200", caption="Gambar acak dari internet")
st.caption("Caption: Digunakan untuk keterangan kecil di bawah gambar atau elemen lain.")

st.divider()

# ─────────────────────────────────────────────
# 6. CODE
# ─────────────────────────────────────────────
st.header("5. st.code()")

python_code = """
def greet(name: str) -> str:
    \"\"\"Fungsi untuk menyapa pengguna.\"\"\"
    return f"Halo, {name}! Selamat datang di Streamlit."

print(greet("Budi"))
"""

sql_code = """
SELECT 
    nama, 
    COUNT(*) AS total_transaksi,
    SUM(nominal) AS total_nilai
FROM transaksi
WHERE tanggal >= '2024-01-01'
GROUP BY nama
ORDER BY total_nilai DESC;
"""

st.code(python_code, language="python")
st.code(sql_code, language="sql")

# Inline code lewat markdown
st.markdown("Gunakan `st.code()` untuk menampilkan blok kode dengan syntax highlighting.")

st.divider()

# ─────────────────────────────────────────────
# 7. LATEX
# ─────────────────────────────────────────────
st.header("6. st.latex()")
st.write("Menampilkan rumus matematika dengan format LaTeX:")

st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} f(x)\,dx = F(b) - F(a)")
st.latex(r"\bar{X} = \frac{1}{n}\sum_{i=1}^{n} x_i")
st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")

st.divider()

# ─────────────────────────────────────────────
# 8. ST.WRITE (Swiss Army Knife)
# ─────────────────────────────────────────────
st.header("7. st.write() — Si Serbaguna")
st.write("st.write() bisa menampilkan hampir semua tipe data:")

st.write("String biasa")
st.write(12345)
st.write(3.14)
st.write(True)
st.write(["apel", "mangga", "jeruk"])
st.write({"nama": "Budi", "umur": 25, "kota": "Surabaya"})

import pandas as pd
df_contoh = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.write("Dataframe via st.write():", df_contoh)

st.divider()

# ─────────────────────────────────────────────
# 9. DIVIDER
# ─────────────────────────────────────────────
st.header("8. st.divider()")
st.write("Garis pembatas horizontal untuk memisahkan bagian:")
st.divider()
st.write("Bagian setelah divider.")

st.divider()

# ─────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────
st.header("📋 Ringkasan Elemen Teks")

data_ringkasan = {
    "Fungsi": [
        "st.title()", "st.header()", "st.subheader()",
        "st.text()", "st.markdown()", "st.caption()",
        "st.code()", "st.latex()", "st.write()", "st.divider()"
    ],
    "Kegunaan": [
        "Judul utama halaman",
        "Judul bagian besar",
        "Judul sub-bagian",
        "Teks plain/monospace",
        "Teks dengan format Markdown & HTML",
        "Teks kecil/keterangan",
        "Blok kode dengan syntax highlighting",
        "Rumus matematika LaTeX",
        "Menampilkan hampir semua tipe data",
        "Garis pemisah horizontal"
    ]
}

st.dataframe(pd.DataFrame(data_ringkasan))