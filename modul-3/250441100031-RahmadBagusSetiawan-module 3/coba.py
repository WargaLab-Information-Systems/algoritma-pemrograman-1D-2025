# Program Struk Pembelian Sederhana IndoMei (Versi Pemula)

ulang = "y"

while ulang == "y":
    print("=== STRUK PEMBELIAN INDOMEI ===")
    nama = input("Masukkan nama pembeli: ")

    # input barang dan harga
    barang1 = input("Masukkan nama barang 1: ")
    harga1 = int(input("Masukkan harga barang 1: "))

    barang2 = input("Masukkan nama barang 2: ")
    harga2 = int(input("Masukkan harga barang 2: "))

    barang3 = input("Masukkan nama barang 3: ")
    harga3 = int(input("Masukkan harga barang 3: "))

    total = harga1 + harga2 + harga3

    print("\n===== STRUK PEMBELIAN =====")
    print("Nama Pembeli:", nama)
    print("----------------------------")
    print(barang1, "Rp", harga1)
    print(barang2, "Rp", harga2)
    print(barang3, "Rp", harga3)
    print("----------------------------")
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!")
    print("============================\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")

print("\nProgram selesai. Semua transaksi telah dicatat.")
