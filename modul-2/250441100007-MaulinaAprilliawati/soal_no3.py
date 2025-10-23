# Input data
jam = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah kamu member VIP? (ya/tidak): ").lower()

if vip == "ya":
    total = 0
else:
    # Hitung jumlah hari dan sisa jam
    hari = jam // 24
    sisa_jam = jam % 24

    # Biaya dari hari penuh (tiap hari Rp20.000)
    total = hari * 20000

    # Hitung biaya sisa jam di hari terakhir
    if sisa_jam <= 2:
        total += 5000
    else:
        tambahan = 5000 + (sisa_jam - 2) * 3000
        if tambahan > 20000:
            tambahan = 20000  
        total += tambahan

# Output hasil
print("\n=== RINCIAN PARKIR ===")
print(f"Lama parkir : {jam} jam")
print(f"Status VIP  : {vip}")
print(f"Total bayar : Rp{total}")
