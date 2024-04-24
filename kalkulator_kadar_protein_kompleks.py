import streamlit as st

# Judul dan deskripsi
st.title("Perhitungan Kadar Protein dalam Produk Pangan")
st.write("Aplikasi ini menghitung kadar protein dalam produk pangan berdasarkan berbagai parameter.")

# Pilih jenis produk
produk_pilihan = st.selectbox(
    "Pilih jenis produk:",
    ["Daging", "Susu", "Telur", "Kacang-kacangan", "Sereal", "Sayuran", "Buah-buahan"]
)

# Input berat produk dalam gram
berat_produk = st.number_input(
    "Masukkan berat produk (gram):",
    min_value=0.0,
    step=0.1,
    format="%.1f"
)

# Input konsentrasi protein dalam persentase (default disesuaikan dengan jenis produk)
default_protein = {
    "Daging": 26.0,
    "Susu": 3.5,
    "Telur": 12.0,
    "Kacang-kacangan": 25.0,
    "Sereal": 10.0,
    "Sayuran": 3.0,
    "Buah-buahan": 1.0
}

konsentrasi_protein = st.number_input(
    f"Masukkan konsentrasi protein dalam {produk_pilihan} (persentase):",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    format="%.1f",
    value=default_protein[produk_pilihan]
)

# Tombol untuk menghitung
if st.button("Hitung Kadar Protein"):
    # Validasi input
    if berat_produk <= 0 or konsentrasi_protein < 0 or konsentrasi_protein > 100:
        st.error("Input tidak valid. Pastikan berat produk lebih dari 0 dan konsentrasi protein antara 0 dan 100.")
    else:
        # Hitung kadar protein
        kadar_protein = (berat_produk * konsentrasi_protein) / 100

        # Tampilkan hasil
        st.success(f"Kadar protein dalam {produk_pilihan} adalah {kadar_protein:.2f} gram.")