keranjang = []

kupon = {
    "disc10": 10,
    "disc20": 20,
    "bonus5": 5
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersisa.")
    else:
        print("\n=== DAFTAR KUPON ===")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}, Diskon: {diskon}%")

def tambah_barang():
    nama = input("Nama barang: ").lower()
    try:
        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))
    except:
        print("Harga dan jumlah harus angka.")
        return
    
    keranjang.append([nama, harga, jumlah])
    print("Barang ditambahkan ke keranjang.")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    
    print("\n=== KERANJANG BELANJA ===")
    total = 0
    for i, item in enumerate(keranjang, start=1):
        nama, harga, jumlah = item
        subtotal = harga * jumlah
        total += subtotal
        print(f"{i}. {nama} - {harga} x {jumlah} = {subtotal}")
    print(f"Total sementara: {total}")

def hapus_barang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    
    lihat_keranjang()
    try:
        index = int(input("Nomor barang yang ingin dihapus: "))
        keranjang.pop(index - 1)
        print("Barang dihapus.")
    except:
        print("Input tidak valid.")

def proses_pembayaran():
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    
    total = sum(harga * jumlah for nama, harga, jumlah in keranjang)
    print(f"\nTotal belanja: {total}")

    kode = input("Masukkan kode kupon (atau kosongkan): ").lower()

    if kode == "":
        print(f"Total bayar: {total}")
    elif kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        total_bayar = total - potongan
        print(f"Kupon {diskon}% diterapkan!")
        print(f"Total bayar: {total_bayar}")
        del kupon[kode]
    else:
        print("Kode kupon tidak valid.")
        print(f"Total bayar tetap: {total}")
    
    keranjang.clear()
    print("Transaksi selesai. Keranjang dikosongkan.")


while True:
    print("\n=== PROGRAM KASIR SEDERHANA ===")
    print("1. Tambah barang")
    print("2. Lihat keranjang")
    print("3. Hapus barang")
    print("4. Tampilkan kupon")
    print("5. Proses pembayaran")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        lihat_keranjang()
    elif pilih == "3":
        hapus_barang()
    elif pilih == "4":
        tampilkan_kupon()
    elif pilih == "5":
        proses_pembayaran()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")
