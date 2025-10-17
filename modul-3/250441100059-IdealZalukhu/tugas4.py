ulang = "y"

while ulang == "y":
    print("\n=== Kasir IndoMei ===")
    nama = input("Nama pembeli: ")
    total = 0
    daftar = ""  # untuk menampung teks daftar barang

    while True:
        barang = input("Nama barang: ")
        harga = int(input("Harga barang: "))
        daftar += f"{barang} - {harga}\n"  # tambahkan ke teks daftar
        total += harga

        lagi = input("Tambah barang lagi? (y/n): ")
        if lagi != "y":
            break

    print("\n--- Struk Pembelian ---")
    print("Nama Pembeli:", nama)
    print("Daftar Barang:")
    print(daftar, end="")  # tampilkan daftar barang
    print("Total Harga :", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    ulang = input("Ada pembeli berikutnya? (y/n): ")
