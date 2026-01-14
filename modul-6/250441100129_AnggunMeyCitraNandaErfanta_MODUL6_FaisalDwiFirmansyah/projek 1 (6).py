data_kunjungan = []
# nomor_antrian = 1

def tambah_pengunjung():
    nomor_antrian = len(data_kunjungan)+1
    
    print("\n--- Tambah Data Pengunjung ---")
    
    nama = input("Nama Pengunjung: ")
    santri = input("Nama Santri yang Dijenguk: ")
    
    daerah = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ")
    
    while daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
        print("Daerah harus Sumatra, Kalimantan, atau Jawa!")
        daerah = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ")
    
    data_kunjungan.append([nomor_antrian, nama, santri, daerah])
    
    print(f"Berhasil ditambah! Nomor Antrian: {nomor_antrian}")
    
    nomor_antrian += 1
    

def lihat_pengunjung():
    print("\n--- Daftar Pengunjung ---")
    
    if len(data_kunjungan) == 0:
        print("Belum ada data pengunjung")
        return
    
    print("\n* Daerah SUMATRA:")
    
    ada_data = False
    
    for data in data_kunjungan:
        if data[3] == "Sumatra":
            print(f"  ID: {data[0]} - {data[1]} menjenguk {data[2]}")
            ada_data = True
    
    if not ada_data:
        print("  (Tidak ada data)")
    
    print("\n* Daerah KALIMANTAN:")
    
    ada_data = False
    
    for data in data_kunjungan:
        if data[3] == "Kalimantan":
            print(f"  ID: {data[0]} - {data[1]} menjenguk {data[2]}")
            ada_data = True
    
    if not ada_data:
        print("  (Tidak ada data)")
    
    print("\n* Daerah JAWA:")
    
    ada_data = False
    
    for data in data_kunjungan:
        if data[3] == "Jawa":
            print(f"  ID: {data[0]} - {data[1]} menjenguk {data[2]}")
            ada_data = True
    
    if not ada_data:
        print("  (Tidak ada data)")

def hapus_pengunjung():
    print("\n--- Hapus Data Pengunjung ---")
    
    if len(data_kunjungan) == 0:
        print("Belum ada data untuk dihapus")
        return
    
    print("Data saat ini:")
    
    for data in data_kunjungan:
        print(f"ID: {data[0]} - {data[1]} - Daerah: {data[3]}")
    
    try:
        id_hapus = int(input("\nMasukkan ID yang akan dihapus: "))
        
        for i in range(len(data_kunjungan)):
            if data_kunjungan[i][0] == id_hapus:
                data_kunjungan.remove(i)
                print(f"Data dengan ID {id_hapus} berhasil dihapus!")
                return
        
        print(f"Data dengan ID {id_hapus} tidak ditemukan!")
        
    except:
        print("ID harus berupa angka!")

def menu_utama():
    print("=== SISTEM KUNJUNGAN SANTRI ===")
    
    while True:
        print("\nMenu:")
        print("1. Tambah Pengunjung")
        print("2. Lihat Daftar Pengunjung") 
        print("3. Hapus Pengunjung")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_pengunjung()
        elif pilihan == "2":
            lihat_pengunjung()
        elif pilihan == "3":
            hapus_pengunjung()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-4.")

menu_utama()