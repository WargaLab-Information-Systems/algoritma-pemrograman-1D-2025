while True:
    print("\n=== Program Kasir IndoMei ===")
    nama_pembeli = input("Masukkan nama pembeli: ")
    total = 0
    struk_barang_str = "" 
    while True:
        barang = input("Nama barang: ")
        harga = float(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))
        subtotal = harga * jumlah
        total += subtotal
        struk_barang_str += f"{barang} (x{jumlah}) = Rp{subtotal:,.0f}\n"
        lagi = input("Tambah barang lagi? (y/n): ").lower()
        if lagi == "n":
            break
    print("\n===== STRUK PEMBELIAN =====")
    print(f"Nama Pembeli:",nama_pembeli)
    print("----------------------------")
    print(struk_barang_str.strip()) 
    print("----------------------------")
    print(f"Total Harga : Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei ")
    print("============================")
    pembeli_lain = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
    if pembeli_lain == "n":
        print("Program selesai. Sampai jumpa!")   