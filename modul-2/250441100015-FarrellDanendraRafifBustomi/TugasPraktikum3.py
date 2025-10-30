lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah anda member VIP? (ya/tidak): ").lower()

if vip == "ya":
    biaya = 0
else:
    if lama_parkir <= 0:
        biaya = 0
    elif lama_parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000

    if biaya > 20000:
        biaya = 20000

print("Total biaya parkir: Rp", biaya)
