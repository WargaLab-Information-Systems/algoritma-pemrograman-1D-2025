# Input
jam = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")

# Hitung
if vip == "ya":
    biaya = 0
else:
    if jam < 2:
        biaya = 5000
    elif jam == 2:
        biaya = 10000
    else:
        biaya = 5000 + (jam - 2) * 3000
    
    # Maksimal tarif per hari Rp20.000
    if biaya > 20000:
        biaya = 20000

# Output
print("Total biaya parkir = Rp", biaya)