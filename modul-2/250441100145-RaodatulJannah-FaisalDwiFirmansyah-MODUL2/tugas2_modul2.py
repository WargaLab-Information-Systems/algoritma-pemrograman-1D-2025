harga_normal = 50000
diskon = 0

usia = int(input("masukkan usia penonton: "))
status_pelajar = (input("apakah pelajar SMA? (ya/tidak): ")). lower()
hari = (input("masukkan hari: ")). lower()

if usia < 12:
    diskon = max(diskon, 50)
elif status_pelajar == "ya":
    diskon = max(diskon, 30)
elif hari == "selasa":
    diskon = max(diskon, 20)
else:
    print("mohon maaf anda tidak mendapatkan diskon")

harga_tiket = harga_normal - (harga_normal * diskon / 100)
 
print("diskon yang didapat: ", (diskon),"%")
print("total harga tiket: Rp", int(harga_tiket))  