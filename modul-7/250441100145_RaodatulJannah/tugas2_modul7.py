inventaris = {}   

def tampilkan_semua():
    print("\n=== DAFTAR INVENTARIS ===")
    if not inventaris:
        print("Tidak ada data barang.")
    else:
        for ID, data in inventaris.items():
            print(f"ID Barang : {ID}")
            print(f"Nama      : {data[0]}")
            print(f"Harga     : {data[1]}")
            print(f"Stok      : {data[2]}")
            print("----------------------------")

def cari_barang():
    print("\n=== CARI BARANG ===")
    ID = input("Masukkan ID barang: ")

    if ID in inventaris:
        data = inventaris[ID]
        print("Barang ditemukan!")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")

def tambah_barang():
    print("\n=== TAMBAH BARANG ===")
    while True:
      ID = input("Masukkan ID: ")
      if not ID.isdigit():
        print("id harus berupa angka yaaa!!!!!!!")
      else:
        break

    if ID in inventaris:
        print("ID sudah terpakai! Gunakan ID lain.")
        return

    while True:
       nama = input("Nama barang: ")
       if not nama.isalpha():
           print("nama harus berupa huruff!!")
       else:
           break

    while True:
        try:
            harga = float(input("Harga barang: "))
            if harga < 0:
                print("Harga tidak boleh minus!")
                continue
            else:
                break
        except:
                print("angka ya, bukan yang lain")
                break
    

    while True:
        try:
            stok = int(input("Stok barang: "))
            if stok < 0:
                print("Stok tidak boleh minus!")
                continue
            else:
                break
        except:
                print("angka ya, bukan yang lain")
                break
    
    inventaris[ID] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    print("\n=== UPDATE STOK BARANG ===")
    while True:
        ID = input("Masukkan ID barang: ")

        if ID not in inventaris:
            print("Barang tidak ditemukan.")
            continue
        else:
            break
    
    while True:
        stok_input = input("Masukkan stok baru (gunakan + atau -) : ")

        if not (stok_input.startswith("+") or stok_input.startswith("-")):
            print("Input harus diawali dengan + atau -, contoh: +10 atau -5")
            continue
        try:
            stok_baru = int(stok_input)
            break
        except:
            print("Format tidak valid! Gunakan angka setelah + atau -.")

    stok_sekarang = inventaris[ID][2]
    stok_final = stok_sekarang + stok_baru

    if stok_final < 0:
        print("Gagal! Stok tidak boleh negatif.")
        return

    inventaris[ID][2] = stok_final
    print("Stok berhasil diperbarui!")


def hapus_barang():
    print("\n=== HAPUS BARANG ===")
    ID = input("Masukkan ID barang yang ingin dihapus: ")

    if ID in inventaris:
        del inventaris[ID]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan.")


while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang (read)")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru(create)")
    print("4. Update Stok Barang(update)")
    print("5. Hapus Barang (delete)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")