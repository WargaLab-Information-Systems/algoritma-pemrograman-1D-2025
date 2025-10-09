# Program menghitung tarif parkir mall

# Input
lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Inisialisasi tarif
tarif_awal = 5000
tarif_per_jam = 3000
tarif_maksimal = 20000

# Proses perhitungan
if vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = tarif_awal
    else:
        total = tarif_awal + (lama_parkir - 2) * tarif_per_jam
        if total > tarif_maksimal:
            total = tarif_maksimal

# Output hasil
print("\n=== HASIL PERHITUNGAN TARIF PARKIR ===")
print(f"Lama parkir : {lama_parkir} jam")
print(f"Status VIP  : {vip}")
print(f"Total biaya : Rp{total:,}")