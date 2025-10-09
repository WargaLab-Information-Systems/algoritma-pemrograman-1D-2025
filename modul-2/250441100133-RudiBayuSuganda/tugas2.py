tiket_normal=50000
usia=int(input("Masukkan Usia Pembeli :"))
pelajar=input("Apakah pelajar SMA Dengan Kartu Pelajar? ").lower()
hari=input("Menonton Pada Hari Apa? ").lower()
diskon=0
if usia<12:
    diskon=0.50
if pelajar=="iya":
    if 0.30>diskon:
        diskon=0.30
if hari=="selasa":
    if 0.20>diskon:
        diskon=0.20
potongan=tiket_normal*diskon
total_bayar=tiket_normal-potongan
print("Tiket Normal = ",tiket_normal)
print("Diskon =",int(diskon*100),"%")
print("Total Pembayaran = ",int(total_bayar))