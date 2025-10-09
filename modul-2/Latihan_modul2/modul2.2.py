# MENENTUKAN HARGA TIKET

tiket_normal = 50000

usia = int(input("Masukkan usia: "))
status_pelajar = input("Apakah pelajar SMA? (ya/tidak): ")
hari = input("Masukkan hari: ")

diskon = 0

# Cek diskon
if usia < 12:
    diskon = max(diskon, 50)
if status_pelajar == "ya":
    diskon = max(diskon, 30)
if hari == "selasa":
    diskon = max(diskon, 20)

# Hitung harga tiket yang harus dibayar
harga_akhir = tiket_normal - (tiket_normal * diskon / 100)

print("Diskon yang digunakan:", diskon, "%")
print("Total harga tiket: Rp", int(harga_akhir))
