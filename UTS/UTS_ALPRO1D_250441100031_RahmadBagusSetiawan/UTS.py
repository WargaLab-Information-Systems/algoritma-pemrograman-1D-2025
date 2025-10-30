# matic = 50000
# trail = 100000
# sport = 75000
# hari = 1

motor = input("Masukkan jenis motor :")
harga = int(input("Masukkan harga :"))
hari = int(input("Masukkan hari :"))

bayar = hari * harga

if bayar >= 150000 :
    diskon = bayar * 0.1
else:
    diskon = 0

total = bayar - diskon 
print (total)