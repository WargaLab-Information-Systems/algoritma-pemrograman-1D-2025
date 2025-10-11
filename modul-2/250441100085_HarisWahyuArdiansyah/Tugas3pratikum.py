lama = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if lama <= 2:
        total = 5000
    elif lama <= 24:
        total = 5000 + (lama - 2) * 3000
        if total > 20000:
            total = 20000
    else:  
        total = 20000 + (lama - 24) * 3000
        
print("Total biaya parkir: Rp", total)