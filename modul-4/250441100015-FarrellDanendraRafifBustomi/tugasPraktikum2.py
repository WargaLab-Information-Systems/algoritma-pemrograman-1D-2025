total_gaji = 0
total_lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif!")
                continue
            
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Masukkan 'y' atau 'n'.")
    
    gaji_harian = 100000
    
    if jam_lembur > 8:
        print("batas jam lembur sampai 8 jam.")
        jam_lembur_dihitung = 8  
    else:
        jam_lembur_dihitung = jam_lembur

    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
        total_lembur += jam_lembur
    elif jam_lembur == 4:
        gaji_harian += 100000
        total_lembur += jam_lembur
    # jika pak wowo lembur 5 jam
    elif jam_lembur == 5:
        gaji_harian += 150000
        total_lembur += jam_lembur
    # end jika pak wowo lembur 5 jam
    elif jam_lembur == 6:
        gaji_harian += 200000
        total_lembur += jam_lembur
    # jika pak wowo lembur 7 jam
    elif jam_lembur == 7:
        gaji_harian += 250000
        total_lembur += jam_lembur
    # end jika pak wowo lembur 7 jam
    elif jam_lembur == 8:
        gaji_harian += 300000
        total_lembur += jam_lembur
    
    total_lembur += jam_lembur_dihitung
    
    if shift_malam == 'y':
        gaji_harian += 50000
        total_bonus_shift += 50000
    
    total_gaji += gaji_harian

print("\n=== Rekapitulasi Gaji Mingguan Pak Wowo ===")
print(f"Total jam lembur        : {total_lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus_shift:,}")
print(f"Total gaji seminggu     : Rp{total_gaji:,}")
