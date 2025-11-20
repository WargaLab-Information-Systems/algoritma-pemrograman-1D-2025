inventaris = {}

def input_angka(pesan, tipe=int):
    while True:
        try:
            nilai = tipe(input(pesan))
            return nilai
        except:
            print("Input harus berupa angka!")


def tambah_barang():
    print("\n=== TAMBAH BARANG ===")

    id_barang = str(len(inventaris) + 1)

    while True:
        nama = input("Masukkan nama barang: ").strip()
        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        if not nama.replace(" ", "").isalpha():
            print("Nama hanya boleh berisi huruf!")
            continue
        break

    while True:
        harga = input_angka("Masukkan harga barang: ", float)
        if harga < 0:
            print("Harga tidak boleh negatif!")
            continue
        break

    while True:
        stok = input_angka("Masukkan jumlah stok: ", int)
        if stok < 0:
            print("Stok tidak boleh negatif!")
            continue
        break

    inventaris[id_barang] = [nama, harga, stok]
    print(f"Barang berhasil ditambahkan dengan ID {id_barang}!")


def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")
    if not inventaris:
        print("Belum ada barang.")
        return

    for idb, data in inventaris.items():
        print(f"ID   : {idb}")
        print(f"Nama : {data[0]}")
        print(f"Harga: {data[1]}")
        print(f"Stok : {data[2]}\n")


def cari_barang():
    print("\n=== CARI BARANG ===")
    idb = input("Masukkan ID barang: ").strip()

    if idb in inventaris:
        data = inventaris[idb]
        print("\nBarang ditemukan:")
        print(f"ID   : {idb}")
        print(f"Nama : {data[0]}")
        print(f"Harga: {data[1]}")
        print(f"Stok : {data[2]}\n")
    else:
        print("Barang tidak ditemukan.")


def perbarui_stok():
    print("\n=== PERBARUI STOK ===")
    idb = input("Masukkan ID barang: ").strip()

    if idb not in inventaris:
        print("Barang tidak ditemukan!\n")
        return

    print(f"Stok sekarang: {inventaris[idb][2]}")

    while True:
        perubahan = input_angka("Masukkan perubahan stok (+ atau -): ", int)

        if inventaris[idb][2] + perubahan < 0:
            print("Stok tidak boleh menjadi negatif!\n")
            continue

        inventaris[idb][2] += perubahan
        print("Stok berhasil diperbarui!\n")
        break


def hapus_barang():
    print("\n=== HAPUS BARANG ===")

    idb = input("Masukkan ID barang: ").strip()

    if idb not in inventaris:
        print("Barang tidak ditemukan!")
        return

    del inventaris[idb]
    print("Barang berhasil dihapus!")

    if inventaris:   
        inventaris_baru = {}
        id_baru = 1

        for data in inventaris.values():
            inventaris_baru[str(id_baru)] = data
            id_baru += 1

        inventaris.clear()
        inventaris.update(inventaris_baru)
        print("ID berhasil dirapikan ulang!")
    else:
        print("Inventaris kosong, ID tidak perlu dirapikan.")

while True:
    print("\n=== PROGRAM INVENTARIS GUDANG ===")
    print("1. Tambah barang (create)")
    print("2. Tampilkan barang (read)")
    print("3. Cari barang")
    print("4. Perbarui stok (update)")
    print("5. Hapus barang (delete)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        cari_barang()
    elif pilihan == "4":
        perbarui_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid!\n")
