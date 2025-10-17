# Input data
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA tersebut membawa kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")

# Harga dan diskon
harga_normal = 50000
diskon = 0

# Cek kondisi dan diskon
if usia < 12:
    diskon = max(diskon, 50)
if pelajar == "ya":
    diskon = max(diskon, 30)
if hari == "selasa":
    diskon = max(diskon, 20)

# Hitung harga 
harga_akhir = harga_normal - (harga_normal * diskon / 100)

print("Harga tiket yang harus dibayar: Rp", int(harga_akhir))