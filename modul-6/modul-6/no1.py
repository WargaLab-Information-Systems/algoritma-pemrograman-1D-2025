data_kunjungan = []
id_counter = 1
def tambah_pengunjung(id_antrian_saat_ini):
    print("\n--- Tambah Pengunjung ---")
    while True:
        nama_pengunjung = str(input("Masukkan Nama Pengunjung: ")).strip()
        if nama_pengunjung.isalpha():
            break
        print("Nama pengunjung tidak boleh kosong/angka. Silakan coba lagi.")
    while True:
        nama_santri = input("Masukkan Nama Santri yang Dijenguk: ").strip()
        if nama_santri.isalpha():
            break
        print("Nama santri tidak boleh kosong/angka. Silakan coba lagi.")
    while True:
        daerah_asal = input("Masukkan Daerah Asal (Sumatra, Kalimantan, atau Jawa): ").strip()
        if daerah_asal in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        print("Daerah asal tidak valid. Harap masukkan 'Sumatra', 'Kalimantan', atau 'Jawa'.")
    data_kunjungan.append([id_antrian_saat_ini, nama_pengunjung, nama_santri, daerah_asal])
    print(f" Data pengunjung {nama_pengunjung} berhasil ditambahkan.")
    print(f"   ID Antrian Anda adalah: {id_antrian_saat_ini}")
    return id_antrian_saat_ini + 1
def tampilkan_daftar_pengunjung():
    print("\n--- Daftar Pengunjung ---")
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    data_urut = data_kunjungan.copy()
    n = len(data_urut)
    for i in range(n):
        for j in range(0, n - i - 1):
            if urutan_daerah.index(data_urut[j][3]) > urutan_daerah.index(data_urut[j+1][3]):
                data_urut[j], data_urut[j+1] = data_urut[j+1], data_urut[j]
    print("-" * 62)
    for id_antrian, pengunjung, santri, daerah in data_urut:
        print(f"id antrian = {id_antrian} | nama pengunjung = {pengunjung} | nama santri = {santri} | daerah asal = {daerah}")
    print("-" * 62)
def hapus_pengunjung():
    print("--- Hapus Pengunjung ---")
    if not data_kunjungan:
        print(" Belum ada data kunjungan yang dapat dihapus.")
        return
    print("ID Antrian yang Tersedia: ", [data[0] for data in data_kunjungan])
    try:
        id_hapus = int(input("Masukkan ID Antrian yang akan dihapus: "))
    except ValueError:
        print("Input tidak valid. masukkan angka untuk ID Antrian.")
        return
    found = False
    for i, data in enumerate(data_kunjungan):
        if data[0] == id_hapus:
            data_yang_dihapus = data_kunjungan.pop(i)
            print(f"Data ID Antrian {id_hapus} ({data_yang_dihapus[1]}) berhasil dihapus.")
            found = True
            break
    if not found: 
        print(f" ID Antrian {id_hapus} tidak ditemukan.")
def tampilkan_menu():
    print("KUNJUNGAN SANTRI")
    print("="*40)
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung (Berdasarkan ID)")
    print("4. Keluar")
    print("="*40)
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan Anda (1-4): ")
    if pilihan == '1':
        id_counter = tambah_pengunjung(id_counter)
    elif pilihan == '2':
        tampilkan_daftar_pengunjung()
    elif pilihan == '3':
        hapus_pengunjung()
    elif pilihan == '4':
        print("Selesai")
        break
    else:
        print(" tidak valid. Silakan masukkan angka antara 1 dan 4.")