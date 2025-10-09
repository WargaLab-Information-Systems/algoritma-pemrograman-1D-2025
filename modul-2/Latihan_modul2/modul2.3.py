# TARIF PARKIR
jam = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

if status_vip == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000                                    # jam pertama
    else:
        biaya = 5000 + (jam - 2) * 3000                 # setiap jam berikutnya
        if biaya > 20000:                               # maksmal tarif/hari
            biaya = 20000

print("Total biaya parkir: Rp", biaya)