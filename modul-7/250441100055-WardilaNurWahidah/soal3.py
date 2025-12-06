kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon yang tersedia.")
        return

    print("\n=== DAFTAR KUPON TERSEDIA ===")
    for kode, diskon in kupon.items():
        print(f"{kode} -> Diskon {diskon}%")
    print()


def tambah_kupon():
    print("\n=== TAMBAH KUPON BARU ===")

    while True:
        kode = input("Masukkan kode kupon baru: ").strip().upper()

        if kode == "":
            print("Kode kupon tidak boleh kosong!")
            continue

        if kode in kupon:
            print("Kode kupon sudah ada dalam sistem!")
            continue

        break

    while True:
        try:
            diskon = float(input("Masukkan persentase diskon (1–100): "))

            if diskon <= 0 or diskon > 100:
                print("Diskon harus antara 1 sampai 100!")
                continue

            break

        except ValueError:
            print("Diskon harus berupa angka!")

    kupon[kode] = diskon
    print(f"Kupon {kode} (diskon {diskon}%) berhasil ditambahkan!\n")


def proses_transaksi():
    try:
        total = float(input("Masukkan total belanja: Rp "))
    except ValueError:
        print("Input total belanja harus berupa angka!")
        return

    kode = input("Masukkan kode kupon: ").strip().upper()

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total:,.0f}")
        return

    if kode not in kupon:
        print("Kupon tidak valid atau sudah digunakan!")
        return

    diskon = kupon[kode]
    potongan = total * (diskon / 100)
    total_bayar = total - potongan

    print(f"Kupon {kode} berhasil digunakan!")
    print(f"Diskon: {diskon}% (- Rp {potongan:,.0f})")
    print(f"Total bayar: Rp {total_bayar:,.0f}")

    del kupon[kode]
    print("Kupon telah dihapus dan tidak bisa digunakan lagi.\n")


def menu_kasir():
    while True:
        print("\n=== MENU KASIR ===")
        print("1. Tampilkan semua kupon")
        print("2. Proses transaksi")
        print("3. Tambah kupon baru")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kupon()
        elif pilihan == "2":
            proses_transaksi()
        elif pilihan == "3":
            tambah_kupon()
        elif pilihan == "0":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")


menu_kasir()