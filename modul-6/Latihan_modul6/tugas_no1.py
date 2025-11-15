data_kunjungan = []
id_antrian = 1

while True:
    print("===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Pengunjung")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        print("=== Tambah Pengunjung ===")

        while True:
            nama_pengunjung = input("Nama pengunjung: ")
            valid = True
            for huruf in nama_pengunjung:
                if not (huruf ==("A" <= huruf <= "Z") or ("a" <= huruf <= "z")):
                    valid = False
                    break
            if valid and nama_pengunjung != "":
                break
            print("Nama hanya boleh berisi huruf!")

        while True:
            nama_santri = input("Nama santri yang dijenguk: ")
            valid = True
            for huruf in nama_santri:
                if not (huruf == " " or ("A" <= huruf <= "Z") or ("a" <= huruf <= "z")):
                    valid = False
                    break
            if valid and nama_santri!= "":
                break
            print("Nama hanya boleh berisi huruf!")

        while True:
            daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")
            if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
                break
            print("Masukkan hanya Sumatra, Kalimantan, atau Jawa!")

        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID {id_antrian}")
        id_antrian += 1

    elif pilih == "2":
        if not data_kunjungan:
            print("Belum ada data kunjungan.")
            continue

        print("=== Daftar Pengunjung Berdasarkan Daerah ===")
        for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            print(f"-- Pengunjung dari {daerah} --")
            ada = False
            for d in data_kunjungan:
                if d[3] == daerah:
                    print(f"ID: {d[0]}, Pengunjung: {d[1]}, Santri: {d[2]}")
                    ada = True
            if not ada:
                print("Tidak ada pengunjung dari daerah ini.")

    elif pilih == "3":
        if not data_kunjungan:
            print("Tidak ada data untuk dihapus.")
            continue

        try:
            hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
            for d in data_kunjungan:
                if d[0] == hapus:
                    data_kunjungan.remove(d)
                    print(f"Data dengan ID {hapus} berhasil dihapus.")
                    break
            else:
                print("ID tidak ditemukan.")
        except ValueError:
            print("ID harus berupa angka!")

    elif pilih == "4":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")