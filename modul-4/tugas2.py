print ("\n" + "="*60)
print ("Program menghitung total gaji mingguan")
print ("="*60)

total_gaji_mingguan = 0
total_jam_lembur_seminggu = 0
total_bonus_shift_malam = 0

for hari_ke in range(1, 8):
    print("Hari ke-" + str(hari_ke) + ":")

    jam_lembur = int(input("Masukkan jumlah jam lembur: "))

    if jam_lembur == 0:
        gaji_lembur = 0
    elif jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 5:
        gaji_lembur = 150000  
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 7:
        gaji_lembur = 250000  
    elif jam_lembur == 8:
        gaji_lembur = 300000
    else:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0  

    gaji_pokok_harian = 100000

    while True:
        shift = input("Apakah shift malam? (y/n): ")
        if shift == "y":
            bonus_shift_malam = 50000
            break
        elif shift == "n":
            bonus_shift_malam = 0
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")

    total_gaji_hari_ini = gaji_pokok_harian + gaji_lembur + bonus_shift_malam

    total_gaji_mingguan += total_gaji_hari_ini
    total_jam_lembur_seminggu += jam_lembur
    total_bonus_shift_malam += bonus_shift_malam

    print("Gaji hari " + str(hari_ke) + ": Rp" + str(total_gaji_hari_ini))
    print("-" * 40)

print("Total setelah 7 hari:")
print("Total jam lembur: " + str(total_jam_lembur_seminggu) + " jam")
print("Total bonus shift malam: Rp" + str(total_bonus_shift_malam))
print("Total gaji seminggu: Rp" + str(total_gaji_mingguan))
