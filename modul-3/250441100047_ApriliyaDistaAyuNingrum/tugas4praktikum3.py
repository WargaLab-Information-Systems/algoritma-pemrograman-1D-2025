# Program struk indomei
while True:
    nama = input("Nama pembeli: ")
    total = 0
    daftar_barang = ""  
    
    print("Input barang (tekan enter kosong untuk selesai):")
    while True:
        b = input("Barang: ")
        if b == "":
            break
        h = int(input("Harga: "))
        total = total + h
        daftar_barang = daftar_barang + b + ": Rp " + str(h) + "\n" 
    # Struk 
    print("=== STRUK INDOMEI ===")
    print("Pembeli:", nama)
    print("Barang:")
    print(daftar_barang) 
    print("Total: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")
    
    jawab = input("Apakah ada pembeli berikutnya? (y/ya, n/tidak): ")
    if jawab == "y" or jawab == "n":  
        print("Selesai! Selamat tinggal!")