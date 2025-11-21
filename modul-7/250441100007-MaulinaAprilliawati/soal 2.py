inventaris = {}
next_id = 1   

def generate_id():
    global next_id

    while str(next_id) in inventaris:
        next_id += 1
    
    hasil = str(next_id)
    next_id += 1
    return hasil

def tampilkan_semua():
    if not inventaris:
        print("Belum ada data barang.")
        return
    print("\n=== DAFTAR BARANG ===")
    for id_barang, data in inventaris.items():
        print(f"ID    : {id_barang}")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}")
        print("------------------------")

def cari_barang():
    id_barang = input("Masukkan ID barang: ")
    if id_barang in inventaris:
        nama, harga, stok = inventaris[id_barang]
        print("\n=== DATA BARANG ===")
        print(f"Nama  : {nama}")
        print(f"Harga : {harga}")
        print(f"Stok  : {stok}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


def tambah_barang():
    id_barang = generate_id()

    print(f"\nID barang otomatis: {id_barang}")
    nama = input("Masukkan nama barang: ")

    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
    except:
        print("Input tidak valid!")
        return

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    id_barang = input("Masukkan ID barang: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
        return

    try:
        stok_baru = int(input("Masukkan stok baru: "))
    except:
        print("Input tidak valid!")
        return

    if stok_baru < 0:
        print("Stok tidak boleh negatif.")
        return

    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui!")


def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan.")


while True:
    print("\n===== MENU INVENTARIS GUDANG =====")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Hapus barang")
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
        print("bye-bye bubb :>")
        break
    else:
        print("cari yang adaa!")
