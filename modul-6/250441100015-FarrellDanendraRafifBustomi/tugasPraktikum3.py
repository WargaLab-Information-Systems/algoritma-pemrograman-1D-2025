def create(data):
    while True:
        try:
            n_input = input("Masukkan jumlah angka (atau ketik 'batal' untuk kembali): ")
            if n_input.lower() == "batal":
                print("Input dibatalkan. Kembali ke menu utama.\n")
                return
            n = int(n_input)
            if n <= 0:
                print("Jumlah angka harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka bulat.")
    
    for i in range(n):
        while True:
            angka_input = input(f"Angka ke-{i+1} (atau ketik 'batal' untuk membatalkan seluruh input): ")
            if angka_input.lower() == "batal":
                print("Input dibatalkan. Tidak ada data yang disimpan.\n")
                return
            try:
                angka = int(angka_input)
                break
            except ValueError:
                print("Input tidak valid! Masukkan angka saja.")

        data.append(angka)
    print("Data berhasil ditambahkan!\n")


def read(data):
    if not data:
        print("Tidak ada data.\n")
    else:
        print("Daftar angka saat ini:", data, "\n")


def update(data):
    read(data)
    if not data:
        return
    
    while True:
        index_input = input("Masukkan indeks yang ingin diubah (atau ketik 'batal' untuk kembali): ")
        if index_input.lower() == "batal":
            print("Update dibatalkan. Kembali ke menu utama.\n")
            return 

        try:
            index = int(index_input)
            if 0 <= index < len(data):
                while True:
                    angka_baru = input("Masukkan angka baru (atau ketik 'batal' untuk kembali): ")
                    if angka_baru.lower() == "batal":
                        print("Perubahan dibatalkan. Kembali ke menu utama.\n")
                        return
                    if not angka_baru.isdigit():
                        print("Input tidak valid! Masukkan angka saja.")
                        continue
                    data[index] = int(angka_baru)
                    print(f"Data pada indeks {index} berhasil diperbarui!\n")
                    break  
                
                while True:
                    lanjut = input("Apakah ingin mengupdate data lain? (y/n): ").lower()
                    if lanjut == "y":
                        read(data)
                        break
                    elif lanjut == "n":
                        print("Kembali ke menu utama.\n")
                        return
                    else:
                        print("Pilihan tidak valid! Ketik 'y' atau 'n'.")
            elif index >= len(data):
                print(f"Indeks hanya sampai {len(data)-1}! Tambahkan data terlebih dahulu.\n")
            else:
                print("Indeks tidak boleh negatif!\n")
        except ValueError:
            print("Input harus berupa angka atau ketik 'batal' untuk kembali!\n")


def delete(data):
    if len(data) == 0:
        print("Tidak ada data untuk dihapus.\n")
        return

    while True:
        index_input = input("Masukkan indeks yang ingin dihapus (atau ketik 'batal' untuk kembali): ")

        if index_input.lower() == "batal":
            print("Penghapusan dibatalkan. Kembali ke menu utama.\n")
            return

        if not index_input.isdigit():
            print("Input tidak valid! Masukkan angka saja atau ketik 'batal' untuk kembali.\n")
            continue

        index = int(index_input)

        if index < 0:
            print("Indeks tidak boleh negatif!\n")
            continue
        elif index >= len(data):
            print(f"Indeks hanya sampai {len(data)-1}! Jika ingin menghapus lebih banyak data, tambahkan dulu datanya.\n")
            continue

        konfirmasi = input(f"Yakin ingin menghapus data indeks {index} ({data[index]})? (y/n): ").lower()
        if konfirmasi == "y":
            del data[index]
            print(f"Data pada indeks {index} berhasil dihapus!\n")
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.\n")
        else:
            print("Pilihan tidak valid! Ketik 'y' atau 'n'.")
            continue

        while True:
            lanjut = input("Apakah ingin menghapus data lain? (y/n): ").lower()
            if lanjut == "y":
                if len(data) == 0:
                    print("Semua data telah dihapus. Kembali ke menu utama.\n")
                    return
                print("Data saat ini:", data)
                break
            elif lanjut == "n":
                print("Kembali ke menu utama.\n")
                return
            else:
                print("Pilihan tidak valid! Ketik 'y' atau 'n'.")


def cek_pembagian_sama(data):
    if not data:
        print("Tidak ada data untuk diperiksa.\n")
        return None

    total = 0
    for i in data:
        total += i  

    kiri = 0
    for i in range(len(data)):
        kiri += data[i]
        kanan = total - kiri
        if kiri == kanan:
            print("Deretan dapat dibagi menjadi dua bagian dengan jumlah sama.")
            print("Bagian kiri :", data[:i+1])
            print("Bagian kanan:", data[i+1:], "\n")
            return True  

    print("Deretan tidak dapat dibagi menjadi dua bagian dengan jumlah sama.\n")
    return False  


data = []

while True:
    print("=== Sistem CRUD  ===")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Cek Pembagian Sama")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        create(data)
    elif pilih == "2":
        read(data)
    elif pilih == "3":
        update(data)
    elif pilih == "4":
        delete(data)
    elif pilih == "5":
        hasil = cek_pembagian_sama(data)
        print("Hasil pembagian sama:", hasil, "\n")
    elif pilih == "6":
        print("Program selesai. Terima kasih!\n")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih antara 1-6.\n")