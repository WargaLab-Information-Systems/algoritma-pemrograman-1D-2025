kupon = {
    "hemat10": 10,
    "belanja20": 20
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("Daftar Kupon:")
        for kode, diskon in kupon.items():
            print(f" {kode} : {diskon}%")

def tambah_kupon():
    kode = input("Masukkan kode kupon baru: ")
    while True:
        angka = input("Masukkan persentase diskon: ")
        if angka.isdigit():  
            diskon = int(angka)
            break
        else:
            print("Input harus berupa ANGKA! Silakan coba lagi.\n")
    kupon[kode] = diskon
    print("Kupon baru berhasil ditambahkan.")

def hapus_kupon():
    kode = input("Masukkan kode kupon yang ingin dihapus: ")
    if kode in kupon:
        del kupon[kode]
        print("Kupon berhasil dihapus.")
    else:
        print("Kupon tidak ditemukan.")

def proses_transaksi():
    total = float(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon (kosongkan jika tidak ada): ")

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total}")
        return

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        total_bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Total setelah diskon: Rp {total_bayar}")

        del kupon[kode]
    else:
        print("Kupon tidak valid! Tidak ada diskon.")
        print(f"Total yang harus dibayar: Rp {total}")

def menu():
    while True:
        print("\n=== SISTEM KASIR ===")
        print("1. Tampilkan kupon")
        print("2. Tambah kupon")
        print("3. Hapus kupon")
        print("4. Proses transaksi")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kupon()
        elif pilihan == "2":
            tambah_kupon()
        elif pilihan == "3":
            hapus_kupon()
        elif pilihan == "4":
            proses_transaksi()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menu() 