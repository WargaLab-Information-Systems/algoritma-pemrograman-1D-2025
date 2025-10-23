while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total_harga = 0
    barang = []

    while True:
        nama_barang = input("Nama barang: ")
        if nama_barang == "selesai":
            break
        jumlah = int(input(f"Jumlah {nama_barang}: "))
        harga = int(input(f"Harga per item {nama_barang}: "))
        subtotal = jumlah * harga
        barang.append((nama_barang, jumlah, harga, subtotal))
        total_harga += subtotal

    print("\n=== Struk Pembelian ===")
    print("Nama Pembeli:", nama_pembeli)
    print("Daftar Belanja:")
    for b in barang:
        print(f"- {b[0]} ({b[1]} x {b[2]}) = {b[3]}")
    print("Total Harga:", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut != 'y':
        break
