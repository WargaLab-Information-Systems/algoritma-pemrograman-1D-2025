total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\n hari ke- {hari}")
    try:
        lembur = int(input("masukkan jam lembur hari ini: "))
    except ValueError:
        print("input tidak valid! lembur otomatis 0.")
        lembur = 0
    shift_malam = input("Apakah hari ini shift malam? (y/n): ")

    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0

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
        gaji_lembur = 300000
    else:
        gaji_lembur = 0

    gaji_pokok = 100000

    if shift_malam.lower() == "y":
        bonus = 50000
    else:
        bonus = 0

    total = gaji_pokok + gaji_lembur + bonus

    total_gaji += total
    total_lembur += gaji_lembur
    total_bonus += bonus

print(f"Total gaji lembur: Rp{total_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji seminggu: Rp{total_gaji}")