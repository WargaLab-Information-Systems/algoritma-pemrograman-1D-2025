kunjungan = []

id_terakhir = 0

def cek_huruf(teks):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_kapital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for karakter in teks:
        if karakter not in huruf_kecil and huruf_kapital and karakter != " ":
            return False
    return True

def tambah_kunjungan(kunjungan, id_terakhir):
    print("\n=== Tambah Data Kunjungan ===")
    while True:
      nama_pengunjung = input("Masukkan nama pengunjung: ")
      if cek_huruf(nama_pengunjung):
          break
      else:
          print("nama pengunjung hanya berisi huruf dan spasi")
    while True:
       nama_santri = input("Masukkan nama santri yang dijenguk: ")
       if cek_huruf(nama_santri):
            break
       else:
           print(" Nama santri hanya boleh berisi huruf dan spasi!")

    while True:
        daerah = input("Masukkan daerah asal (Sumatra / Kalimantan / Jawa): ")
        if daerah.lower() in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print("Daerah hanya boleh Sumatra, Kalimantan, atau Jawa!")

    id_terakhir += 1

    data = [id_terakhir, nama_pengunjung, nama_santri, daerah]
    kunjungan.append(data)
    print(" Data berhasil ditambahkan!\n")
    return id_terakhir

def tampilkan_kunjungan(kunjungan):
    print("\n=== Daftar Kunjungan Santri ===")

    if len(kunjungan) == 0:
        print("Belum ada data kunjungan.")
        return

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for daerah in urutan_daerah:
        print(f"\n-- Pengunjung dari {daerah} --")
        ada_data = False
        for data in kunjungan:
            if data[3].lower() == daerah.lower(): 
                ada_data = True
                print(f"ID: {data[0]} | Nama: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")
        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")


def hapus_kunjungan(kunjungan):
    print("\n=== Hapus Data Kunjungan ===")
    if len(kunjungan) == 0:
        print("Belum ada data untuk dihapus.")
        return

    try:
        id_hapus = int(input("Masukkan ID antrian yang akan dihapus: "))
        ditemukan = False
        for data in kunjungan:
            if data[0] == id_hapus:
                kunjungan.remove(data)
                ditemukan = True
                print(" Data berhasil dihapus!\n")
                break
        if not ditemukan:
            print(" ID tidak ditemukan.")
    except ValueError:
        print("Masukkan angka yang valid untuk ID.")


while True:
    print("\n=== MENU SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Daftar Kunjungan")
    print("3. Hapus Data Kunjungan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        id_terakhir = tambah_kunjungan(kunjungan, id_terakhir)
    elif pilihan == "2":
        tampilkan_kunjungan(kunjungan)
    elif pilihan == "3":
        hapus_kunjungan(kunjungan)
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.") 