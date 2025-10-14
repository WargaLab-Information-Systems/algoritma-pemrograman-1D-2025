usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

# Harga normal
harga = 50000

# Perintah if, elif, else untuk cek kondisi diskon
if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0


# Hitung harga akhir
harga_diskon = harga - (harga * diskon / 100)


# Output hasil
print("====RINCIAN PEMBAYARAN===")
print("Harga tiket yang harus dibayar adalah Rp", int(harga_diskon))
print("Diskon yang di dapat sebesar",int(diskon))