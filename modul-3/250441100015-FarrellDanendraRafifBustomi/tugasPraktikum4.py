while True:
    print("=== Program Struk Pembelian IndoMei ===")
    nama = input("Masukkan nama pembeli: ")

    daftar_barang = []
    daftar_harga = []

    while True:
        barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        daftar_barang.append(barang)
        daftar_harga.append(harga)

        while True:
            lagi = input("Apakah ingin menambah barang lagi? (y/n): ").lower()
            if lagi == "y":
                break
            elif lagi == "n":
                break
            else:
                print("Huruf tidak sesuai! Mohon pilih y atau n.")
        if lagi == "n":
            break

    total = sum(daftar_harga)

    print("\n=== Struk Pembelian IndoMei ===")
    print("Nama Pembeli :", nama)
    print("-------------------------------")
    for i in range(len(daftar_barang)):
        print(f"{i+1}. {daftar_barang[i]} - Rp{daftar_harga[i]}")
    print("-------------------------------")
    print("Total Harga : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")
    print("===============================\n")

    while True:
        lanjut = input("Apakah ada pembeli berikutnya? (y/n): ").lower()
        if lanjut == "y":
            break
        elif lanjut == "n":
            print("Program selesai. Semua transaksi telah dicatat.")
            exit()  
        else:
            print("Huruf tidak sesuai! Mohon pilih y atau n.")
            