# Program Perhitungan Gaji Mingguan Pak Wowo

total_gaji = 0
total_bonus_shift = 0
total_jam_lembur = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif, coba lagi.")
                continue
            if jam_lembur > 8:
                print("Lembur melebihi batas, tidak dihitung.")
            break
        except:
            print("Input tidak valid, masukkan angka.")

    if jam_lembur == 0:
        tambahan_lembur = 0
    if 1 <= jam_lembur <= 3:
        tambahan_lembur = 25000 * jam_lembur
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 5:
        tambahan_lembur = 150000  # Nilai tengah antara 4 dan 6 jam
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 7:
        tambahan_lembur = 250000  # Nilai tengah antara 6 dan 8 jam
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    elif jam_lembur > 8 :
        jam_lembur = 8
        tambahan_lembur = 300000

    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam == "y":
            bonus_shift = 50000
            break
        elif shift_malam == "n":
            bonus_shift = 0
            break
        else:
            print("Input tidak valid, masukkan hanya 'y' untuk ya atau 'n' untuk tidak.")

    gaji_harian = 100000

    total_jam_lembur = total_jam_lembur + jam_lembur
    total_bonus_shift = total_bonus_shift + bonus_shift
    total_gaji = total_gaji + gaji_harian + tambahan_lembur + bonus_shift

    print()

print()
print("Total jam lembur selama seminggu adalah:", total_jam_lembur, "jam")
print("Total bonus shift malam selama seminggu adalah: Rp", total_bonus_shift)
print("Total gaji Pak Wowo selama seminggu adalah: Rp", total_gaji)