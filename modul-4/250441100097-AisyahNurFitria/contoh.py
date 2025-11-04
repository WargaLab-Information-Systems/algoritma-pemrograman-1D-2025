def hitung_tagihan(kwh):
    tarif = 1500  # tarif dasar per kWh
    total = kwh * tarif
    return total

# Fungsi untuk menentukan kategori penggunaan listrik
def kategori_penggunaan(kwh):
    if kwh >= 500:
        return "Penggunaan Tinggi"
    else:
        return "Penggunaan Normal"

# Program utama
pemakaian = float(input("Masukkan jumlah pemakaian listrik (kWh): "))

total_tagihan = hitung_tagihan(pemakaian)
kategori = kategori_penggunaan(pemakaian)

print("\n===HASIL PERHITUNGAN===")
print(f"Pemakaian Listrik : {pemakaian} kWh")
print(f"Total Tagihan     : Rp {total_tagihan:,.0f}")
print(f"Kategori          : {kategori}")