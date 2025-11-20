print("\nPROGRAM MANAJEMEN INVENTARIS GUDANG BERBASIS CRUD (CREATE, READ, UPDATE, DELETE)\n")

inventaris = {
    "1": ["Monitor", 1500000, 10],
    "2": ["Keyboard", 250000, 25],
    "3": ["Mouse", 150000, 40]
}

while True:
    print("MENU UTAMA PROGRAM INVENTARIS GUDANG")
    print("1. Tampilkan Semua Barang (Read)")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru (Create)")
    print("4. Perbarui Stok Barang (Update)")
    print("5. Hapus Barang (Delete)")
    print("6. Selesai, Keluar dari Program")

    pilihan = input("\nSilakan pilih menu (Hanya di Nomor 1-6): ")

    try:
        pilihan = int(pilihan)
        if pilihan < 1 or pilihan > 6:
            print("Input tidak valid! Silakan pilih menu nomor 1 hingga 6.\n")
            continue
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka, bukan huruf atau simbol.\nSilakan coba lagi.\n")
        continue

    if pilihan == 1:
        print("\nTAMPILKAN SEMUA BARANG")
        if len(inventaris) == 0:
            print("Belum ada data barang yang tersimpan.\n")
        else:
            for id_barang, info in inventaris.items():
                print("ID:", id_barang, "| Nama Barang:", info[0], "| Harga:", info[1], "| Stok:", info[2])
            print()

    elif pilihan == 2:
        print("\nCARI BARANG BERDASARKAN ID")
        while True:
            id_cari = input("Masukkan ID barang: ")
            if id_cari == "":
                print("Input tidak valid! ID tidak boleh kosong. Silakan ulangi.")
                continue
            if id_cari.isdigit() == False:
                print("Input tidak valid! ID hanya boleh berisi angka. Silakan ulangi.")
                continue
            if id_cari not in inventaris:
                print("Barang tidak ditemukan. Silakan masukkan ID yang sesuai.\n")
                continue

            print("Barang ditemukan!")
            print("Nama Barang:", inventaris[id_cari][0])
            print("Harga:", inventaris[id_cari][1])
            print("Stok:", inventaris[id_cari][2])
            print()
            break

    elif pilihan == 3:
        print("\nTAMBAH BARANG BARU")
        while True:
            id_baru = input("Masukkan ID barang baru: ")
            if id_baru == "":
                print("Input tidak valid! ID tidak boleh kosong. Silakan ulangi.")
                continue
            if id_baru.isdigit() == False:
                print("Input tidak valid! ID hanya boleh berisi angka. Silakan ulangi.")
                continue

            id_baru_int = int(id_baru)
            if id_baru_int < 1:
                print("Input tidak valid! ID barang harus dimulai dari angka 1 atau lebih. Silakan ulangi.")
                continue

            if str(id_baru_int) in inventaris:
                print("ID sudah terdaftar. Gunakan ID lain.")
                continue

            id_baru = str(id_baru_int)
            break

        while True:
            nama_baru = input("Masukkan nama barang baru: ")
            if nama_baru == "":
                print("Input tidak valid! Nama barang tidak boleh kosong. Silakan ulangi.")
                continue
            if nama_baru.replace(" ", "").isalpha() == False:
                print("Input tidak valid! Nama barang hanya boleh berisi huruf dan spasi. Silakan ulangi.")
                continue
            nama_sudah_ada = False
            for data in inventaris.values():
                if data[0].lower() == nama_baru.lower():
                    nama_sudah_ada = True
                    break
            if nama_sudah_ada:
                print("Nama barang sudah terdaftar! Gunakan nama barang yang lain.")
                continue
            break

        while True:
            harga_baru = input("Masukkan harga barang: ")
            try:
                harga_baru = int(harga_baru)
                if harga_baru <= 0:
                    print("Input tidak valid! Harga harus lebih dari 0. Silakan ulangi.")
                    continue
                break
            except:
                print("Input tidak valid! Harga hanya boleh berupa angka. Silakan ulangi.")

        while True:
            stok_baru = input("Masukkan stok awal barang: ")
            try:
                stok_baru = int(stok_baru)
                if stok_baru < 0:
                    print("Input tidak valid! Stok tidak boleh bernilai negatif. Silakan ulangi.")
                    continue
                break
            except:
                print("Input tidak valid! Stok hanya boleh berupa angka. Silakan ulangi.")

        inventaris[id_baru] = [nama_baru, harga_baru, stok_baru]
        print("Barang berhasil ditambahkan!\n")

    elif pilihan == 4:
        print("\nPERBARUI STOK BARANG")
        while True:
            id_update = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
            if id_update == "":
                print("Input tidak valid! ID tidak boleh kosong. Silakan ulangi.")
                continue
            if id_update.isdigit() == False:
                print("Input tidak valid! ID hanya boleh berisi angka. Silakan ulangi.")
                continue
            if id_update not in inventaris:
                print("Barang tidak ditemukan. Silakan masukkan ID yang sesuai.\n")
                continue
            break

        while True:
            stok_baru = input("Masukkan jumlah perubahan stok (contoh: +5 atau -3): ")
            try:
                if stok_baru == "":
                    print("Input tidak valid! Tidak boleh kosong. Silakan ulangi.")
                    continue
                if not (stok_baru.startswith("+") or stok_baru.startswith("-")):
                    print("Input tidak valid! Gunakan angka dan operator '+' untuk menambah atau '-' untuk mengurangi.")
                    continue
                if stok_baru == "+0" or stok_baru == "-0":
                    print("Input tidak valid! Tidak ada perubahan stok. Silakan masukkan nilai selain 0.")
                    continue
                stok_baru = int(stok_baru)
                if inventaris[id_update][2] + stok_baru < 0:
                    print("Stok tidak boleh menjadi negatif. Silakan ulangi.")
                    continue
                break
            except:
                print("Input tidak valid! Stok harus berupa angka positif atau negatif, tanpa spasi. Silakan ulangi.")

        inventaris[id_update][2] = inventaris[id_update][2] + stok_baru
        print("Stok barang berhasil diperbarui!\n")

    elif pilihan == 5:
        print("\nHAPUS BARANG")
        while True:
            while True:
                id_hapus = input("Masukkan ID barang yang ingin dihapus: ")
                if id_hapus == "":
                    print("Input tidak valid! ID tidak boleh kosong. Silakan ulangi.")
                    continue
                if id_hapus.isdigit() == False:
                    print("Input tidak valid! ID hanya boleh berisi angka. Silakan ulangi.")
                    continue
                break

            if id_hapus in inventaris:
                del inventaris[id_hapus]
                print("Barang berhasil dihapus!\n")
                break
            else:
                print("Barang tidak ditemukan.\n")
                continue

        data_baru = {}
        nomor_baru = 1
        for nilai in inventaris.values():
            data_baru[str(nomor_baru)] = nilai
            nomor_baru = nomor_baru + 1
        inventaris.clear()
        inventaris.update(data_baru)
        print("ID barang telah diperbarui dan dimulai kembali dari 1.\n")

    elif pilihan == 6:
        print("\nSELESAI, KELUAR DARI PROGRAM")
        print("Terima kasih! Program Inventaris Gudang telah selesai dijalankan.\n")
        break