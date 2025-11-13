data_kunjungan = []     
id_counter = 1 
def tambah_pengunjung():
    global id_counter
    print("\n=== TAMBAH DATA PENGUNJUNG ===")
    
    nama = input("Nama pengunjung: ")
    if not nama.replace(" ", "").isalpha ():
        print("masukan huruffff,jangan angkaa!")
    santri = input("Nama santri yang dijenguk: ")
    if not santri.replace(" ", "").isalpha ():
        print("masukkan hurufff,jangan angkaaaa!")
    
    while True:
        
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")
        if not daerah.isalpha():
            print("Daerah tidak boleh angka atau simbol! Silakan ulangi.")
            continue
        if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
            print("Masukkan daerah yang valid (Sumatra/Kalimantan/Jawa)!")
        else:
            break
    
    data_kunjungan.append([nama, santri, daerah, id_counter])
    print(f"Pengunjung berhasil ditambahkan dengan ID {id_counter}")
    id_counter += 1

def tampilkan_data():
    print("\n=== Data Kunjungan Santri ===")

    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan:
        for data in data_kunjungan:
            if data[2].capitalize() == daerah.capitalize():
                print(f"ID: {data[3]} | Pengunjung: {data[0]} | Santri: {data[1]} | Daerah: {data[2]}")
    print()

def hapus_pengunjung():
    print("\n=== HAPUS DATA PENGUNJUNG ===")
    tampilkan_data()
    
    if not data_kunjungan:
        return
    
    id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
    
    for d in data_kunjungan:
        if d[3] == id_hapus:
            data_kunjungan.remove(d)
            print("Data berhasil dihapus!")
            return
    
    print("ID tidak ditemukan.")

while True:
    print("\n===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Pengunjung (Create)")
    print("2. Tampilkan Daftar Pengunjung (Read)")
    print("3. Hapus Data Pengunjung (Delete)")
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