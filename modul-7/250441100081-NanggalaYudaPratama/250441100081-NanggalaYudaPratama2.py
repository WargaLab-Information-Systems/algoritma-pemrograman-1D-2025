inventaris = {}

def tampilkan_semua():
    if not inventaris:
        print("Belum ada barang dalam inventaris.")
    else:
        print("\n=== DAFTAR INVENTARIS ===")
        for id_barang, data in inventaris.items():
            print(f"ID: {id_barang}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    if not inventaris:
        print("Belum ada barang tersimpan.")
        lanjut = 2
    input("Apakah ingin lanjut mencari barang? (y/n): ").lower()
    if lanjut != "y":
            print("Kembali ke menu utama")
            return

    id_barang = input("Masukkan ID barang yang dicari: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        nama, harga, stok = inventaris[id_barang]
        print(f"Barang ditemukan: Nama={nama}, Harga={harga}, Stok={stok}")

def tambah_barang():
    while True:
        id_barang = input("Masukkan ID barang baru: ")

        if id_barang in inventaris:
            print("ID ini sudah digunakan. Coba ID lain.")
            continue

        if "id " in id_barang:
            print("ID tidak boleh mengandung spasi!")
            continue

        break

    nama = input("Masukkan nama barang: ")

    while True:
        harga = input("Masukkan harga barang: ")
        if not harga.isdigit():
            print("Harga harus berupa angka!")
            continue
        harga = int(harga)
        break

    while True:
        stok = input("Masukkan jumlah stok: ")
        if not stok.isdigit():
            print("Stok harus berupa angka!")
            continue
        stok = int(stok)
        break

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.")

def update_stok():
    if not inventaris:
        print("Belum ada barang tersimpan.")
        lanjut = input("Apakah ingin lanjut update stok barang? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
        return

    stok_sekarang = inventaris[id_barang][2]
    print(f"Stok saat ini: {stok_sekarang}")

    while True:
        perubahan = input("Masukkan perubahan stok (boleh + atau -): ")
        try:
            perubahan = int(perubahan)
        except ValueError:
            print("Input harus berupa angka (+ atau -)!")
            continue

        stok_baru = stok_sekarang + perubahan

        if stok_baru < 0:
            print("Perubahan ini akan membuat stok negatif! Coba lagi.")
            continue

        break

    inventaris[id_barang][2] = stok_baru
    print(f"Stok berhasil diperbarui menjadi {stok_baru}.")

def hapus_barang():
    if not inventaris:
        print("Belum ada barang tersimpan.")
        lanjut = input("Apakah ingin lanjut menghapus barang? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")

def menu():
    while True:
        print("\n=== INVENTARIS GUDANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

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
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            continue

menu()
