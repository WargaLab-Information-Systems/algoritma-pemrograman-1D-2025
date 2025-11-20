inventaris = []
kupon = {
    "DISKON10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}

def reset_id():
    for i in range(len(inventaris)):
        inventaris[i]["id"] = i + 1

def tampil():
    if not inventaris:
        print("\nInventaris kosong.\n")
        return

    print("\n=== DATA BARANG ===")
    for item in inventaris:
        print(f"ID    : {item['id']}")
        print(f"Nama  : {item['nama']}")
        print(f"Harga : Rp {item['harga']}")
        print(f"Stok  : {item['stok']}\n")


def tambah():
    print("\n=== TAMBAH BARANG ===")
    nama = input("Nama barang: ").strip()

    while True:
        harga = input("Harga barang: ")
        if harga.isdigit(harga)() and int(harga) > 0:
            harga = int
            break
        print("Harga harus angka dan tidak boleh 0!\n")

    while True:
        stok = input("Stok barang: ")
        if stok.isdigit():
            stok = int(stok)
            break
        print("Stok harus angka!\n")

    item = {
        "id": len(inventaris) + 1,
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(item)
    print("Barang berhasil ditambahkan!\n")


def hapus():
    if not inventaris:
        print("\nInventaris kosong.\n")
        return
    
    tampil()
    try:
        hapus = int(input("Masukkan ID barang yang ingin dihapus: "))
    except:
        print("Input harus angka!\n")
        return

    for item in inventaris:
        if item["id"] == hapus:
            inventaris.remove(item)
            reset_id()
            print("Barang berhasil dihapus!\n")
            return

    print("ID tidak ditemukan!\n")


def update_stock():
    if not inventaris:
        print("\nInventaris kosong.\n")
        return
    
    tampil()
    try:
        item_id = int(input("Masukkan ID barang: "))
    except:
        print("Input harus angka!")
        return

    for item in inventaris:
        if item["id"] == item_id:
            try:
                perubahan = int(input("Masukkan perubahan stok (+/-): "))
            except:
                print("Input harus angka!")
                return

            if item["stok"] + perubahan < 0:
                print("Stok tidak boleh negatif!\n")
                return
            
            item["stok"] += perubahan
            print("Stok berhasil diperbarui!\n")
            return

    print("ID tidak ditemukan!\n")

def tampil_kupon():
    if not kupon:
        print("\nTidak ada kupon tersedia.\n")
        return
    print("\n=== KUPON TERSEDIA ===")
    for kode, diskon in kupon.items():
        print(f"{kode} - {diskon}%")
    print()

def proses_transaksi():
    if not inventaris:
        print("\nInventaris kosong! Tidak bisa transaksi.\n")
        return

    keranjang = []
    total = 0

    print("\n=== BELANJA ===")
    tampil()

    while True:
        pilih = input("Masukkan ID barang (ketik 'selesai'): ")

        if pilih.lower() == "selesai":
            break

        if not pilih.isdigit():
            print("ID harus angka!\n")
            continue

        pilih = int(pilih)
        barang = None

        for item in inventaris:
            if item["id"] == pilih:
                barang = item
                break

        if barang is None:
            print("ID tidak ditemukan!\n")
            continue

        jumlah = input(f"Jumlah beli ({barang['nama']}): ")

        if not jumlah.isdigit():
            print("Jumlah harus angka!\n")
            continue

        jumlah = int(jumlah)

        if jumlah > barang["stok"]:
            print("Stok tidak cukup!\n")
            continue

        subtotal = barang["harga"] * jumlah
        total += subtotal
        keranjang.append((barang["nama"], barang["harga"], jumlah, subtotal))

        barang["stok"] -= jumlah
        print("Ditambahkan ke keranjang!\n")

    print("\n=== RINGKASAN BELANJA ===")
    for nama, harga, qty, sub in keranjang:
        print(f"{nama} x{qty} = Rp {sub}")

    print(f"\nTOTAL = Rp {total}")

    kode = input("\nMasukkan kode kupon (ketik 'tidak' jika tidak memakai): ").upper()

    total_diskon = 0

    if kode.lower() == "tidak":
        print("Tidak menggunakan kupon.\n")

    elif kode not in kupon:
        print("Kupon tidak valid / sudah digunakan!\n")

    else:
        diskon = kupon[kode]
        total_diskon = total * diskon / 100
        print(f"Kupon valid! Diskon {diskon}% = Rp {total_diskon:.2f}")

        del kupon[kode]    
        print("Kupon sudah digunakan dan dihapus dari daftar.\n")

    total_bayar = total - total_diskon

    print(f"\nTOTAL DISKON : Rp {total_diskon:.2f}")
    print(f"TOTAL BAYAR  : Rp {total_bayar:.2f}")

    while True:
        try:
            bayar = float(input("Uang pelanggan: Rp "))
            if bayar < total_bayar:
                print("Uang tidak cukup!\n")
                continue
            break
        except:
            print("Harus angka!\n")

    kembalian = bayar - total_bayar
    print(f"KEMBALIAN : Rp {kembalian:.2f}\n")

while True:
    print("===== MENU KASIR =====")
    print("1. Tampilkan barang")
    print("2. Tambah barang")
    print("3. Hapus barang")
    print("4. Update stok")
    print("5. Tampilkan kupon")
    print("6. Proses transaksi")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1": tampil()
    elif menu == "2": tambah()
    elif menu == "3": hapus()
    elif menu == "4": update_stock()
    elif menu == "5": tampil_kupon()
    elif menu == "6": proses_transaksi()
    elif menu == "0":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid!\n")