data_kunjungan = []
id_counter = 1

def tambah_data():
    global id_counter
    print("\n=== Tambah Data Kunjungan ===")
    while True:
        nama_pengunjung = input("Nama Pengunjung: ")
        if nama_pengunjung.isalpha():
            break
        else:
            print("Nama tidak boleh mengandung angka! Silakan ulang.")
            continue

    while True:
        nama_santri = input("Nama Santri yang Dijenguk: ")
        if nama_santri.isalpha():
            break
        else:
            print("Nama tidak boleh mengandung angka! Silakan ulang.")
            continue

    while True:
        daerah = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Masukkan hanya: Sumatra, Kalimantan, atau Jawa!")
            continue

    data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan id_antrian: {id_counter}")
    id_counter += 1

def tampilkan_data():
    print("\n=== Daftar Kunjungan Berdasarkan Daerah ===")
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print(f"\nPengunjung dari {daerah}")
        ada = False
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}")
                ada = True
        if not ada:
            print("Tidak ada data.")

def hapus_data():
    print("\n=== Hapus Data Kunjungan ===")
    id_hapus = int(input("Masukkan id_antrian yang ingin dihapus: "))
    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")

while True:
    print("\n==== Sistem Kunjungan Santri ====")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")
        continue
