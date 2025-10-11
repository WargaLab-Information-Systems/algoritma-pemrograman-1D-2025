lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")
if vip == "ya" or vip == "Ya":
    total = 0
    print("Anda member VIP, biaya parkir gratis.")
elif vip == "tidak" or vip == "Tidak":
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000
        if total > 20000:
            total = 20000
else:
    total = 0
    print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
print("Total biaya parkir: Rp", total)
