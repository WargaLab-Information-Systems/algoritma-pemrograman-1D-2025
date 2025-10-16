# TUGAS PRAKTIKUM NO.3

lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

if status_vip == "ya":
    total_biaya = 0
else:
    # biaya parkir
    if lama_parkir <= 2:
        total_biaya = 5000
    elif lama_parkir <= 24:
        total_biaya = 5000 + (lama_parkir - 2) * 3000
        if total_biaya > 20000:
            total_biaya = 20000
    else:
        # jika lebih dari 24 jam 
        hari_penuh = lama_parkir // 24
        sisa_jam = lama_parkir % 24
        total_biaya = hari_penuh * 20000  # tarif maksimal per hari

        # tambah biaya sisa jam di hari berikutnya 
        if sisa_jam > 0:
            if sisa_jam <= 2:
                total_biaya += 5000
            else:
                total_biaya += 5000 + (sisa_jam - 2) * 3000

            # batasi maksimal tarif per hari
            if total_biaya > (hari_penuh + 1) * 20000:
                total_biaya = (hari_penuh + 1) * 20000

print("\n=== RINCIAN TARIF PARKIR ===")
print(f"Lama Parkir : {lama_parkir} jam")
print(f"Status VIP  : {status_vip}")
print(f"Total Biaya : Rp{total_biaya:,}")