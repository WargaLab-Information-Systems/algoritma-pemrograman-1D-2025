# harga tiket bioskop
tiket_normal = 50000

# input data
usia = int(input("Masukkan usia penonton: "))
status_pelajar = input("Apakah anda pelajar SMA (ya/tidak): ")
hari = input("Masukkan hari apa anda menonton: ")

# diskon awal
diskon = 0

# diskon
if usia < 12:
    diskon = 50
elif status_pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

# kombinasi diskon yang lebih besar
if usia < 12:
    diskon = max(diskon, 50)
elif status_pelajar == "ya":
    diskon = max(diskon, 30)
elif hari == "selasa":
    diskon == max(diskon,20)

# harga setelah diskon
harga_diskon = tiket_normal - (tiket_normal * diskon / 100)

# hasil
print(f"hari : {hari}")
print(f"usia : {usia} tahun")
print(f"diskon yang didapat : {diskon}%")
print(f"harga bayar : Rp {int(harga_diskon):,}")