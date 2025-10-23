# Meminta input lama parkir dalam jam
jam = int(input("Masukkan lama parkir (jam): "))

# Meminta status VIP dari pengguna
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Jika VIP, langsung gratis
if vip == "ya":
    biaya = 0

# Kalau bukan VIP, hitung sesuai aturan
else:
    # Hitung berapa hari dan sisa jam
    hari = jam // 24
    sisa_jam = jam % 24

    # Biaya untuk hari penuh
    biaya = hari * 20000

    # Hitung biaya tambahan untuk sisa jam di hari berikutnya
    if sisa_jam <= 2 and sisa_jam > 0:
        tambahan = 5000
    elif sisa_jam > 2:
        tambahan = 5000 + (sisa_jam - 2) * 3000
    else:
        tambahan = 0

    # Maksimal biaya per hari adalah 20.000
    if tambahan > 20000:
        tambahan = 20000

    biaya += tambahan

# Cetak hasil akhir
print("Total biaya parkir yang harus dibayar: Rp", biaya)
print("Maksimal tarif parkir per hari adalah Rp20.000")