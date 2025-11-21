kupon = {
    "Nora": 10,
    "Indah": 20,
    "Santa": 50     
}

barang = {}
total_setelah_diskon = 0   


def tampilkan_kupon():
    if kupon:
        print("\nKupon Yang Ada")
        for k, d in kupon.items():
            print(f"- {k} | Diskon {d}%")
    else:
        print("Tidak ada kupon tersisa.")


def tambah_data():
    global total_setelah_diskon

    while True:
        nama = input("Masukkan nama barang: ")
        if nama.replace(" ", "").isalpha():
            break
        print("Nama barang harus huruf!")

    while True:
        harga = input("Masukkan harga barang: ")
        if harga.isdigit():
            harga = int(harga)
            break
        print("Harga harus angka!")

    barang[nama] = harga
    total_setelah_diskon += harga   
    print(f"Barang '{nama}' ditambahkan.")


def tampilkan_pembelian():
    if not barang:
        print("Belum ada pembelian.")
        return

    print("\n===== Daftar Pembelian =====")
    for nama, harga in barang.items():
        print(f"Nama barang: {nama} | Harga: Rp {harga}")


def hitung_transaksi():
    global total_setelah_diskon

    if not barang:
        print("Belum ada barang.")
        return

    print(f"\nTotal belanja saat ini: Rp {total_setelah_diskon}")

    kode = input("Masukkan Kode Kupon (kosong jika tidak ada): ")

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total_setelah_diskon}")
        return

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total_setelah_diskon * (diskon / 100)
        total_setelah_diskon -= potongan    

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Potongan: Rp {int(potongan)}")
        print(f"Total setelah diskon: Rp {int(total_setelah_diskon)}")

        del kupon[kode]   
    else:
        print("Kupon tidak valid!")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tambah Barang")
        print("2. Tampilkan Pembelian")
        print("3. Tampilkan Kupon")
        print("4. Hitung Transaksi (Gunakan Kupon)")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == '1':
            tambah_data()
        elif pilih == '2':
            tampilkan_pembelian()
        elif pilih == '3':
            tampilkan_kupon()
        elif pilih == '4':
            hitung_transaksi()
        elif pilih == '5':
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid!")


menu()