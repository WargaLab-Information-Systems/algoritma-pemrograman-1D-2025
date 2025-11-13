# soal no 2
tiket_normal = 50000

usia = int(input("masukan usia :"))
status_pelajar = input("apakah anda pelajar sma? (ya/tidak) :")
hari = input("masukan hari :")

diskon = 0

if usia <12:
    diskon = 0.5
elif status_pelajar == "ya":
    diskon = 0.3
elif hari == "selasa":
    diskon = 0.2


harga_bayar = tiket_normal - (tiket_normal * diskon)

print("harga tiket normal : Rp ", tiket_normal)
print("diskon : ", diskon)
print("total yang harus dibayar adalah :", harga_bayar)


print("================================")



# soal no 3
lama_parkir = int(input("masukan lama parkir (jam):"))
status_vip = input("Apakah anda member VIP? (ya/tidak): ")

if status_vip == "ya":
    total_bayar = 0
else:
    if lama_parkir <= 2:
        total_bayar = 5000
    else: 
        total_bayar = 5000 + (lama_parkir - 2) * 3000

    
    if total_bayar > 20000:
        total_bayar = 20000

    print("lama parkir :", lama_parkir)
    print("status VIP :", status_vip)
    print("total bayar parkir : Rp", total_bayar )





