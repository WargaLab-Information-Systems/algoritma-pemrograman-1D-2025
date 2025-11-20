total_gaji = 0
total_lembur_jam = 0
total_bonus_shift = 0

print("=== Program Hitung Gaji Mingguan Pak Wowo ===")

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    # Validasi input jumlah jam lembur
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur (0-8): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    # Validasi input shift malam
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Masukkan 'y' atau 'n'.")
    
    # Gaji pokok per hari
    gaji_harian = 100000
    
    # Hitung lembur
    if 1 <= jam_lembur <= 3:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 8:
        lembur = 300000
    elif jam_lembur > 8:
        jam_lembur = 8
        print("⚠️ Lembur melebihi batas, tidak dihitung.")
        lembur = 300000
    else:
        lembur = 0  # jika tidak lembur
    
    # Hitung bonus shift malam
    bonus = 50000 if shift_malam == 'y' else 0
    
    # Hitung total gaji harian
    total_harian = gaji_harian + lembur + bonus
    
    # Tambahkan ke total mingguan
    total_gaji += total_harian
    total_lembur_jam += jam_lembur if jam_lembur <= 8 else 0
    total_bonus_shift += bonus
    
    print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")

# Setelah 7 hari
print("\n=== Rangkuman Gaji Mingguan ===")
print(f"Total jam lembur selama seminggu : {total_lembur_jam} jam")
print(f"Total bonus shift malam          : Rp{total_bonus_shift:,}")
print(f"Total gaji selama seminggu       : Rp{total_gaji:,}")
