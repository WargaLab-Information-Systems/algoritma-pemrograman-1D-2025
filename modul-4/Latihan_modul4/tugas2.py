print("=== Program Gaji Mingguan Pak Wowo ===")

total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(0, 7):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jumlah jam lembur: "))
    shift = input("Apakah shift malam? (y/n): ")

    gaji_pokok = 100000
    tambahan = 0

    if lembur >= 1 and lembur <= 3:
        tambahan = lembur * 25000
    elif lembur == 4:
        tambahan = 100000
    elif lembur == 6:
        tambahan = 200000
    elif lembur == 8:
        tambahan = 300000
    elif lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan = 0

    bonus = 0
    if shift == "y":
        bonus = 50000

    gaji_hari_ini = gaji_pokok + tambahan + bonus

    total_gaji = total_gaji + gaji_hari_ini
    total_lembur = total_lembur + lembur
    total_bonus = total_bonus + bonus

print("\n=== Rekap Gaji Mingguan ===")
print("Total jam lembur:", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu: Rp", total_gaji)