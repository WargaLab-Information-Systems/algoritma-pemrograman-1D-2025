ulang = "y"

while ulang.lower() == "y":
    print("=== STRUK PEMBELIAN INDOMEI ===")
    nama = input("Masukkan nama pembeli: ")

    total = 0
    hitung = "a"

    while hitung.lower() == "a":
        barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        total += harga  
        hitung = input("Apakah masih ada barang lagi? (a/n): ")

    print("===== STRUK PEMBELIAN =====")
    print("Nama Pembeli:", nama)
    print("----------------------------")
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!")
    print("============================")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")

print("Program selesai. Semua transaksi telah dicatat.")