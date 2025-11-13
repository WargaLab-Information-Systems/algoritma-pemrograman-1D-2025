print("==== Harga Tiket Bioskop ====")

price_tiket_normal = 50000

#diskon untuk usia,pelajar,hari
umur = int(input("Masukkan umur :"))
status = input("Apakah kamu itu pelajar SMA dengan kartu pelajar? (yes or no) :")
day = input("Lu nonton di hari apa: ")

#ketentuan diskon
if umur < 12:
    diskon = 50
elif status == "yes":
    diskon = 30
elif day == "selasa":
    diskon = 20
else:
    diskon = 0

    #harga after diskon
harga_dibayar = price_tiket_normal - (price_tiket_normal * diskon / 100)
print("diskon yang kamu dapatkan:", diskon, "%")
print("total harga tiket yang kamu bayar: rp", harga_dibayar)