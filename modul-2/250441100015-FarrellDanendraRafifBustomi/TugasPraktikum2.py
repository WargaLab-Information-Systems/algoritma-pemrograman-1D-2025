harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

diskon = 0

if usia < 12:
    diskon = max(diskon, 50)
if pelajar == "ya":
    diskon = max(diskon, 30)
if hari == "selasa":
    diskon = max(diskon, 20)

harga_bayar = harga_normal - (harga_normal * diskon / 100)

print("Diskon yang diperoleh:", diskon, "%")
print("Harga yang harus dibayar: Rp", int(harga_bayar))
