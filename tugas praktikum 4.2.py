# Program Gaji Mingguan Pak Wowo

total_gaji = 0
total_jam_lembur = 0
total_bonus_shift_malam = 0

for hari in range(1, 8):
    print(f"\n=== Hari ke-{hari} ===")
    jam_lembur = int(input("Masukkan jumlah jam lembur: "))
    
    # Validasi input shift malam
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ["y", "n"]:
            break
        print("Input tidak valid, masukkan 'y' atau 'n'.")
 
    gaji_harian = 100000
    bonus_shift = 50000 if shift_malam == "y" else 0
    lembur = 0

    if 1 <= jam_lembur <= 3:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 5:
        lembur = 125000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 7:
        lembur = 225000
    elif jam_lembur == 8:
        lembur = 300000
    else: 
        jam_lembur > 8
        print("Lembur melebihi batas, tidak dihitung.")

    gaji_total_hari = gaji_harian + lembur + bonus_shift
    total_gaji += gaji_total_hari
    total_jam_lembur += jam_lembur if jam_lembur <= 8 else 0
    total_bonus_shift_malam += bonus_shift

print("\n=== Rekap Mingguan ===")
print(f"Total jam lembur        : {total_jam_lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus_shift_malam:,}")
print(f"Total gaji seminggu     : Rp{total_gaji:,}")