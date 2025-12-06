inventaris = {"_counter": 1}


def buat_id_otomatis():
    id_baru = f"B{inventaris['_counter']:03d}"
    inventaris["_counter"] += 1
    return id_baru


def input_non_kosong(pesan):
    while True:
        data = input(pesan).strip()
        if data == "":
            print("Input tidak boleh kosong!")
        else:
            return data


def input_nama_huruf(pesan):
    while True:
        nama = input_non_kosong(pesan)

        if nama.replace(" ", "").isalpha():
            return nama
        else:
            print("Nama barang hanya boleh berisi huruf dan spasi!")


def input_angka(pesan, boleh_nol=True):
    while True:
        try:
            angka = int(input(pesan))

            if not boleh_nol and angka <= 0:
                print("Angka harus lebih dari 0!")
                continue

            if angka < 0:
                print("Angka tidak boleh negatif!")
                continue

            return angka

        except ValueError:
            print("Input harus berupa angka!")


def input_perubahan_stok(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")


def tampilkan_barang():
    barang_ada = False

    for idb, data in inventaris.items():
        if idb.startswith("_"):  # abaikan _counter
            continue

        barang_ada = True
        print(f"ID: {idb}, Nama: {data['nama']}, Harga: {data['harga']}, Stok: {data['stok']}")

    if not barang_ada:
        print("Belum ada barang.")


def cari_barang():
    idb = input_non_kosong("Masukkan ID barang: ")
    if idb in inventaris and not idb.startswith("_"):
        data = inventaris[idb]
        print(f"Nama: {data['nama']}, Harga: {data['harga']}, Stok: {data['stok']}")
    else:
        print("Barang tidak ditemukan.")


def tambah_barang():
    idb = buat_id_otomatis()
    print(f"ID Barang: {idb}")

    nama = input_nama_huruf("Nama Barang: ")
    harga = input_angka("Harga: ", boleh_nol=False)
    stok = input_angka("Stok: ", boleh_nol=True)

    inventaris[idb] = {"nama": nama, "harga": harga, "stok": stok}
    print("Barang berhasil ditambahkan.")


def update_stok():
    idb = input_non_kosong("Masukkan ID barang: ")
    if idb in inventaris and not idb.startswith("_"):
        tambahan = input_perubahan_stok("Perubahan stok (+/-): ")

        if inventaris[idb]["stok"] + tambahan < 0:
            print("Gagal! Stok tidak boleh negatif.")
        else:
            inventaris[idb]["stok"] += tambahan
            print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")


def hapus_barang():
    idb = input_non_kosong("Masukkan ID barang yang ingin dihapus: ")
    if idb in inventaris and not idb.startswith("_"):
        del inventaris[idb]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")


def menu_inventaris():
    while True:
        print("\n=== INVENTARIS GUDANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok")
        print("5. Hapus barang")
        print("0. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            tampilkan_barang()
        elif pilihan == 2:
            cari_barang()
        elif pilihan == 3:
            tambah_barang()
        elif pilihan == 4:
            update_stok()
        elif pilihan == 5:
            hapus_barang()
        elif pilihan == 0:
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")


menu_inventaris()