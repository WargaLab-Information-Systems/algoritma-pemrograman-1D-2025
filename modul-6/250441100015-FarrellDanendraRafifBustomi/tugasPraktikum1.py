dataKunjungan = []
id_antrian = 1

def tambah_data():
    global id_antrian

    print("\n=== Tambah Data Pengunjung ===")

    while True:
        namaPengunjung = input("Masukkan nama pengunjung: ")
        if not namaPengunjung.replace(" ", "").isalpha():
            print("Nama pengunjung tidak boleh mengandung angka atau simbol! Coba lagi.\n")
            continue
        break

    while True:
        namaSantri = input("Masukkan nama santri yang dijenguk: ")
        if not namaSantri.replace(" ", "").isalpha():
            print("Nama santri tidak boleh mengandung angka atau simbol! Coba lagi.\n")
            continue
        break

    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah tidak valid! Harus Sumatra, Kalimantan, atau Jawa. Silakan coba lagi.\n")

    dataKunjungan.append([id_antrian, namaPengunjung, namaSantri, daerah])
    print(f"Data berhasil ditambahkan! ID Antrian: {id_antrian}")
    id_antrian += 1


def tampilkan_data():
    print("\n=== Daftar Pengunjung Berdasarkan Daerah ===")

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    if not dataKunjungan:
        print("Belum ada data pengunjung.")
        return

    for daerah in urutan_daerah:
        print(f"\n-- Daerah {daerah} --")
        for data in dataKunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}")


def hapus_data():
    global id_antrian
    print("\n=== Hapus Data Pengunjung ===")

    if not dataKunjungan:
        print("Belum ada data pengunjung untuk dihapus.\n")
        return

    try:
        id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
        for data in dataKunjungan:
            if data[0] == id_hapus:
                dataKunjungan.remove(data)
                print(f"Data dengan ID {id_hapus} berhasil dihapus!")

                id_antrian = 1
                for d in dataKunjungan:
                    d[0] = id_antrian
                    id_antrian += 1
                return

        print("ID tidak ditemukan!\n")
    except ValueError:
        print("Input harus berupa angka!\n")


while True:
    print("\n===== Sistem Kunjungan Santri =====")
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
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
