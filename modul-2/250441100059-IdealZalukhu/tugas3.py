# hitung tarif parkir mall
lama_parkir = int(input("Masukkan berapa lama parkir(jam): "))
vip = input("apakah anda member vip (ya/tidak): ")

# jika member vip, parkir gratis
if vip == "ya":
    total_bayar = 0
else:
    if lama_parkir <= 2:
        total_bayar = 5000
    else:
        total_bayar = 5000 + (lama_parkir - 2) * 3000
# maksimal tarif parkir per hari
    if total_bayar > 20000:
        total_bayar = 20000

    # tambahan biaya jika lebih dari 24 jam
    if lama_parkir > 24:
        tambahan_hari = lama_parkir // 24
        total_bayar += tambahan_hari * 5000

# hasil
print(f"lama parkir : {lama_parkir} jam")
print(f"status vip : {vip}")
print(f"total bayar : {total_bayar}")
