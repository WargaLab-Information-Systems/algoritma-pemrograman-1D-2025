# Fungsi untuk menghitung total tagihan listrik
def hitung_tagihan(kwh):
    tarif = 1500
    total = kwh * tarif
    return total

# Fungsi untuk menentukan kategori penggunaan listrik
def kategori_penggunaan(kwh):
    if kwh >= 500:
        return "Penggunaan Tinggi"
    else:
        return "Penggunaan Normal"

# Program utama
print("=== Program Hitung Tagihan Listrik PLN ===")
kwh = float(input("Masukkan jumlah pemakaian listrik (kWh): "))

# Hitung total tagihan dan kategori
total_tagihan = hitung_tagihan(kwh)
kategori = kategori_penggunaan(kwh)

# Tampilkan hasil
print("\n--- Hasil Perhitungan ---")
print(f"Total Tagihan: Rp {total_tagihan:,.0f}")
print(f"Kategori Penggunaan: {kategori}")
