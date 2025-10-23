while True:
    nama_pembeli = input("Masukkan nama pembeli:")
    total = 0
    
    while True:
        barang_dibeli = input("Masukkan nama barang:")
        harga_barang = int(input("Masukkan harga barang:"))
        total = total + harga_barang

        lagi = input("Apa mau tambah barang lagi? (yea/nono):")
        if lagi == "nono":
            break
    print("=== Struk pembelian Toko IndoMei ===")
    print("Nama pembeli:", nama_pembeli)
    print("Total harga:", total)
    print("Terimakasih telah berbelanja di IndoMei")

    ulang = input("Apa ada pembeli lain selanjutnya? (yea/nono):")
    if ulang == "nono":
        break
 
