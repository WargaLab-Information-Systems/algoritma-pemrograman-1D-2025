inventaris = {}

def reset_id():
    new_inventaris = {}
    new_id = 1
    for _, data in inventaris.items():
        new_inventaris[str(new_id)] = data
        new_id += 1
    return new_inventaris

def generate_id():
    return str(len(inventaris) + 1)

def tampil():
    if not inventaris:
        print("\nInventaris masih kosong.\n")
        return

    print("\n=== DATA INVENTARIS ===")
    for item_id, data in inventaris.items():
        print(f"ID    : {item_id}")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}\n")

def cari():
    if not inventaris:
        print("\nInventaris masih kosong.\n")
        return
    
    while True:
        item_id = input("Masukkan ID barang (ketik 'batal'): ")
        if item_id.lower() == "batal":
            print("Pencarian dibatalkan.\n")
            return

        if item_id not in inventaris:
            print("Barang tidak ditemukan.\n")
            continue
        
        data = inventaris[item_id]
        print("\n=== BARANG DITEMUKAN ===")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}\n")
        return

def tambah():
    print("\n=== TAMBAH BARANG ===")

    item_id = generate_id()
    print(f"ID barang: {item_id}")

    while True:
        nama = input("Nama barang (ketik 'batal'): ").strip()
        if nama.lower() == "batal":
            print("Tambah barang dibatalkan.\n")
            return
        if len(nama) < 2:
            print("Nama minimal 2 karakter!\n")
            continue
        break

    while True:
        harga = input("Harga barang (ketik 'batal'): ")
        if harga.lower() == "batal":
            print("Tambah barang dibatalkan.\n")
            return
        if harga.isdigit():
            harga = int(harga)
            if harga == 0:
                print("Harga tidak boleh 0!\n")
                continue
            break
        print("Harga harus berupa angka!\n")

    while True:
        stok = input("Stok barang (ketik 'batal'): ")
        if stok.lower() == "batal":
            print("Tambah barang dibatalkan.\n")
            return
        if stok.isdigit():
            stok = int(stok)
            break
        print("Stok harus berupa angka!\n")

    inventaris[item_id] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!\n")

def update():
    if not inventaris:
        print("\nInventaris masih kosong.\n")
        return

    print("\n=== UPDATE STOK BARANG ===")
    while True:
        item_id = input("Masukkan ID barang (ketik 'batal'): ")
        if item_id.lower() == "batal":
            print("Update stok dibatalkan.\n")
            return

        if item_id not in inventaris:
            print("Barang tidak ditemukan.\n")
            continue
        break

    while True:
        perubahan = input("Masukkan perubahan stok (positif/negatif, ketik 'batal'): ")
        if perubahan.lower() == "batal":
            print("Update stok dibatalkan.\n")
            return

        try:
            perubahan = int(perubahan)
        except:
            print("Input harus berupa angka!\n")
            continue

        stok_baru = inventaris[item_id][2] + perubahan

        if stok_baru < 0:
            print("Stok tidak boleh negatif!\n")
            continue

        inventaris[item_id][2] = stok_baru
        print("Stok berhasil diperbarui!\n")
        return

def hapus():
    global inventaris
    
    if not inventaris:
        print("\nInventaris masih kosong.\n")
        return

    print("\n=== HAPUS BARANG ===")
    while True:
        item_id = input("Masukkan ID barang (ketik 'batal'): ")
        if item_id.lower() == "batal":
            print("Hapus barang dibatalkan.\n")
            return

        if item_id not in inventaris:
            print("Barang tidak ditemukan.\n")
            continue

        while True:
            yakin = input(f"Yakin ingin menghapus barang '{inventaris[item_id][0]}'? (y/n): ").lower()

            if yakin == "y":
                del inventaris[item_id]
                inventaris = reset_id() 
                print("Barang berhasil dihapus & ID disusun ulang!\n")
                return

            elif yakin == "n":
                print("Penghapusan dibatalkan.\n")
                return
            else:
                print("Masukkan hanya 'y' atau 'n'!\n")

while True:
    print("===== MENU INVENTARIS GUDANG =====")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update Stok barang")
    print("5. Hapus barang")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        tampil()
    elif menu == "2":
        cari()
    elif menu == "3":
        tambah()
    elif menu == "4":
        update()
    elif menu == "5":
        hapus()
    elif menu == "0":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")