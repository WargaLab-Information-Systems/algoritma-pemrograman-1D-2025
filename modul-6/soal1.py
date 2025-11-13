print ("\n" + "="*60)
print ("program sistem kunjungan santri ")
print ("="*60)

data_kunjungan = []
id_antrian = 1

while True:
    print("\n=== MENU SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Semua Data Pengunjung (urut daerah)")
    print("3. Hapus Data Pengunjung (berdasarkan ID)")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ").replace(" ", "")

    if pilih == "1":
        
        while True:
            nama_pengunjung = input("Masukkan nama pengunjung: ")
            if nama_pengunjung.replace(" ", "").isalpha():
                break
            else:
                print("Masukkan nama dengan huruf! Silakan ulangi.")

        
        while True:
            nama_santri = input("Masukkan nama santri yang dijenguk: ")
            if nama_santri.replace(" ", "").isalpha():
                break
            else:
                print("Masukkan nama dengan huruf! Silakan ulangi.")

        
        while True:
            daerah = input("Masukkan daerah (Sumatra/Kalimantan/Jawa): ").lower()
            if daerah not in ["sumatra", "kalimantan", "jawa"]:
                print("Masukkan daerah yang valid!")
            else:
                break

        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print("Data berhasil ditambahkan dengan ID:", id_antrian)
        id_antrian += 1

    elif pilih == "2":
        if len(data_kunjungan) == 0:
            print("Belum ada data kunjungan.")
        else:
            print("\n=== DAFTAR KUNJUNGAN ===")
            urut_daerah = ["sumatra", "kalimantan", "jawa"]
            for daerah in urut_daerah:
                for data in data_kunjungan:
                    if data[3] == daerah:
                        print(f"id antrian : {data[0]} | nama pengunjung : {data[1]} | nama santri : {data[2]} | daerah : {data[3]}")

    elif pilih == "3":
        if len(data_kunjungan) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            id_hapus = input("Masukkan ID yang ingin dihapus: ").replace(" ", "")
            if id_hapus.isdigit():
                id_hapus = int(id_hapus)
                ketemu = False
                for d in data_kunjungan:
                    if d[0] == id_hapus:
                        data_kunjungan.remove(d)
                        print("Data berhasil dihapus.")
                        ketemu = True
                        break
                if ketemu == False:
                    print("ID tidak ditemukan.")
            else:
                print("ID harus angka!")

    elif pilih == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan menu tidak valid!")
