lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

if status_vip == "ya":
    total_biaya = 0
else:
    hari = lama_parkir // 24
    sisa_jam = lama_parkir % 24

    biaya_hari = hari * 20000  

    if sisa_jam <= 2:
        biaya_jam = 5000
    else:
        biaya_jam = 5000 + (sisa_jam - 2) * 3000
        if biaya_jam > 20000:
            biaya_jam = 20000

    total_biaya = biaya_hari + biaya_jam

print(f"Total Biaya : Rp{total_biaya:,}")
