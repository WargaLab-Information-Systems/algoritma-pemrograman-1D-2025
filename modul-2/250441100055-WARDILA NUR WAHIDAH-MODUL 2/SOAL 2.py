# Program menghitung harga tiket bioskop

# Input data penonton
usia = int(input("Masukkan usia penonton: "))
pelajar = input("Apakah pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari menonton: ").capitalize()

# Harga tiket normal
harga_normal = 50000
diskon = 0

# Menentukan diskon berdasarkan kondisi
if usia < 12:
    diskon = 0.5
elif pelajar == "ya":
    diskon = 0.3
elif hari == "Selasa":
    diskon = 0.2

# Hitung harga akhir
harga_akhir = harga_normal - (harga_normal * diskon)

# Output hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"Hari menonton  : {hari}")
print(f"Status pelajar : {pelajar}")
print(f"Usia penonton  : {usia} tahun")
print(f"Diskon diterapkan: {int(diskon * 100)}%")
print(f"Harga tiket akhir: Rp{int(harga_akhir):,}")