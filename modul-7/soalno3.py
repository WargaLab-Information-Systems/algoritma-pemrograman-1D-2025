barang = {}   

kupon = {     
    "SYUKRONGUYY20": 20,
    "DISKONMALL50": 50,
    "SABARYAAA30": 30,
    "BUTUHCUAN25": 25
}

def validasi_nama_barang(nama):
    if nama == "":
        print("Nama barang tidak boleh kosong!")
        return False

    if " " in nama.strip() and nama.strip() == "":
        print("Nama barang tidak boleh hanya spasi!")
        return False

    return True

def tambah_barang():
    print("\n=== TAMBAH BARANG ===")

    while True:
        nama = input("Masukkan nama barang: ").strip()
        if not validasi_nama_barang(nama):
            continue

        if nama in barang:
            print("Barang sudah ada! Tidak boleh duplikat.")
            continue

        break


    while True:
        try:
            harga = float(input("Masukkan harga barang: Rp "))
            if harga <= 0:
                print("Harga harus lebih dari 0!")
                continue
            break
        except:
            print("Harga harus berupa angka!")

    barang[nama] = harga
    print(f"Barang '{nama}' berhasil ditambahkan!")


def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")
    if not barang:
        print("Belum ada barang.")
        return

    for nama, harga in barang.items():
        print(f"- {nama} : Rp {harga}")


def proses_transaksi():
    print("\n=== PROSES TRANSAKSI ===")

    if not barang:
        print("Belum ada barang yang bisa dibeli!")
        return

    
    tampilkan_barang()

    nama = input("\nMasukkan nama barang yang dibeli: ").strip()

    if nama not in barang:
        print("Barang tidak ditemukan!")
        return

    harga = barang[nama]

   
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pembelian: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            break
        except:
            print("Jumlah harus angka!")

    total = harga * jumlah
    print(f"\nTotal sebelum diskon: Rp {total}")

    # Masukkan kupon
    kode = input("Masukkan kode kupon (atau kosong): ").upper().strip()

    if kode == "":
        print(f"Total bayar: Rp {total}")
        return

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        total_bayar = total - potongan

        print(f"\nKupon valid! Diskon {diskon}%")
        print(f"Potongan: Rp {potongan}")
        print(f"Total bayar: Rp {total_bayar}")

        del kupon[kode]
        print("Kupon sudah dihapus (tidak bisa dipakai lagi).")

    else:
        print("Kupon tidak valid!")
        print(f"Total bayar: Rp {total}")

def menu():
    while True:
        print("\n===== SISTEM KASIR =====")
        print("1. Tambah barang")
        print("2. Tampilkan barang")
        print("3. Proses transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_barang()
        elif pilihan == "3":
            proses_transaksi()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan kasir!")
            break
        else:
            print("Pilihan tidak valid!")

menu()
