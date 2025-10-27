gaji_pokok = 100000
total_gaji = 0
total_minggu = 0
total_lembur = 0
total_bonus = 0
for i in range(1, 8):
    while True:
        try:
            lembur = int(input(f"Masukkan jumlah jam lembur hari-{i}: "))
            if lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka saja.")
    while True:
        malam = input("Apakah termasuk shift malam (y/n): ").lower()
        if malam in ["y", "n"]:
            break
        else:
            print("Input hanya 'y' atau 'n'. Coba lagi.")
    if 1 <= lembur <= 3:
        gaji_lembur = lembur * 25000
    elif lembur == 4:
        gaji_lembur = 100000
    elif lembur == 5:
        gaji_lembur = 125000
    elif lembur == 6:
        gaji_lembur = 200000
    elif lembur == 7:
        gaji_lembur = 225000
    elif lembur == 8:
        gaji_lembur = 300000
    elif lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0
    else:
        gaji_lembur = 0
    if malam == "y":
        bonus = 50000
    else:
        bonus = 0
    total_gaji=gaji_pokok+gaji_lembur+bonus
    total_lembur += lembur
    total_bonus += bonus
    total_minggu += total_gaji
print(f"Total jam lembur minggu ini : {total_lembur} jam")
print(f"Total bonus shift malam     : Rp{total_bonus:,}")
print(f"Total gaji selama 7 hari    : Rp{total_minggu:,}")