total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print("\nHari ke-" + str(hari))
    jam = int(input("Masukkan jumlah jam lembur: "))
    shift = input("Apakah shift malam? (y/n): ")
    

    gaji_pokok = 100000
    gaji_lembur = 0
    bonus_shift = 0

    if 1 <= jam <= 3:
        gaji_lembur = jam * 25000
    elif jam == 4:
        gaji_lembur = 100000
    elif jam == 5:
        gaji_lembur = 125000
    elif jam == 6:
        gaji_lembur = 200000
    elif jam == 7:
        gaji_lembur = 225000
    elif jam == 8:
        gaji_lembur = 300000
    elif jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0
    
    if shift == "y" and jam > 0:
        bonus_shift = 50000
    else:
        bonus_shift = 0

    total_gaji += gaji_pokok + gaji_lembur + bonus_shift
    total_lembur += jam
    total_bonus += bonus_shift

print("\n")
print("Total jam lembur       :", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu    : Rp", total_gaji)