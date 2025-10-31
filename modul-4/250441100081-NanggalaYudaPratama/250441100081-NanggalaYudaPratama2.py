# SOAL 2

while True:
    nama = input("Masukkan nama karyawan: ")
    if nama == "":
        print("Nama tidak boleh kosong. Silakan masukkan lagi.")
        continue

    if any(angka in nama for angka in "0123456789"):
        print("Peringatan: Nama mengandung angka, kemungkinan typo.")
    elif nama.isupper():
        print("Catatan: Nama semuanya huruf besar.")
    elif nama.islower():
        print("Catatan: Nama semuanya huruf kecil.")
    else:
        print("Nama terdeteksi normal.\n")

    konfirmasi = input("Apakah data nama sudah benar? (y/n): ")
    if konfirmasi != "y":
        print("Kembali ke awal untuk mengulang data...\n")
        continue

    total_gaji = 0
    total_lembur = 0
    total_bonus_shift = 0
    hari = 1
    
    for hari in range(1, 8):
        print(f"\nHari ke-{hari}:")
        jam_input = input("Masukkan jumlah jam lembur: ")

        if not jam_input.isdigit():
            print("Kesalahan input! Harus berupa angka.")
            ulang = input("Ingin kembali ke awal program? (y/n): ")
            if ulang == "n":
                break  
            else:
                continue

        jam_lembur = int(jam_input)
        shift_malam = input("Apakah shift malam? (y/n): ")

        if shift_malam not in ["y", "n"]:
            print("Input tidak valid! Harus 'y' atau 'n'.")
            ulang = input("Ingin kembali ke awal program? (y/n): ")
            if ulang == "n":
                break
            else:
                print("Mengulang hari ini...")
                continue

        if jam_lembur > 8:
            print("Lembur melebihi batas, tidak dihitung.")
            lembur_hari_ini = 0
        elif 1 <= jam_lembur <= 3:
            lembur_hari_ini = jam_lembur * 25000
        elif 4 <= jam_lembur <= 5: #4-5
            lembur_hari_ini = 100000
        elif 6 <= jam_lembur <= 7: #6-7
            lembur_hari_ini = 200000
        elif jam_lembur == 8:
            lembur_hari_ini = 300000
        else:
            lembur_hari_ini = 0

        gaji_pokok = 100000
        bonus_shift = 50000 if shift_malam == "y" else 0
        total_harian = gaji_pokok + lembur_hari_ini + bonus_shift

        print(f"Gaji hari ini : Rp{total_harian:,}")
        if shift_malam == "y":
            print("Catatan: Bonus shift malam ditambahkan sebesar Rp50.000")
        if jam_lembur == 0:
            print("Catatan: Tidak ada lembur hari ini.")
        
        total_gaji += total_harian
        total_lembur += jam_lembur if jam_lembur <= 8 else 0
        total_bonus_shift += bonus_shift
        hari += 1

    else: 
        print("\n===== REKAP GAJI MINGGUAN =====")
        print(f"Nama karyawan          : {nama}")
        print(f"Total jam lembur       : {total_lembur} jam")
        print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
        print(f"Total gaji seminggu    : Rp{total_gaji:,}")
        print("================================")

        ulang = input("\nApakah ingin menghitung lagi? (y/n): ")
        if ulang == "y":
            continue
        else:
            print("Program selesai. Terima kasih!")
            break
