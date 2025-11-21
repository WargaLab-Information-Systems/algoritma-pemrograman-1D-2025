
total_gaji = 0
total_lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):  
    print(f"\nHari ke-{hari}")
    
   
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka jam lembur dengan benar.")
    

    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ["y", "n"]:
            break
        else:
            print("Input salah! Harap masukkan 'y' untuk ya atau 'n' untuk tidak.")


    gaji_harian = 100000
    lembur_harian = 0
    bonus_shift = 0

    
    if 1 <= jam_lembur <= 3:
        lembur_harian = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur_harian = 100000
    elif jam_lembur == 6:
        lembur_harian = 200000
    elif jam_lembur == 8:
        lembur_harian = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur_harian = 0

    
    if shift_malam == "y":
        bonus_shift = 50000
        total_bonus_shift += bonus_shift

    
    total_harian = gaji_harian + lembur_harian + bonus_shift

    
    total_gaji += total_harian
    total_lembur += jam_lembur

   
print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")
print("\n=== Rekap Gaji Mingguan Pak Wowo ===")
print(f"Total jam lembur selama seminggu: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
print(f"Total gaji selama seminggu: Rp{total_gaji:,}")