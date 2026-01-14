data_kunjungan = []       

def tambah_pengunjung():
    id_antrian = len(data_kunjungan)+1
    print("\n=== TAMBAH DATA PENGUNJUNG ===")
    while True:
        nama = input("Nama pengunjung: ")
        if not nama.replace(" ", "").isalpha():
            print("masukan huruffff,jangan angkaa!")
            continue
        else:
            break

    while True:
        santri = input("Nama santri yang dijenguk: ")
        if not santri.replace(" ", "").isalpha ():
            print("masukkan hurufff,jangan angkaaaa!")
            continue
        else:
            break
            
    while True:
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if not daerah.isalpha():
            print("Daerah tidak boleh angka atau simbol! Silakan ulangi.")
            continue
        elif daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
            print("Masukkan daerah yang valid (Sumatra/Kalimantan/Jawa)!")
            continue
        else:
            break

    data_kunjungan.append([id_antrian, nama, santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID {id_antrian}!\n")
    
def tampilkan_data():
    if len(data_kunjungan) == 0:
        print("\nBelum ada data kunjungan.")
    else:
        print("\n=== DAFTAR KUNJUNGAN SANTRI ===")
        for data in data_kunjungan:
            print(f"ID {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")

def hapus_pengunjung():
    if len(data_kunjungan) == 0:
        print("\nBelum ada data yang bisa dihapus.")
        return

    try:
        id_hapus = int(input("\nMasukkan ID pengunjung yang ingin dihapus: "))
        indeks = -1

        for i in range(len(data_kunjungan)):
            if data_kunjungan[i][0] == id_hapus:
                indeks = i
                break

        if indeks != -1:
            for j in range(indeks, len(data_kunjungan) - 1):
                data_kunjungan[j] = data_kunjungan[j + 1]
            data_kunjungan.pop()
            print(f"Data dengan ID {id_hapus} berhasil dihapus.")
        else:
            print("Data dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("Input ID harus berupa angka!")

def tampilkan_berdasarkan_daerah():
    if len(data_kunjungan) == 0:
        print("\nBelum ada data kunjungan.")
        return

    print("\n=== DATA BERDASARKAN DAERAH ===")
    
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for daerah in urutan_daerah:
        print(f"\n--- Pengunjung dari {daerah} ---")
        ada_data = False

        for data in data_kunjungan:
            if data[3].lower() == daerah.lower():
                print(f"ID {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")
                ada_data = True

        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")

while True:
    print("\n===== MENU SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah data pengunjung")
    print("2. Tampilkan semua data pengunjung")
    print("3. Hapus data pengunjung")
    print("4. Tampilkan data berdasarkan daerah")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_pengunjung()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_pengunjung()
    elif pilihan == "4":
        tampilkan_berdasarkan_daerah()
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")