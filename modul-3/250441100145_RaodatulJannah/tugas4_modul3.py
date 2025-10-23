ulang = "y"

while ulang.lower() == "y":
    print("\n=====Struk Pembelian IndoMEI=====")

    nama = input("masukkan nama pembeli: ")
    jumlah = int(input("masukkan jumlah barang: "))

    total = 0

    print("\nDaftar Barang:")
    for i in range(jumlah):
        nama_barang = input(f"Nama barang ke-{i+1} :")  
        harga = int(input("harga barang: "))
        total += harga  

    print("\n==============================")
    print("       STRUK PEMBELIAN")
    print("==============================")
    print("Nama Pembeli :", nama)
    print(f"total Harga  : Rp, {total:}")
    print("-------------------------------")
    print("Terima kasih telah berbelanja di IndoMei!")

    ulang = input("\nApakah ada pembeli berikutnya? (y/n):")
print("\nProgram selesai. Sampai jumpa!")
    