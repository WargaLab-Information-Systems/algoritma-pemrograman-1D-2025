# Program menghitung tarif parkir

# Input dari pengguna
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda VIP? (ya/tidak): ")

# Jika pengguna adalah VIP
if status_vip.lower() == "ya":
    total_bayar = 0

else:
    if lama_parkir <= 2:
        total_bayar = 5000
    elif lama_parkir <= 7:
        # 2 jam pertama = 5000, jam ke-3 s.d ke- 24= 3000/jam
        total_bayar = 5000 + (lama_parkir - 2) * 3000
    else:
        # Sampai 24 jam = 20000, sisanya 3000/jam
        total_bayar = 20000 + (lama_parkir - 24) * 3000

# Tampilkan hasil
print(f"Total biaya parkir: Rp{total_bayar:,}")
