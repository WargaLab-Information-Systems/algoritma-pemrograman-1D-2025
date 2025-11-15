total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    # Input jam lembur
    jam_lembur = int(input("Masukkan jam lembur (0-8): "))

    # Validasi jam lembur
    if jam_lembur > 8:
        print("Lembur melebihi batas, dihitung maksimal 8 jam.")
        jam_lembur = 8
    elif jam_lembur < 0:
        jam_lembur = 0

    # Hitung gaji lembur
    if jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 5:
        gaji_lembur = 125000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 7:
        gaji_lembur = 225000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    else:
        gaji_lembur = 0

    # Input shift malam
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam == "y":
            bonus = 50000
            break
        elif shift_malam == "n":
            bonus = 0
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")

    # Hitung total gaji harian
    gaji_harian = 100000
    total_gaji_harian = gaji_harian + gaji_lembur + bonus

    # Akumulasi total mingguan
    total_gaji += total_gaji_harian
    total_lembur += jam_lembur
    total_bonus += bonus

    print(f"Gaji hari ke-{hari}: Rp{total_gaji_harian:,}")

# Hasil akhir
print("\n==== Total Gaji Selama 1 Minggu ====")
print(f"Total jam lembur        : {total_lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus:,}")
print(f"Total gaji mingguan     : Rp{total_gaji:,}")