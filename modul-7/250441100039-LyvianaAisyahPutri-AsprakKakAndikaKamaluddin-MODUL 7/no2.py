inventaris = {}

def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")
    if len(inventaris) == 0:
        print("Belum ada barang.")
    else:
        for id_brg, data in inventaris.items():
            print(f"ID: {id_brg}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    id_brg = input("Masukkan ID barang: ")

    if id_brg == "":
        print("ID tidak boleh kosong!")
        return
    if not id_brg.isdigit():
        print("ID berupa angka, tidak boleh huruf!")
        return

    if id_brg in inventaris:
        data = inventaris[id_brg]
        print(f"ID: {id_brg}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang():
    id_brg = input("Masukkan ID barang: ")

    if id_brg == "":
        print("ID tidak boleh kosong!")
        return
    if not id_brg.isdigit():
        print("ID harus berupa angka, tidak boleh huruf!")
        return
    if id_brg in inventaris:
        print("ID sudah digunakan!")
        return

    nama = input("Masukkan nama barang: ")
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    if nama.isdigit():
        print("Nama barang tidak boleh hanya angka!")
        return

    harga = input("Masukkan harga barang: ")
    if not harga.isdigit():
        print("Harga harus angka!")
        return
    harga = int(harga)
    if harga < 0:
        print("Harga tidak boleh negatif!")
        return

    stok = input("Masukkan stok barang: ")
    if not stok.isdigit():
        print("Stok harus angka!")
        return
    stok = int(stok)
    if stok < 0:
        print("Stok tidak boleh negatif!")
        return

    inventaris[id_brg] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")

def update_stok():
    id_brg = input("Masukkan ID barang: ")

    if id_brg == "":
        print("ID tidak boleh kosong!")
        return
    if not id_brg.isdigit():
        print("ID harus berupa angka, tidak boleh huruf!")
        return
    if id_brg not in inventaris:
        print("ID tidak ditemukan!")
        return

    perubahan = input("Masukkan perubahan stok : ")
    if not perubahan.lstrip("-").isdigit():
        print("Perubahan stok harus berupa angka!")
        return

    perubahan = int(perubahan)
    stok_baru = inventaris[id_brg][2] + perubahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif!")
        return

    inventaris[id_brg][2] = stok_baru
    print("Stok berhasil diperbarui!")

def hapus_barang():
    id_brg = input("Masukkan ID barang: ")

    if id_brg == "":
        print("ID tidak boleh kosong!")
        return
    if not id_brg.isdigit():
        print("ID harus berupa angka, tidak boleh huruf!")
        return
    if id_brg not in inventaris:
        print("Barang tidak ditemukan!")
        return

    # hapus barang
    del inventaris[id_brg]
    print("Barang berhasil dihapus!")

    id_baru = int(id_brg)   
    while True:
        id_lama = str(id_baru + 1)  

        if id_lama in inventaris:  
            inventaris[str(id_baru)] = inventaris[id_lama]  
            del inventaris[id_lama]
            id_baru += 1
        else:
            break
while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
