data_kunjungan = []
id_counter = 1

def tambah_pengunjung():
    global id_counter
    print("\n=== TAMBAH DATA PENGUNJUNG ===")

    while True:
        nama = input("Nama pengunjung: ")
        if nama.replace(" ", "").isalpha():
            break
        print("Masukkan huruf saja, jangan angka!")

    while True:
        santri = input("Nama santri yang dijenguk: ")
        if santri.replace(" ", "").isalpha():
            break
        print("Masukkan huruf saja, jangan angka!")

    while True:
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")
        if daerah.capitalize() in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        print("Masukkan daerah yang valid!")

    data_kunjungan.append([nama, santri, daerah.capitalize(), id_counter])
    print(f"Pengunjung berhasil ditambahkan dengan ID {id_counter}")
    id_counter += 1


def tampilkan_data():
    print("\n=== DAFTAR PENGUNJUNG (URUT DAERAH) ===")

    if not data_kunjungan:
        print("Belum ada data.")
        return

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for daerah in urutan_daerah:
        print(f"\n--- {daerah} ---")
        for d in data_kunjungan:
            if d[2] == daerah:
                print(f"ID {d[3]} | Pengunjung: {d[0]} | Santri: {d[1]} | Daerah: {d[2]}")


def hapus_pengunjung():
    print("\n=== HAPUS DATA PENGUNJUNG ===")

    if not data_kunjungan:
        print("Belum ada data.")
        return

    tampilkan_data()

    id_hapus = input("\nMasukkan ID yang ingin dihapus: ")

    if not id_hapus.isdigit():
        print("ID harus angka!")
        return

    id_hapus = int(id_hapus)

    for d in data_kunjungan:
        if d[3] == id_hapus:
            data_kunjungan.remove(d)
            print("Data berhasil dihapus!")
            return

    print("ID tidak ditemukan.")


while True:
    print("\n===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_pengunjung()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        hapus_pengunjung()
    elif pilih == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
        break