daftar_pengunjung = []
nomor_antrian = 1

def input_pengunjung_baru():
    global nomor_antrian
    print("\n=== Tambah Data Kunjungan ===")
    while True:
        nama_tamu = input("Nama Pengunjung: ")
        if nama_tamu.isalpha():
            break
        else:
            print("Nama tamu tidak boleh berupa angka.")
            continue

    while True:
        nama_murid = input("Nama Santri yang Dijenguk: ")
        if nama_murid.isalpha():
            break
        else:
            print("Nama murid tidak boleh berupa angka.")
            continue

    while True:
        asal_wilayah = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if asal_wilayah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Masukkan hanya: Sumatra, Kalimantan, atau Jawa!")
            continue

    daftar_pengunjung.append([nomor_antrian, nama_tamu, nama_murid, asal_wilayah])
    print(f"Data berhasil ditambahkan dengan id_antrian: {nomor_antrian}")
    nomor_antrian += 1

def lihat_daftar_berdasarkan_daerah():
    print("\n=== Daftar Kunjungan Berdasarkan Daerah ===")
    urutan_wilayah = ["Sumatra", "Kalimantan", "Jawa"]
    for wilayah in urutan_wilayah:
        print(f"\nPengunjung dari {wilayah}")
        ditemukan = False
        for entri in daftar_pengunjung:
            if entri[3] == wilayah:
                print(f"ID: {entri[0]}, Pengunjung: {entri[1]}, Santri: {entri[2]}")
                ditemukan = True
        if not ditemukan:
            print("Tidak ada data.")

def hapus_entri_pengunjung():
    print("\n=== Hapus Data Kunjungan ===")
    if not daftar_pengunjung:
        print("tidak ada data")
        return
    id_hapus = int(input("Masukkan id_antrian yang ingin dihapus: "))
    for entri in daftar_pengunjung:
        if entri[0] == id_hapus:
            daftar_pengunjung.remove(entri)
            print("Data berhasil dihapus.")
            return
    print("ID tidak ditemukan.")


while True:
    print("\n=== Sistem Kunjungan Santri ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan_user = input("Pilih menu (1-4): ")

    if pilihan_user == "1":
        input_pengunjung_baru()
    elif pilihan_user == "2":
        lihat_daftar_berdasarkan_daerah()
    elif pilihan_user == "3":
        hapus_entri_pengunjung()
    elif pilihan_user == "4":
        break
    else:
        print("Pilihan tidak valid.")
        continue