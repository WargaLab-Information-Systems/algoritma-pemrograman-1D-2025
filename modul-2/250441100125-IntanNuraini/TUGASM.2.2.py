harga_normal = 50000
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Hari apa? (contoh: senin, selasa, ...): ")

diskon = 0
if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

harga_akhir = harga_normal - (harga_normal * diskon / 100)

print("Diskon yang diperoleh:", diskon, "%")
print("Total harga tiket:", int(harga_akhir))