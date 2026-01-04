inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("\nBelum ada data barang.")
        return

    print("\n=== Daftar Semua Barang ===")
    for id_barang, data in inventaris.items():
        print(f"ID    : {id_barang}")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}")
        print("---------------------------")
    print()


def merapikan_id():
    data_baru = {}
    id_baru = 1
    for data in inventaris.values():
        data_baru[str(id_baru)] = data

        id_baru += 1
    inventaris.clear()
    inventaris.update(data_baru)


def cari_barang():
    id_barang = input("Masukkan ID barang yang ingin dicari: ")

    if id_barang in inventaris:
        data = inventaris[id_barang]
        print("\nBarang ditemukan:")
        print(f"Nama  : {data[0]}")
        print(f"Harga : {data[1]}")
        print(f"Stok  : {data[2]}\n")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.\n")


def tambah_barang():
    id_baru = str(len(inventaris) + 1)

    while True:
        try:
            nama = input("Masukkan nama: ")

            if all(char == " " for char in nama):
                print("Nama tidak boleh kosong")
                continue

            if not all(char.isalpha() or char == " " for char in nama):
                print("Nama harus berupa huruf")
                continue

            break

        except ValueError:
            print("Inputan tidak valid!")

    while True:
        try:
            harga = int(input("Masukkan harga barang: "))

            if harga <= 0:
                print("Harga harus angka positif!")
                continue

            break
        except ValueError:
            print("Input harga harus berupa angka!")
            continue

    while True:
        try:
            stok = int(input("Masukkan jumlah stok: "))

            if stok < 0:
                print("Stok tidak boleh negatif!")
                continue

            break
        except ValueError:
            print("Input stok harus berupa angka!")
            continue

    inventaris[id_baru] = [nama, harga, stok]
    print(f"Barang berhasil ditambahkan dengan ID {id_baru}!\n")


def update_stok():
    while True:
        id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")

        try:
            int(id_barang)  
        except ValueError:
            print("ID harus berupa angka! Coba lagi.\n")
            continue

        if id_barang not in inventaris:
            print("ID barang tidak ditemukan. Coba lagi.\n")
            continue
        
        break 

    while True:
        try:
            perubahan = int(input("Masukkan perubahan stok (+ tambah, - kurangi): "))
            break
        except ValueError:
            print("Input tidak valid. Harus berupa angka.\n")

    stok_sekarang = inventaris[id_barang][2]
    stok_baru = stok_sekarang + perubahan

    if stok_baru < 0:
        print("Error: Stok tidak boleh negatif!\n")
        return

    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui!\n")


def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.\n")
        return

    del inventaris[id_barang]
    merapikan_id()  
    print("Barang berhasil dihapus dan ID diperbarui!\n")


while True:
    print("\n=== MENU INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

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
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid! Silakan masukkan 1-6.\n")