kupon = {}

def tampilkan_kupon():
    if not kupon:
        print("Belum ada kupon tersimpan.")
        lanjut = input("Apakah ingin lanjut menampilkan kupon? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("\n=== DAFTAR KUPON TERSEDIA ===")
        for kode, diskon in kupon.items():
            print(f"{kode} -> {diskon}%")

def tambah_kupon():
    while True:
        kode = input("Masukkan kode kupon baru: ").upper()
        if kode in kupon:
            print("Kode kupon sudah ada!")
            continue
        break

    while True:
        diskon = input("Masukkan persentase diskon (1-100): ")
        if not diskon.isdigit():
            print("Diskon harus berupa angka dan tidak boleh bernilai negatif!")
            continue
        diskon = int(diskon)
        if diskon < 1 or diskon > 100:
            print("Diskon harus di antara 1-100!")
            continue
        break

    kupon[kode] = diskon
    print("Kupon berhasil ditambahkan!")

def hapus_kupon():
    if not kupon:
        print("Belum ada kupon tersimpan.")
        lanjut = input("Apakah ingin lanjut menghapus kupon? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    kode = input("Masukkan kode kupon yang ingin dihapus: ").upper()
    if kode not in kupon:
        print("Kupon tidak ditemukan.")
        return
    del kupon[kode]
    print("Kupon berhasil dihapus.")


def proses_transaksi():
    while True:
        total = input("Masukkan total belanja: ")
        if not total.isdigit():
            print("Total belanja harus berupa angka!")
            continue
        total = int(total)
        break 

    pakai = input("Apakah ada kupon (y/n): ").lower()

    if pakai == "n":
        print("\n===RINCIAN TRANSAKSI===")
        print("Tidak menggunakan kupon.")
        print(f"Total yang harus dibayar: Rp{total:,}")
        return
    elif pakai != "y":
        print("\n=== RINCIAN TRANSAKSI ===")
        print("Input tidak dikenal. Transaksi tanpa kupon.")
        print(f"Total yang harus dibayar: Rp{total:,}")
        return

    kode = input("Masukkan kode kupon: ").upper()

    if kode not in kupon:
        print("\n=== RINCIAN TRANSAKSI ===")
        print(f"Kupon '{kode}' tidak valid atau tidak tersedia.")
        print(f"Total yang harus dibayar: Rp{total:,}")
        return

    diskon = kupon[kode]
    potongan = total * diskon / 100
    total_bayar = total - potongan

    print("\n=== RINCIAN TRANSAKSI ===")
    print(f"Harga sebelum diskon: Rp{total:,}")
    print(f"Kupon valid! Diskon {diskon}%")
    print(f"Potongan: Rp{int(potongan):,}")
    print(f"Total bayar: Rp{int(total_bayar):,}")

    del kupon[kode]
    print("Kupon telah dihapus karena sudah digunakan.")



def menu():
    while True:
        print("\n=== SISTEM KUPON DISKON ===")
        print("1. Tampilkan semua kupon")
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
            print("Pilihan tidak valid!")

menu()