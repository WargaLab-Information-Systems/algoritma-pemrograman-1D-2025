def hitung_total(data):
    total = 0
    for angka in data:
        total += angka
    return total

def cekpembagian(data):
    total = hitung_total(data)
    setengah = total / 2
    temp = 0

    for i in range(len(data)):
        temp += data[i]
        if temp == setengah:
            return True
    return False

def tampilkan_data(data):
    if not data:
        print("Daftar angka masih kosong.")
    else:
        print("Daftar angka saat ini:", data)

def tambah_data(data):
    try:
        angka = input("Masukkan angka (bisa lebih dari 1, pisahkan dengan spasi): ")
        angka = angka.replace(",", " ").split()
        for a in angka:
            if a.isdigit():
                data.append(int(a))
                print(f"Angka {a} berhasil ditambahkan.")
            else:
                print(f"'{a}' bukan angka, di-skip.")
    except ValueError:
        print("Input tidak valid!")

def ubah_data(data):
    tampilkan_data(data)
    if not data:
        return
        
    try:
        indeks = int(input("Masukkan indeks angka yang ingin diubah: "))
        if 0 <= indeks < len(data):
            angka_baru = input("Masukkan angka baru: ")
            if angka_baru.isdigit():
                data[indeks] = int(angka_baru)
                print("Data berhasil diubah.")
            else:
                print("Input harus berupa angka!")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def hapus_data(data):
    tampilkan_data(data)
    if not data:
        return
        
    try:
        indeks = int(input("Masukkan indeks angka yang ingin dihapus: "))
        if 0 <= indeks < len(data):
            data.pop(indeks)
            print("Data berhasil dihapus.")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def menu():
    data = []
    while True:
        print("\n=== PROGRAM ===")
        print("1. Tambah Angka")
        print("2. Tampilkan Angka")
        print("3. Ubah Angka")
        print("4. Hapus Angka")
        print("5. Cek Pembagian Dua Bagian Sama Besar")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            tampilkan_data(data)
        elif pilihan == "3":
            ubah_data(data)
        elif pilihan == "4":
            hapus_data(data)
        elif pilihan == "5":
            tampilkan_data(data)
            if cekpembagian(data):
                print("Deretan dapat dibagi menjadi dua bagian dengan jumlah yang sama")
            else:
                print("Deretan tidak dapat dibagi menjadi dua bagian dengan jumlah yang sama")
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            breakh
        else:
            print("Pilihan tidak tersedia")

menu()