while True:
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    # deteksi kemungkinan typo umum
    if '0' in nama or '1' in nama or '2' in nama or '3' in nama or '4' in nama or '5' in nama or '6' in nama or '7' in nama or '8' in nama or '9' in nama:
        print("Peringatan: Nama pembeli mengandung angka, kemungkinan typo.")
    elif nama.isupper():
        print("Catatan: Nama pembeli semuanya huruf besar.")
    elif nama.islower():
        print("Catatan: Nama pembeli semuanya huruf kecil.")
    else:
        print("Nama pembeli terdeteksi normal.\n")  

    daftar_barang = []  
    total_harga = 0 

    for i in range(jumlah_barang):
        print(f"\nBarang ke-{i+1}")
        nama_barang = input("Nama barang: ")

        # deteksi typo pada nama barang
        if any(angka in nama_barang for angka in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '/', '\\']):
            print("Peringatan: Nama barang mengandung simbol aneh, kemungkinan typo.")
        elif nama_barang.strip() == "":
            print("Peringatan: Nama barang kosong, kemungkinan salah input.")
        elif nama_barang.isupper():
            print("Catatan: Nama barang semuanya huruf besar.")
        else:
            print("Nama barang terdeteksi normal.\n")

        harga = int(input("Harga barang (Rp): "))
        daftar_barang.append((nama_barang, harga))
        total_harga += harga

    print("\n===== STRUK PEMBELIAN =====")
    print(f"Nama Pembeli : {nama}")
    print("-----------------------------") 

    for barang, harga in daftar_barang:
        print(f"{barang:25 s} Rp{harga:,}")
    print("-----------------------------")
    print(f"Total Harga   : Rp{total_harga:,}")
    print("-----------------------------")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("=============================\n")

