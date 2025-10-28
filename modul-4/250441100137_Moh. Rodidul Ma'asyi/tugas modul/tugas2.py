print("=== Program Perhitungan Gaji Mingguan Pak Wowo ===")

total_gaji = 0
total_jam_lembur = 0
total_bonus_shift = 0
gaji_pokok = 100_000 

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur (0–8): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")

    while True:
        shift = input("Apakah shift malam? (y/n): ").lower()
        if shift in ["y", "n"]:
            break
        print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
    
    if 1 <= jam_lembur <= 3:
        bonus_lembur = jam_lembur * 25_000
    elif jam_lembur == 4:
        bonus_lembur = 100_000
    elif jam_lembur == 6:
        bonus_lembur = 200_000
    elif jam_lembur == 8:
        bonus_lembur = 300_000
    elif jam_lembur > 8:
        print(" Lembur melebihi batas, tidak dihitung.")
        bonus_lembur = 0
    else:
        bonus_lembur = 0 

    bonus_shift = 50_000 if shift == "y" else 0

    gaji_harian = gaji_pokok + bonus_lembur + bonus_shift
    total_gaji += gaji_harian
    total_jam_lembur += jam_lembur
    total_bonus_shift += bonus_shift

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")

print("\n=== Rekapitulasi Gaji Mingguan Pak Wowo ===")
print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")