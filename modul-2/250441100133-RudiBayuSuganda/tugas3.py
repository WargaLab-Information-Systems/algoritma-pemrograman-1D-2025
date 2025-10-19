lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah member VIP? (iya/tidak): ").lower()
if status_vip == "iya":
    total_biaya = 0
elif lama_parkir<=2:
    total_biaya=5000
elif lama_parkir<=7:
    total_biaya=5000+(lama_parkir-2)*3000
else :total_biaya=20000
print("Total biaya parkir: Rp",total_biaya)