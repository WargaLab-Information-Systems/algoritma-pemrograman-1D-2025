while True:
    nama = input("Nama pembeli: ")
    barang = []
    harga = []

    while True:
        nama_barang = input("Nama barang : ")
        if nama_barang.lower() == "selesai":
            break
        harganya = int(input(f"Harga {nama_barang} (Rp): "))
        barang.append(nama_barang)
        harga.append(harganya)

    total = 0
    for h in harga:
        total += h

    print("\n=== Struk Pembelian IndoMei ===")
    print("Nama Pembeli:", nama)
    for i in range(len(barang)):
        print(f"{i+1}. {barang[i]} - Rp{harga[i]}")
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
    if lanjut != 'y':
        print("Program selesai. Terima kasih!")
        break