kupon = {
    "DISC10": 10,
    "PROMO20": 20,
    "SALE30": 30
}

def tampilkan_kupon():
    print("\n=== DAFTAR KUPON TERSEDIA ===")
    if len(kupon) == 0:
        print("Tidak ada kupon tersedia.")
    else:
        for kode, diskon in kupon.items():
            print(kode, ":", diskon, "%")

def proses_transaksi():
    print("\n=== PROSES TRANSAKSI PEMBELIAN BAJU ===")
    
    nama = input("Masukkan nama baju : ")
    if nama == "":
        print("Nama baju tidak boleh kosong!")
        return
    
    harga = input("Masukkan harga : ")
    if not harga.isdigit():
        print("Harga harus berupa angka ")
        return
    harga = int(harga)

    jumlah = input("Masukkan jumlah baju yang dibeli: ")
    if not jumlah.isdigit():
        print("Jumlah baju harus berupa angka!")
        return
    jumlah = int(jumlah)

    total = harga * jumlah
    print("\nTotal belanja untuk", nama, ":", total)

    kode = input("Masukkan kode kupon: ")

    if kode == "":
        print("Kode kupon tidak boleh kosong!")
        return
    
    if kode not in kupon:
        print("Kupon tidak valid atau sudah digunakan!")
        return

    diskon = kupon[kode]
    potongan = total * diskon / 100
    total_akhir = total - potongan

    print("\n=== STRUK PEMBELIAN BAJU ===")
    print("Nama        :", nama)
    print("Harga       :", harga)
    print("Jumlah      :", jumlah)
    print("Subtotal    :", total)
    print("Diskon      :", diskon, "%")
    print("Potongan    :", potongan)
    print("Total Bayar :", total_akhir)

    del kupon[kode]
    print("Kupon sudah dihapus dan tidak bisa dipakai lagi.")

# MENU UTAMA
while True:
    print("\n=== SISTEM KUPON DISKON TOKO BAJU ===")
    print("1. Tampilkan kupon")
    print("2. Proses transaksi pembelian")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")