inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("Belum ada barang.")
    else:
        for idb, data in inventaris.items():
            print(f"ID: {idb}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    idb = input("Masukkan ID barang: ")
    if idb in inventaris:
        nama, harga, stok = inventaris[idb]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")

def generate_id():
    return str(len(inventaris) + 1)

def tambah_barang():
    idb = generate_id()
    print(f"ID baru: {idb}")
    
    nama = input("Nama barang: ").lower()
    
    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        inventaris[idb] = [nama, harga, stok]
        print("Barang berhasil ditambahkan.")
    except:
        print("Harga dan stok harus angka.")

def update_stok():
    idb = input("Masukkan ID barang: ")

    if idb in inventaris:
        try:
            perubahan = int(input("Tambah/Kurang stok (contoh: 5 atau -3): "))

            if inventaris[idb][2] + perubahan < 0:
                print("Stok tidak boleh negatif!")
            else:
                inventaris[idb][2] += perubahan
                print("Stok berhasil diperbarui.")
        except:
            print("Input harus angka.")
    else:
        print("ID barang tidak ditemukan.")

def hapus_barang():
    idb = input("ID barang yang dihapus: ")
    if idb in inventaris:
        del inventaris[idb]
        print("Barang berhasil dihapus.")

        temp = list(inventaris.values()) 
        inventaris.clear()                

        for i, data in enumerate(temp, start=1):
            inventaris[str(i)] = data

        print("ID telah diperbarui")
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok")
    print("5. Hapus barang")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_barang()
    elif pilih == "2":
        cari_barang()
    elif pilih == "3":
        tambah_barang()
    elif pilih == "4":
        update_stok()
    elif pilih == "5":
        hapus_barang()
    elif pilih == "6":
        break
    else:
        print("Menu tidak valid.")
