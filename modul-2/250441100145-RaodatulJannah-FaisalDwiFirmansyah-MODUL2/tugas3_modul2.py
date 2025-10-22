lama_parkir = int(input("masukkan lama parkir (jam): "))
vip = input("apakah anda member VIP (ya/tidak): "). lower()

if vip == "ya":
    total_biaya = 0
else:
    if lama_parkir <= 2:
        biaya = 5000
    else:
        total_biaya = 5000 + (lama_parkir - 2) * 3000
    
    if total_biaya > 20000:
        total_biaya = 20000

print("total biaya parkir anda adalah: Rp", total_biaya)