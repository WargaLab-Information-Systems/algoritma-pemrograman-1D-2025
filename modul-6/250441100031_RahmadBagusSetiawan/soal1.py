
data_kunjungan = []  
id_counter = 1       

def validasi_nama(teks):
    for huruf in teks:
        if huruf.isdigit():
            return False
    return True

def tambah_data():
    global id_counter

    while True:
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        if not validasi_nama(nama_pengunjung):
            print("❌ Nama tidak boleh mengandung angka. Coba lagi!")
            continue

        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        if not validasi_nama(nama_santri):
            print("❌ Nama santri tidak boleh mengandung angka. Coba lagi!")
            continue

        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").lower()

        if daerah not in ["sumatra", "kalimantan", "jawa"]:
            print("❌ Daerah asal harus Sumatra, Kalimantan, atau Jawa!")
            continue

        data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
        print("✅ Data berhasil ditambahkan dengan ID:", id_counter)
        id_counter += 1
        break


def tampilkan_data():
    if not data_kunjungan:
        print("📭 Belum ada data pengunjung.")
        return

    print("\n=== DAFTAR KUNJUNGAN SANTRI ===")
    urutan_daerah = ["sumatra", "kalimantan", "jawa"]

    for daerah in urutan_daerah:
        print(f"\n-- Pengunjung dari {daerah.capitalize()} --")
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}")


def hapus_data():
    if not data_kunjungan:
        print("📭 Belum ada data yang bisa dihapus.")
        return

    try:
        id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
        for data in data_kunjungan:
            if data[0] == id_hapus:
                data_kunjungan.remove(data)
                print("🗑️ Data berhasil dihapus!")
                return
        print("❌ ID tidak ditemukan.")
    except ValueError:
        print("❌ ID harus berupa angka!")


def menu():
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")


while True:
    menu()
    pilihan = input("Pilih menu (1-4): ").strip()


    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        print("👋 Program selesai. Terima kasih!")
        break
    else:
        print("❌ Pilihan tidak valid! Silakan pilih 1 - 4.")
