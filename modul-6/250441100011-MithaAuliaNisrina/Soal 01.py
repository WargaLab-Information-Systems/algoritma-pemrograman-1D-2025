print("\nPROGRAM SISTEM KUNJUNGAN SANTRI")

data_kunjungan = []
id_antrian = 1

while True:
    print("\nMENU UTAMA SISTEM KUNJUNGAN SANTRI")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung Berdasarkan Daerah (Sumatra/Kalimantan/Jawa)")
    print("3. Hapus Data Pengunjung Berdasarkan ID Antrian")
    print("4. Akhiri Proses Kunjungan Santri, Keluar dari Program")

    pilihan = input("\nSilakan pilih menu (Hanya di Nomor 1-4): ")

    if pilihan == "1":
        print("\nTAMBAH DATA PENGUNJUNG")

        while True:
            nama_pengunjung = input("Masukkan nama pengunjung: ")
            if nama_pengunjung.replace(" ", "").isalpha():
                break
            else:
                print("Input tidak valid! Nama pengunjung hanya boleh berisi huruf.\nSilakan masukkan ulang.")

        while True:
            nama_santri = input("Masukkan nama santri yang dijenguk: ")
            if nama_santri.replace(" ", "").isalpha():
                break
            else:
                print("Input tidak valid! Nama santri hanya boleh berisi huruf.\nSilakan masukkan ulang.")

        while True:
            daerah = input("Masukkan daerah asal pengunjung (Sumatra/Kalimantan/Jawa): ").lower()
            if daerah in ["sumatra", "kalimantan", "jawa"]:
                break
            else:
                print("Input tidak valid! Pilihan hanya boleh antara Sumatra, Kalimantan, atau Jawa.\nSilakan masukkan ulang.")

        id_pengunjung = id_antrian
        id_antrian = id_antrian + 1

        data_kunjungan.append([id_pengunjung, nama_pengunjung, nama_santri, daerah])
        print("\nData pengunjung berhasil ditambahkan.")
        print("ID Antrian Pengunjung:", id_pengunjung)
        print("Nama Pengunjung:", nama_pengunjung)
        print("Nama Santri yang Dijenguk:", nama_santri)
        print("Daerah Asal:", daerah.capitalize())

    elif pilihan == "2":
        print("\nDAFTAR PENGUNJUNG BERDASARKAN DAERAH (SUMATRA/KALIMANTAN/JAWA)")

        if len(data_kunjungan) == 0:
            print("Belum ada data pengunjung yang tersimpan.")
        else:
            for wilayah in ["sumatra", "kalimantan", "jawa"]:
                print("\nDaerah", wilayah.capitalize(),)
                ada_data = False
                for data in data_kunjungan:
                    if data[3] == wilayah:
                        print("ID Antrian:", data[0])
                        print("Nama Pengunjung:", data[1])
                        print("Nama Santri yang Dijenguk:", data[2])
                        print("Daerah Asal:", data[3].capitalize())
                        print()
                        ada_data = True
                if not ada_data:
                    print("Tidak ada data pengunjung dari daerah ini.")

    elif pilihan == "3":
        print("\nHAPUS DATA PENGUNJUNG BERDASARKAN ID ANTRIAN")

        if len(data_kunjungan) == 0:
            print("Tidak ada data yang dapat dihapus.")
        else:
            while True:
                try:
                    hapus_id = int(input("Masukkan ID antrian yang ingin dihapus: "))

                    ditemukan = False
                    for data in data_kunjungan:
                        if data[0] == hapus_id:
                            data_kunjungan.remove(data)
                            print("Data dengan ID antrian", hapus_id, "berhasil dihapus.")
                            ditemukan = True
                            break

                    if ditemukan:
                        id_antrian = 1
                        for d in data_kunjungan:
                            d[0] = id_antrian
                            id_antrian = id_antrian + 1
                        break
                        
                    else:
                        print("ID antrian yang dimasukkan tidak ditemukan.\nSilakan masukkan ID yang benar.\n")

                except:
                    print("Input tidak valid! ID antrian harus berupa angka.\nSilakan masukkan ulang.")

    elif pilihan == "4":
        print("\nMENGAKHIRI PROSES KUNJUNGAN SANTRI, KELUAR DARI PROGRAM")
        print("\nTerima kasih! Program Sistem Kunjungan Santri telah selesai dijalankan.\n")
        break

    else:
        print("\nPilihan menu tidak valid! Silakan pilih menu di nomor antara 1 hingga 4.")