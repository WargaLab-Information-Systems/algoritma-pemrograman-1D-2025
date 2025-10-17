# Program struk pembelian setiap pelanggan di sebuah IndoMei 

while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    daftar_barang = [] 
    total_harga = 0

    while True:
        nama_barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if nama_barang.lower() == "selesai":
            break

        harga_barang = int(input("Masukkan harga barang: "))
        daftar_barang.append((nama_barang, harga_barang))
        total_harga = total_harga + harga_barang 

    print("\nSTRUK PEMBELIAN INDOMEI")
    print("Nama Pembeli:", nama_pembeli)
    print("Daftar Barang:")
    for nama_barang, harga_barang in daftar_barang:
        print("-", nama_barang, ": Rp", harga_barang)
    print("Total Harga: Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")
    if ulang.lower() != "y":
        print("Program selesai. Semua transaksi telah dicetak.")
        break