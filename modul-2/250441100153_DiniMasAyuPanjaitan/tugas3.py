# Program Penghitung Biaya Parkir Mall
# Tarif parkir
tarif_2jam = 5000
tarif_perjam = 3000
maksimal_harian = 20000

# Input dari pengguna
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

# Hitung biaya
if status_vip == 'ya':
    biaya = 0
else:
    if lama_parkir <= 2:
       biaya = tarif_2jam
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000
    # Batasi maksimal harian
    biaya = min(biaya, maksimal_harian)
    
# Output
print("Total biaya parkir:Rp".biaya)