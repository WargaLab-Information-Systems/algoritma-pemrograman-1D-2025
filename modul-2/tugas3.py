# Program Menghitung Tarif Parkir Mall dengan Perhitungan Harian

lama_parkir = int(input("Berapa lama kamu parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ").lower()

# Jika member VIP, biaya parkir gratis
if vip == "ya":
    total = 0
else:
    total = 0
    hari_penuh = lama_parkir // 24
    sisa_jam = lama_parkir % 24

    # Biaya untuk hari-hari penuh
    total += hari_penuh * 20000

    # Hitung biaya sisa jam
    if sisa_jam > 0:
        if sisa_jam <= 2:
            biaya_sisa = 5000
        else:
            biaya_sisa = 5000 + (sisa_jam - 2) * 3000

        # Batas maksimal per hari
        if biaya_sisa > 20000:
            biaya_sisa = 20000

        total += biaya_sisa

# Output hasil
print("Total biaya parkir: Rp", total)