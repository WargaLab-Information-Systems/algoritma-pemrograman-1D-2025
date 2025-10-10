harga = 50000
# Input
usia = int(input("Masukkan usia Anda: "))
pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ")
hari = input("Masukkan hari: ")

# diskon
if usia < 12:
    diskon = 50
elif pelajar.lower() == "ya":
    diskon = 30
elif hari.lower() == "selasa":
    diskon = 20
else:
    diskon = 0

# Hitung Pembayaran
bayar = harga - (harga * diskon / 100)

print("Harga tiket normal = Rp", harga)
print("Diskon =", diskon, "%")
print("Total bayar = Rp", int(bayar))
