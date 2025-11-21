def manajemen_inventaris():
    inventaris = {}
    id = 1
    while True:
        print("=== MANAJEMEN INVENTARIS GUDANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang berdasarkan ID")
        print("3. Tambah Barang Baru")
        print("4. Perbarui Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")
  
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            if not inventaris:
                print("\nGudang kosong! Tidak ada barang.")
            else:
                print(f"\n{'DAFTAR BARANG DI GUDANG':^60}")
                print("-" * 80)
                print(f"{'ID':<8} {'Nama':<20} {'Harga (Rp)':<15} {'Stok':<8}")
                print("-" * 80)
                for item_id, info in inventaris.items():
                    nama, harga, stok = info
                    print(f"{item_id:<8} {nama:<20} {harga:<15,} {stok:<8}")
                print("-" * 80)

        elif pilihan == '2':
            item_id = input("\nMasukkan ID barang: ").strip()
            if item_id in inventaris:
                nama, harga, stok = inventaris[item_id]
                print(f"\nBarang ditemukan:")
                print(f"ID     : {item_id}")
                print(f"Nama   : {nama}")
                print(f"Harga  : Rp {harga:,}")
                print(f"Stok   : {stok} unit")
            else:
                print(f"\nBarang dengan ID '{item_id}' tidak ditemukan.")

        elif pilihan == '3':
            item_id = 1
            if item_id in inventaris:
                print(f"ID '{item_id}' sudah digunakan! Gunakan ID lain.")
            else:
                nama = input("Masukkan nama barang: ").strip()
                if not nama:
                    print("Nama tidak boleh kosong!")
                    continue

                try:
                    harga = int(input("Masukkan harga per unit (Rp): ").strip())
                    if harga < 0:
                        print("Harga tidak boleh negatif!")
                        continue
                except ValueError:
                    print("Harga harus berupa angka!")
                    continue

                try:
                    stok = int(input("Masukkan jumlah stok awal: ").strip())
                    if stok < 0:
                        print("Stok tidak boleh negatif!")
                        continue
                except ValueError:
                    print("Stok harus berupa angka!")
                    continue

                inventaris[item_id] = [nama, harga, stok]
                print(f"Barang '{nama}' (ID: {id}) berhasil ditambahkan!")
                item_id += 1

        elif pilihan == '4':
            item_id = input("\nMasukkan ID barang yang akan diperbarui stoknya: ").strip()
            if item_id not in inventaris:
                print(f"Barang dengan ID '{item_id}' tidak ditemukan.")
            else:
                print(f"Stok saat ini: {inventaris[item_id][2]} unit")
                try:
                    perubahan = int(input("Masukkan perubahan stok (+ untuk tambah, - untuk kurangi): ").strip())
                    stok_lama = inventaris[item_id][2]
                    stok_baru = stok_lama + perubahan

                    if stok_baru < 0:
                        print(f"Stok tidak boleh negatif! Stok tetap: {stok_lama} unit.")
                    else:
                        inventaris[item_id][2] = stok_baru
                        print(f"Stok berhasil diperbarui: {stok_lama} → {stok_baru} unit")
                except ValueError:
                    print("Perubahan stok harus berupa angka!")

        elif pilihan == '5':
            item_id = input("\nMasukkan ID barang yang akan dihapus: ").strip()
            if item_id not in inventaris:
                print(f"Barang dengan ID '{item_id}' tidak ditemukan.")
            else:
                nama_barang = inventaris[item_id][0]

manajemen_inventaris()