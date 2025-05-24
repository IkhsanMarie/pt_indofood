import streamlit as st
import matplotlib.pyplot as plt

# Fungsi-fungsi utama
def total_waktu_produksi(x, y):
    return 2 * x**2 + 3 * x * y + y**2

def turunan_parsial(x, y):
    dT_dx = 4 * x + 3 * y
    dT_dy = 3 * x + 2 * y
    return dT_dx, dT_dy

def waktu_baku(waktu_normal, toleransi):
    return waktu_normal * (1 + toleransi)

# Judul Aplikasi
st.title("🔧 Aplikasi Analisis Waktu Baku Produksi Mobil")

# Input Pengguna
st.sidebar.header("📥 Input Data Aktivitas Produksi")
x = st.sidebar.number_input("Waktu Perakitan Mesin (x) [jam]", min_value=0.0, value=2.0, step=0.5)
y = st.sidebar.number_input("Waktu Pemasangan Bodi (y) [jam]", min_value=0.0, value=3.0, step=0.5)
toleransi = st.sidebar.slider("Toleransi (%)", 0, 30, 15, 1)

# Perhitungan
waktu_total = total_waktu_produksi(x, y)
dT_dx, dT_dy = turunan_parsial(x, y)
wb = waktu_baku(waktu_total, toleransi / 100)

# Output Hasil
st.header("📊 Hasil Perhitungan Waktu Produksi")
st.write(f"**Total Waktu Produksi (T):** {waktu_total:.2f} jam")
st.write(f"**Turunan Parsial terhadap x (∂T/∂x):** {dT_dx:.2f}")
st.write(f"**Turunan Parsial terhadap y (∂T/∂y):** {dT_dy:.2f}")
st.write(f"**Waktu Baku (dengan toleransi {toleransi}%):** {wb:.2f} jam")

# Grafik Pengaruh Aktivitas
st.subheader("📈 Grafik Pengaruh Aktivitas terhadap Waktu Produksi")

fig, ax = plt.subplots()
aktivitas = ['Perakitan Mesin (x)', 'Pemasangan Bodi (y)']
pengaruh = [dT_dx, dT_dy]
warna = ['#FF6F61', '#6BAED6']

bars = ax.bar(aktivitas, pengaruh, color=warna)
ax.set_ylabel("Pengaruh terhadap Total Waktu (jam)")
ax.set_title("Turunan Parsial ∂T/∂x dan ∂T/∂y")
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Tambahkan label di atas bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.1f}', ha='center', va='bottom', fontweight='bold')

st.pyplot(fig)
