kunjungan = []  
id_counter = 1  

while True:
    print("\n===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Daftar Kunjungan")
    print("3. Hapus Data Kunjungan")
    print("4. Keluar")
    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        print("\n=== Tambah Data Kunjungan ===")

        while True:
            nama_pengunjung = input("Masukkan nama pengunjung: ")
            if any(char.isdigit() for char in nama_pengunjung):
                print("Nama pengunjung tidak boleh mengandung angka! Silakan masukkan kembali.")
            elif nama_pengunjung.strip() == "":
                print("Nama pengunjung tidak boleh kosong!")
            else:
                break

        while True:
            nama_santri = input("Masukkan nama santri yang dijenguk: ")
            if any(char.isdigit() for char in nama_santri):
                print("Nama santri tidak boleh mengandung angka! Silakan masukkan kembali.")
            elif nama_santri.strip() == "":
                print("Nama santri tidak boleh kosong!")
            else:
                break

        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
            print("Daerah tidak valid! Gunakan: Sumatra, Kalimantan, atau Jawa.")
        else:
            kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
            print(f"Data berhasil ditambahkan dengan ID antrian: {id_counter}")
            id_counter += 1

    elif menu == "2":
        if len(kunjungan) == 0:
            print("\nBelum ada data kunjungan.")
        else:
            print("\n=== DAFTAR KUNJUNGAN SANTRI ===")
            urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
            for daerah in urutan_daerah:
                print(f"\n--- Pengunjung dari {daerah} ---")
                ada = False
                for data in kunjungan:
                    if data[3] == daerah:
                        print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Asal: {data[3]}")
                        ada = True
                if not ada:
                    print("(Tidak ada pengunjung dari daerah ini)")

    elif menu == "3":
        if len(kunjungan) == 0:
            print("\nBelum ada data yang bisa dihapus.")
        else:
            try:
                id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
                ditemukan = False
                for data in kunjungan:
                    if data[0] == id_hapus:
                        kunjungan.remove(data)
                        print(f"Data dengan ID {id_hapus} berhasil dihapus.")
                        ditemukan = True
                        break
                if not ditemukan:
                    print("ID tidak ditemukan.")
            except ValueError:
                print("Masukkan angka yang benar untuk ID.")

    elif menu == "4":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
