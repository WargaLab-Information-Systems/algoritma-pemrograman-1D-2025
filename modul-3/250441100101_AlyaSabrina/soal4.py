while True:
    nama = input("Masukkan nama pembeli : ")

    # Nama hanya boleh huruf
    while not nama.isalpha():
        print("Nama hanya boleh huruf!")
        nama = input("Masukkan nama pembeli : ")

    total = 0
    daftar_barang = []

    while True:
        barang = input("Masukkan nama barang : ")

        # Nama barang tidak boleh angka saja
        if barang.isdigit():
            print("Nama barang tidak boleh angka saja!")
            continue

        # Harga harus angka
        while True:
            harga = input("Masukkan harga barang : ")
            if harga.isdigit():
                harga = int(harga)
                break
            else:
                print("Harga harus angka!")

        total += harga
        daftar_barang.append((barang, harga))

        lagi_barang = input("Apakah ada barang lagi? (y/n): ")
        if lagi_barang == "n":
            break

    # Tampilkan hasil belanja
    print("\n===== STRUK BELANJA =====")
    print("Nama Pembeli:", nama)
    print("--------------------------")
    for item, harga in daftar_barang:
        print(item, "-", "Rp", harga)
    print("--------------------------")
    print("Total Belanja: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei !\n")

    lagi = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lagi == "n":
        print("Program selesai.")
        break