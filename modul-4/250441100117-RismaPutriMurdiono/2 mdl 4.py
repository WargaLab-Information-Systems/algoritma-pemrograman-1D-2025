# # Program Menghitung Gaji Mingguan Pak Wowo
# total_gaji = 0
# total_lembur = 0
# total_bonus = 0

# for hari in range(1, 8):
#     print(f"\nHari ke-{hari}")
#     jam_lembur = int(input("Masukkan jumlah jam lembur: "))
#     shift_malam = input("Apakah shift malam? (y/n): ").lower()

#     # Hitung gaji pokok harian
#     gaji_pokok = 100000
#     bonus = 50000 if shift_malam == 'y' else 0
#     total_bonus += bonus

#     # Hitung lembur
#     if jam_lembur <= 0:
#         lembur = 0
#     elif jam_lembur <= 3:
#         lembur = jam_lembur * 25000
#     elif jam_lembur == 4:
#         lembur = 100000
#     elif jam_lembur == 5:
#         lembur = 100000 + 25000
#     elif jam_lembur == 6:
#         lembur = 200000
#     elif jam_lembur == 7:
#         lembur = 200000 + 25000
#     elif jam_lembur == 8:
#         lembur = 300000
#     else:
#         print("Lembur melebihi batas, tidak dihitung.")
#         lembur = 0

#     total_lembur += lembur
#     total_gaji += gaji_pokok + lembur + bonus

# print("\n--- Rincian Mingguan ---")
# print(f"Total lembur   : Rp{total_lembur:,}")
# print(f"Total bonus    : Rp{total_bonus:,}")
# print(f"Total gaji minggu: Rp{total_gaji:,}")
# print()


total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    jam_lembur = int(input("Masukkan jumlah jam lembur: ".lower ))
    shift_malam = input("Apakah shift malam? (y/n): ").lower()

    gaji_pokok = 100000
    bonus = 50000 if shift_malam == 'y' else 0
    total_bonus += bonus

    if jam_lembur <= 0:
        lembur = 0
    elif jam_lembur <= 3:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 5:
        lembur = 100000 + 25000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 7:
        lembur = 200000 + 25000
    elif jam_lembur == 8:
        lembur = 300000
    else:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0

    total_lembur += lembur
    total_gaji += gaji_pokok + lembur + bonus

print("\n--- Rincian Mingguan ---")
print(f"Total lembur   : Rp{total_lembur:,}")
print(f"Total bonus    : Rp{total_bonus:,}")
print(f"Total gaji minggu: Rp{total_gaji:,}")
print()