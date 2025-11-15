 # Program menghitung total gaji mingguan Pak Wowo
total_gaji = 0
total_jam = 0
total_bonus = 0

for hari in range(1, 8): 
    print(f"\nHari ke-{hari}")
    try:
        lembur = int(input("Masukkan jam lembur hari ini: "))
    except ValueError:
        print("inputan tidak valid! lembur otomatis 0.")

    shift_malam = input("Apakah hari ini shift malam? (y/n): ")

    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 8

    # Hitung gaji lembur
    if lembur <= 3:
        gaji_lembur = lembur * 25000
    elif lembur == 4:
        gaji_lembur = 100000
    elif lembur == 5:
        gaji_lembur = 100000 + 25000
    elif lembur == 6:
        gaji_lembur = 200000
    elif lembur == 7:
        gaji_lembur = 200000 + 25000
    elif lembur == 8:
        gaji_lembur = 3000000
    else:
        gaji_lembur = 0
    # Gaji pokok
    gaji_pokok = 100000

    # Bonus shift malam
    if shift_malam == "y":
        bonus = 50000
    else:
        bonus = 0

    total = gaji_pokok + gaji_lembur + bonus

    total_gaji += total
    total_jam += lembur
    total_bonus += bonus

print("\n=== HASIL PERHITUNGAN GAJI MINGGUAN ===")
print(f"Total jam lembur: {total_jam} jam")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji seminggu: Rp{total_gaji}")