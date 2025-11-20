inventaris = {}
id_barang = 1


def cek_kosong():
    """Cek apakah inventaris kosong. Jika kosong, beri pesan dan return True."""
    if not inventaris:
        print("\n Belum ada barang dalam inventaris. Tambahkan barang terlebih dahulu!")
        return True
    return False


def tampilkan():
    if cek_kosong():  
        return
    print("\n=== DAFTAR INVENTARIS ===")
    for id_brg, data in inventaris.items():
        print(f"ID: {id_brg} || Nama: {data[0]} | Harga: {data[1]} | Stok: {data[2]}")


def cari():
    if cek_kosong():
        return

    id_brg = input("Masukkan ID barang yang dicari: ")
    if not id_brg.isdigit():
        print("ID harus berupa angka!")
        return

    id_brg = int(id_brg)

    if id_brg not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        nama, harga, stok = inventaris[id_brg]
        print(f"Barang ditemukan: Nama={nama}, Harga={harga}, Stok={stok}")


def tambah_barang(id_barang):
    while True:
        nama = input("Masukkan nama barang: ")
        if not nama or not nama[0].isalpha():
            print("Nama barang harus dimulai dengan huruf!")
            continue
        break
    
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
    return id_barang + 1


def update_stok():
    if cek_kosong():
        return

    id_brg = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if not id_brg.isdigit():
        print("ID harus berupa angka!")
        return
    id_brg = int(id_brg)

    if id_brg not in inventaris:
        print("Barang tidak ditemukan.")
        return

    nama = inventaris[id_brg][0]
    stok = inventaris[id_brg][2]
    print(f"Nama barang: {nama} || Stok sekarang: {stok}")

    while True:
        perubahan = input("Masukkan perubahan stok (boleh + atau -): ")
        try:
            perubahan = int(perubahan)
        except ValueError:
            print("Input harus berupa angka (+ atau -)!")
            continue

        stokbaru = stok + perubahan

        if stokbaru < 0:
            print("Stok tidak boleh negatif!")
            continue

        break

    inventaris[id_brg][2] = stokbaru
    print(f"Stok {nama} berhasil diperbarui menjadi {stokbaru}.")


def hapus_barang():
    if cek_kosong():
        return

    id_brg = input("Masukkan ID barang yang ingin dihapus: ")
    if not id_brg.isdigit():
        print("ID harus berupa angka!")
        return

    id_brg = int(id_brg)

    if id_brg not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        del inventaris[id_brg]
        print("Barang berhasil dihapus.")


# === MAIN MENU ===
while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("0. Keluar")

    pilihan = input("Pilih : ")

    if pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        cari()
    elif pilihan == "3":
        id_barang = tambah_barang(id_barang)
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "0":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
