# # Harga Menghitung Harga Tiket Bioskop

# Harga_normal = 50000

# usia = int(input("Berapa usia anda: "))

# pelajar = input("Pelajar SMA dengan kartu pelajar? (ya/tidak): ")
# hari = input("Masukan hari (senin, selasa, rabu, kamis, jum'at, sabtu, minggu): ")

# if usia <= 12:
#     diskon = 50
# elif pelajar == "ya":
#     diskon = 30
# elif hari == "selasa":
#     diskon = 20

# harga_bayar = Harga_normal - (Harga_normal * diskon / 100)
# print("\nDiskon yang di dapatkan : ", diskon, "%")
# print("harga tiket yang harus di bayar: Rp", int(harga_bayar))


# Program Menghitung Tarif Parkir Mall

lama_parkir = int(input("Berapa lama kamu parkir(jam): "))

vip = input("Apakah memmber VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000

    if total >= 20000:
        total = 20000

print("\nTotal biaya parkir: Rp", total)
