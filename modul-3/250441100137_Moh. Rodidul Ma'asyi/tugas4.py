ulang = "iya"

while ulang.lower() == "iya":
    nama = input("Masukkan nama pembeli: ")

    total = 0
    hitung = "iya"

    while hitung.lower() == "iya":
        barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        total += harga  
        
        hitung = input("Apakah masih ada barang lagi? (sudah/belum): ")

    print("Nama Pembeli:", nama)
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!")

    ulang = input("Apakah ada pembeli berikutnya? (iya/tidak): ")

print("Program selesai. Semua transaksi telah dicatat.")