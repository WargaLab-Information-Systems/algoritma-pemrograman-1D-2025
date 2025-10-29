total_gaji = total_lembur = total_bonus = 0

for i in range(7):
    while True:
        try:
            lembur = int(input(f"jam lembur hari ke-{i+1}: "))
            shift = input("shift malam? (y/n): ")
            if lembur < 0 or shift not in ('y', 'n'):
                print("input salah, ulangi!")
                continue
            break
        except:
            print("harus angka!")
    
    gaji_harian = 100000

    if 1 <= lembur <= 3:
        gaji_harian += lembur * 25000
    elif lembur == 4:
        gaji_harian += 100000
    elif lembur == 5:
        gaji_harian += 100000+25000
    elif lembur == 6:
        gaji_harian += 200000
    elif lembur == 7:
        gaji_harian += 200000+25000
    elif lembur == 8:
        gaji_harian += 300000
    elif lembur > 8:
        print("lembur melebihi batas, tidak dihitung.")
        lembur = 0

    if shift == 'y':
        gaji_harian += 50000
        total_bonus += 50000

    total_gaji += gaji_harian
    total_lembur += lembur

print("\n--- Rekap Gaji Pak Wowo ---")
print("total jam lembur :", total_lembur, "jam")
print("total bonus shift malam : Rp", total_bonus)
print("total gaji mingguan : Rp", total_gaji)