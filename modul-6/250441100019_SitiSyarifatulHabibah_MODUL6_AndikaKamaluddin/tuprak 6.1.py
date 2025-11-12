d_kunjungan = []
id_antri = 1

while True:
    print("===================================")
    print("===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Menambah data pengunjung")
    print("2. Menampilkan semua data pengunjung")
    print("3. Ngehapus data pengunjung")
    print("4. EXIT")
    pilihan = input("Choose menu:")

    if pilihan == "1":
        name_pengunjung = input("Nama pengunjung:")
        name_santri = input("Nama santri yang dikunjungi:")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")

        d_kunjungan.append([id_antri, name_pengunjung, name_santri, daerah])
        print("Data berhasil ditambahkan dengan ID antrian: ", id_antri)
        id_antri = id_antri + 1

    elif pilihan == "2":
        print("===================================")
        print("===================================")
        print("Daftar Kunjungan Santri")
        urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
        for daerah in urutan_daerah:
            print(f"daerah: {daerah}")
            for data in d_kunjungan:
                if data[3] == daerah:
                    print(f"id:{data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
                    print("===================================")

    elif pilihan == "3":
        for daerah in urutan_daerah:
            print(f"daerah: {daerah}")
            for data in d_kunjungan:
                if data[3] == daerah:
                    print(f"id:{data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
                    print("===================================")
        
        hapus = int(input("Masukkan id santri yang mau dihapus: "))
        ditemukan = False
        for data in d_kunjungan:
            if data[0] == hapus:
                d_kunjungan.remove(data)
                ditemukan = True
                print("Data berhasil dihapus!")
                break
        if not ditemukan:
            print("ID tidak ditemukan, cek lagi")
            
    elif pilihan == "4":
        print("Program ditutup")
        break
    else:
        print("Pilihan tidak tersedia")