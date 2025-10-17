harga_normal = 50000

umur = int(input("Masukkan umur: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar (ya/tidak)? ")
hari = input("Masukkan hari :")

#diskon = 0
#cek diskon
if umur < 12:
    diskon = 50
elif pelajar == "ya":
        diskon = 30
elif hari == "selasa":
        diskon = 20
else:
        diskon = 0

#Harga akhir
harga_bayar = 50000 - (harga_normal * diskon / 100)

print ("diskon =", diskon,)
print ("harga tiket yang harus di bayar: Rp", int(harga_bayar))