# Harga Menghitung Harga Tiket Bioskop

Harga_normal = 50000

usia = int(input("Berapa usia anda: "))

pelajar = input("Pelajar SMA dengan kartu pelajar? (ya/tidak): ").lower()
hari = input("Masukan hari (senin, selasa, rabu, kamis, jum'at, sabtu, minggu): ").lower()

if usia <= 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else :
    diskon = 0

harga_bayar = Harga_normal - (Harga_normal * diskon / 100)
print("Diskon yang di dapatkan : ", diskon, "%")
print("harga tiket yang harus di bayar: Rp", int(harga_bayar))

