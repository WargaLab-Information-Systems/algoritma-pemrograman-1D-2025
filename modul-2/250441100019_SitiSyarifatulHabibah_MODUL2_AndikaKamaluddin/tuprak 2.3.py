print("==== Tarif Parkir Mall ====")

lama_parkir = int(input("berapa lama parkir (jam): "))
status_vip = input("member vip? (yes or no): ")

if status_vip == "yes":  #gratis
    biaya_parkir = 0
elif status_vip == "no":   #tidak gratis
    if lama_parkir <= 2:
        biaya_parkir = 5000
    else:
        biaya_parkir = 5000 + (lama_parkir - 2) * 3000
    if biaya_parkir > 20000:
        biaya_parkir = 20000
else:
    print("input salah,coba ketik yes or no")
    biaya_parkir = 0

print("total biaya parkir yang harus kamu bayar: rp", biaya_parkir)