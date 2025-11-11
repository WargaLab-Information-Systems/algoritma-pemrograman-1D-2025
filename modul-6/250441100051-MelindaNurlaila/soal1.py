kunjungan = []

def tambah_kunjungan():
    print("=== Tambah Data Kunjungan ===")

    while True:
        try:
            id_antrian = int(input("Masukkan ID Antrian: "))
            sudah_ada = False
            for data in kunjungan:
                if data[0] == id_antrian:
                    sudah_ada = True
                    break
            if sudah_ada:
                print("ID tersebut sudah digunakan! Masukkan ID lain.")
            else:
                break
        except ValueError:
            print("ID harus berupa angka!")
  
    nama_pengunjung = input("Masukkan nama pengunjung : ")
    
    nama_santri = input("Masukkan nama santri yang dijenguk : ")

    while True:
        daerah_asal = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah_asal in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah asal tidak valid! Harus 'Sumatra', 'Kalimantan', atau 'Jawa'.")

    kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah_asal])
    print(f"Data berhasil ditambahkan dengan ID Antrian: {id_antrian}")

def tampilkan_kunjungan():
    if not kunjungan:
        print("Belum ada data kunjungan.")
        return

    print("=== Daftar Kunjungan Santri ===")
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for daerah in urutan_daerah:
        data_daerah = []
        for data in kunjungan:
            if data [3] == daerah:
                data_daerah.append(data)

        if data_daerah:
            print(f"--- Pengunjung dari {daerah} ---")
            for data in data_daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Asal: {data[3]}")

def hapus_kunjungan():
    if not kunjungan:
        print("Tidak ada data untuk dihapus.")
        return

    try:
        id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
        for data in kunjungan:
            if data[0] == id_hapus:
                kunjungan.remove(data)
                print(f"Data dengan ID {id_hapus} berhasil dihapus.")
                return
            print("Data dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("ID harus berupa angka!")

def menu():
    while True:
        print("\n===== Sistem Kunjungan Santri =====")
        print("1. Tambah Data Kunjungan")
        print("2. Tampilkan Seluruh Kunjungan")
        print("3. Hapus Data Kunjungan")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tambah_kunjungan()
        elif pilihan == "2":
            tampilkan_kunjungan()
        elif pilihan == "3":
            hapus_kunjungan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

menu()