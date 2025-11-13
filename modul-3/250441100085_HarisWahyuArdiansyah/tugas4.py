while True:
    nama = input("Masukkan nama pembeli: ")
    
    while not nama.replace(" ", "").isalpha():
        print("Nama hanya boleh huruf")
        nama = input("Nama pembeli: ")
    
    barang_list = []
    harga_list = []

    while True:
        barang = input("Masukkan nama barang ('selesai' untuk berhenti): ")
        if barang.lower() == "selesai":
            break
        while barang.isdigit():
            print("Nama barang tidak Terdeteksi")
            barang = input("Nama barang (ketik 'selesai'): ")

        harga = int(input(f"Masukkan harga {barang}: "))
        barang_list.append(barang)
        harga_list.append(harga)
    
    total = sum(harga_list)

    print("\n====== STRUKL PEMBELIAN ======")
    print(f"Nama Pembeli : {nama}")
    print("-----------------------------")
    for i in range(len(barang_list)):
        print(f"{i+1}. {barang_list[i]} \t Rp{harga_list[i]}")
    print("-----------------------------")
    print(f"Total Harga  : Rp{total}")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("=============================\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != "y":
        print("Program selesai")
        break