while True:
    nama = input("Masukkan nama pembeli : ")

    total_harga = 0
    nomor = 1
    daftar_barang = ""

    print("Masukkan nama dan harga barang (ketik 'n' jika sudah selesai):")

    while True:
        nama_barang = input("Masukkan nama barang : ")
        if nama_barang == "n":
            break

        harga = int(input("Masukkan harga barang (Rp) : "))

        total_harga = total_harga + harga

        daftar_barang = daftar_barang + str(nomor) + ". " + nama_barang + " - Rp " + str(harga) + "\n"

        nomor = nomor + 1 

    print("=" * 40)
    print("=== STRUK PEMBELIAN INDOMEI ===")
    print("=" * 40)
    print("Nama Pembeli : ", nama)
    print("-" * 40)
    print("Daftar Barang :")
    print(daftar_barang, end="")
    print("-" * 40)
    print("Total Harga  : Rp", total_harga)
    print("=" * 40)
    print("Terimakasih telah berbelanja di IndoMei.")
    print("=" * 40)

    lanjut = input("Apakah ada pembeli berikutnya? (y/n) : ")

    if lanjut == "n":
        print("Program selesai. Terimakasih.")
        break