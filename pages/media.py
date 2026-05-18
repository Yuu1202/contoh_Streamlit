"""
====================================================
STREAMLIT DEMO - MEDIA ELEMENTS
====================================================
Fitur yang dibahas:
- st.image()
- st.audio()
- st.video()
- st.camera_input()
- st.logo()
- Menampilkan media dari URL, file lokal, dan numpy array
- PIL Image manipulation + tampil di Streamlit
- OpenCV frame + tampil di Streamlit
====================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import io

st.set_page_config(page_title="Media Elements", page_icon="🎬", layout="wide")

# ─────────────────────────────────────────────
# LOGO (ditampilkan di sidebar)
# ─────────────────────────────────────────────
# st.logo() menampilkan gambar kecil di pojok atas sidebar
# st.logo("assets/logo.png")   # uncomment jika file tersedia

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.title("🎬 Streamlit Media Elements")
st.write("Semua cara menampilkan gambar, audio, video, dan kamera di Streamlit.")
st.divider()

# ─────────────────────────────────────────────
# 1. ST.IMAGE — DARI URL
# ─────────────────────────────────────────────
st.header("1. st.image()")

st.subheader("1a. Gambar dari URL")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://picsum.photos/seed/nature/400/300",
        caption="🌿 Gambar Alam (URL)",
        use_container_width=True
    )

with col2:
    st.image(
        "https://picsum.photos/seed/city/400/300",
        caption="🏙️ Gambar Kota (URL)",
        use_container_width=True
    )

with col3:
    st.image(
        "https://picsum.photos/seed/tech/400/300",
        caption="💻 Gambar Teknologi (URL)",
        use_container_width=True
    )

st.divider()

# ─────────────────────────────────────────────
# 2. ST.IMAGE — NUMPY ARRAY (generate dengan PIL)
# ─────────────────────────────────────────────
st.subheader("1b. Gambar dari Numpy Array / PIL")
st.write("Gambar bisa dibuat langsung dari array NumPy atau objek PIL tanpa file eksternal.")

col_img1, col_img2 = st.columns(2)

# Gradien warna — numpy array
with col_img1:
    st.write("**Gradien Warna (NumPy)**")
    gradient = np.zeros((200, 400, 3), dtype=np.uint8)
    gradient[:, :, 0] = np.linspace(0, 255, 400)    # Red
    gradient[:, :, 1] = np.linspace(255, 0, 400)    # Green
    gradient[:, :, 2] = 128                          # Blue konstan
    st.image(gradient, caption="Gradien RGB via NumPy", use_container_width=True)

# Noise — numpy array
with col_img2:
    st.write("**Noise Acak (NumPy)**")
    noise = np.random.randint(0, 255, (200, 400, 3), dtype=np.uint8)
    st.image(noise, caption="Random Noise via NumPy", use_container_width=True)

st.divider()

# ─────────────────────────────────────────────
# 3. PIL IMAGE MANIPULATION
# ─────────────────────────────────────────────
st.subheader("1c. Manipulasi Gambar dengan PIL + Streamlit")

# Buat gambar PIL programatik
def buat_gambar_pil(teks: str, bg_color: tuple, text_color: tuple) -> Image.Image:
    img = Image.new("RGB", (400, 200), color=bg_color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 390, 190], outline=text_color, width=3)
    draw.text((200, 100), teks, fill=text_color, anchor="mm")
    return img

col_pil1, col_pil2, col_pil3, col_pil4 = st.columns(4)

with col_pil1:
    img_asli = buat_gambar_pil("ORIGINAL", (70, 130, 180), (255, 255, 255))
    st.image(img_asli, caption="Original", use_container_width=True)

with col_pil2:
    img_grayscale = img_asli.convert("L")
    st.image(img_grayscale, caption="Grayscale", use_container_width=True)

with col_pil3:
    img_blur = img_asli.filter(ImageFilter.GaussianBlur(radius=5))
    st.image(img_blur, caption="Gaussian Blur", use_container_width=True)

with col_pil4:
    enhancer = ImageEnhance.Brightness(img_asli)
    img_bright = enhancer.enhance(1.8)
    st.image(img_bright, caption="Brightness +80%", use_container_width=True)

# Slider untuk brightness real-time
st.write("**Atur Kecerahan Gambar Secara Real-Time:**")
brightness_val = st.slider("Kecerahan:", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
img_base = buat_gambar_pil("Adjust Me!", (30, 100, 150), (255, 220, 50))
enhancer_rt = ImageEnhance.Brightness(img_base)
img_rt = enhancer_rt.enhance(brightness_val)
st.image(img_rt, caption=f"Brightness: {brightness_val}x", width=400)

# Download gambar hasil manipulasi
buf = io.BytesIO()
img_rt.save(buf, format="PNG")
st.download_button(
    "⬇️ Download Gambar",
    data=buf.getvalue(),
    file_name="hasil_manipulasi.png",
    mime="image/png"
)

st.divider()

# ─────────────────────────────────────────────
# 4. MULTIPLE IMAGES (list)
# ─────────────────────────────────────────────
st.subheader("1d. Multiple Images sekaligus (list)")

urls = [
    "https://picsum.photos/seed/a1/300/200",
    "https://picsum.photos/seed/b2/300/200",
    "https://picsum.photos/seed/c3/300/200",
]
captions = ["Gambar 1", "Gambar 2", "Gambar 3"]

st.image(urls, caption=captions, width=250)

st.divider()

# ─────────────────────────────────────────────
# 5. ST.IMAGE — DARI FILE LOKAL
# ─────────────────────────────────────────────
st.subheader("1e. Dari File Lokal (anggap tersedia)")
st.info("""
Jika file gambar ada di direktori lokal, gunakan:

```python
st.image("assets/foto_produk.jpg", caption="Foto Produk", width=400)
st.image("assets/banner.png", use_container_width=True)

# Atau buka dulu dengan PIL:
from PIL import Image
img = Image.open("assets/foto_produk.jpg")
st.image(img, caption="Dibuka via PIL")
```

File yang didukung: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`
""")

st.divider()

# ─────────────────────────────────────────────
# 6. ST.AUDIO
# ─────────────────────────────────────────────
st.header("2. st.audio()")

st.subheader("2a. Audio dari URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url, format="audio/mp3")

st.subheader("2b. Audio dari Numpy (Sine Wave)")
st.write("Membuat gelombang sinus dan memutarnya langsung di Streamlit:")

sample_rate = 22050
frekuensi = st.slider("Frekuensi (Hz):", min_value=100, max_value=1000, value=440, step=10)
durasi = st.slider("Durasi (detik):", min_value=0.5, max_value=3.0, value=1.0, step=0.5)

t = np.linspace(0, durasi, int(sample_rate * durasi))
gelombang = (np.sin(2 * np.pi * frekuensi * t) * 32767).astype(np.int16)

st.audio(gelombang, sample_rate=sample_rate)
st.caption(f"Gelombang sinus {frekuensi} Hz selama {durasi} detik")

st.subheader("2c. Audio dari File Lokal (anggap tersedia)")
st.info("""
```python
# File lokal
st.audio("assets/podcast_episode.mp3", format="audio/mp3")
st.audio("assets/efek_suara.wav", format="audio/wav")

# Dengan start_time
st.audio("assets/lagu.mp3", start_time=30)  # mulai dari detik ke-30

# Autoplay (tidak selalu diizinkan browser)
st.audio("assets/notif.mp3", autoplay=True)
```
Format yang didukung: `.mp3`, `.wav`, `.ogg`, `.flac`
""")

st.divider()

# ─────────────────────────────────────────────
# 7. ST.VIDEO
# ─────────────────────────────────────────────
st.header("3. st.video()")

st.subheader("3a. Video dari URL (YouTube / direct link)")

col_v1, col_v2 = st.columns(2)

with col_v1:
    st.write("**YouTube:**")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.caption("Video YouTube embed langsung")

with col_v2:
    st.write("**Direct MP4 URL:**")
    # Video pendek open-source
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.caption("Direct MP4 file via URL")

st.subheader("3b. Video dengan subtitles")
st.info("""
```python
# Video dengan file subtitle (.vtt)
st.video(
    "assets/tutorial.mp4",
    subtitles={
        "Indonesian": "assets/subtitle_id.vtt",
        "English": "assets/subtitle_en.vtt"
    }
)
```
""")

st.subheader("3c. Video dari File Lokal (anggap tersedia)")
st.info("""
```python
# File lokal
st.video("assets/demo_video.mp4", format="video/mp4")
st.video("assets/screen_record.webm", format="video/webm")

# Dengan start_time
st.video("assets/tutorial.mp4", start_time=60)  # mulai menit ke-1

# Autoplay + loop (untuk background video / showcase)
st.video("assets/loop.mp4", autoplay=True, loop=True, muted=True)
```

Format yang didukung: `.mp4`, `.webm`, `.ogg`, `.mkv` (tergantung browser)
""")

st.divider()
# ─────────────────────────────────────────────
# 8. ST.CAMERA_INPUT (DENGAN TOMBOL AKTIVASI)
# ─────────────────────────────────────────────
st.header("4. st.camera_input()")
st.write("Mengambil foto langsung dari kamera perangkat (webcam).")

# Inisialisasi session state untuk status kamera aktif atau tidak
if "kamera_aktif" not in st.session_state:
    st.session_state.kamera_aktif = False

# Jika kamera belum aktif, tampilkan tombol untuk mengaktifkan
if not st.session_state.kamera_aktif:
    st.info("Kamera dinonaktifkan untuk kenyamanan Anda. Klik tombol di bawah untuk mengaktifkan.")
    if st.button("📸 Aktifkan Kamera"):
        st.session_state.kamera_aktif = True
        st.rerun()  # Memuat ulang halaman untuk memunculkan kamera

else:
    # Tombol untuk mematikan kembali kamera jika user selesai
    if st.button("❌ Matikan Kamera"):
        st.session_state.kamera_aktif = False
        st.rerun()

    st.divider()

    # Layout kolom untuk kamera dan hasil filter
    col_cam1, col_cam2 = st.columns([1, 1])

    with col_cam1:
        # Kamera baru akan muncul di sini setelah user menekan tombol aktifkan
        foto = st.camera_input("📷 Ambil foto sekarang:")

    with col_cam2:
        if foto is not None:
            st.write("**Foto yang diambil:**")
            img_foto = Image.open(foto)

            # Pilihan filter
            filter_pilihan = st.selectbox(
                "Terapkan filter:",
                ["Original", "Grayscale", "Sepia", "Blur", "Contour"]
            )

            if filter_pilihan == "Grayscale":
                img_hasil = img_foto.convert("L").convert("RGB")
            elif filter_pilihan == "Sepia":
                img_gray = np.array(img_foto.convert("L"))
                sepia = np.stack([
                    np.clip(img_gray * 1.1, 0, 255),
                    np.clip(img_gray * 0.9, 0, 255),
                    np.clip(img_gray * 0.7, 0, 255),
                ], axis=-1).astype(np.uint8)
                img_hasil = Image.fromarray(sepia)
            elif filter_pilihan == "Blur":
                img_hasil = img_foto.filter(ImageFilter.GaussianBlur(radius=8))
            elif filter_pilihan == "Contour":
                img_hasil = img_foto.filter(ImageFilter.CONTOUR)
            else:
                img_hasil = img_foto

            st.image(img_hasil, caption=f"Filter: {filter_pilihan}", use_container_width=True)

            # Download foto hasil
            buf_cam = io.BytesIO()
            img_hasil.save(buf_cam, format="PNG")
            st.download_button(
                "⬇️ Download Foto",
                data=buf_cam.getvalue(),
                file_name=f"foto_{filter_pilihan.lower()}.png",
                mime="image/png",
                use_container_width=True
            )
        else:
            st.info("Klik tombol jepret pada kamera untuk mengambil foto. Filter akan diterapkan secara real-time.")

st.divider()

# ─────────────────────────────────────────────
# 9. LIVE WEBCAM STREAM (pattern)
# ─────────────────────────────────────────────
st.header("5. Pola Live Stream dengan st.empty()")
st.info("""
Untuk streaming webcam / frame-by-frame (misal dengan OpenCV), gunakan pola berikut:

```python
import cv2
import streamlit as st

frame_placeholder = st.empty()
stop_button = st.button("⏹️ Stop")

cap = cv2.VideoCapture(0)

while cap.isOpened() and not stop_button:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Konversi BGR → RGB untuk Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Tampilkan frame di placeholder (update terus-menerus)
    frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

cap.release()
```
""")

st.divider()

# ─────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────
st.header("📋 Ringkasan Media Elements")

ringkasan = pd.DataFrame({
    "Fungsi": [
        "st.image(url)", "st.image(numpy_array)", "st.image(pil_image)",
        "st.image([url1, url2])", "st.audio(url)", "st.audio(numpy_array, sample_rate)",
        "st.video(url)", "st.video(file_path)", "st.camera_input()", "st.logo()"
    ],
    "Kegunaan": [
        "Tampilkan gambar dari URL internet",
        "Tampilkan array NumPy sebagai gambar",
        "Tampilkan objek PIL Image (mendukung manipulasi)",
        "Tampilkan beberapa gambar sekaligus",
        "Putar audio dari URL (mp3, wav, dll)",
        "Putar audio dari data NumPy (sine wave, TTS, dll)",
        "Embed video dari URL atau YouTube",
        "Putar video dari file lokal",
        "Ambil foto dari kamera/webcam pengguna",
        "Logo kecil di pojok atas sidebar"
    ],
    "Format Didukung": [
        ".jpg .png .gif .webp .bmp",
        "uint8 shape (H,W,3) atau (H,W)",
        "PIL.Image object",
        "List of URL/array/PIL",
        ".mp3 .wav .ogg .flac",
        "int16/float32 numpy array",
        "YouTube / direct .mp4 .webm",
        ".mp4 .webm .ogg",
        "Snapshot dari kamera perangkat",
        ".png .jpg"
    ]
})
st.dataframe(ringkasan, use_container_width=True, hide_index=True)