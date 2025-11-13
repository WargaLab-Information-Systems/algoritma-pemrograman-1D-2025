def hitung_total(data):
    total = 0
    for angka in data:
        total += angka
    return total

def cekpembagian(data):
    if not data:
        print("Daftar angka masih kosong.")
    else:
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
    angka = input("Masukkan angka (bisa lebih dari 1, pisahkan dengan spasi): ")
    angka = angka.replace(",", " ").split()
    for a in angka:
        if a.isdigit():
            data.append(int(a))
        else:
            print(a, "bukan angka, di-skip.")
def ubah_data(data):
    if not data:
        print("Daftar angka masih kosong.")
    else:
        tampilkan_data(data)
        try:
            indeks = int(input("Masukkan indeks angka yang ingin diubah: "))
            if 0 <= indeks < len(data):
                angka_baru = int(input("Masukkan angka baru: "))
                data[indeks] = angka_baru
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak ditemukan.")
        except ValueError:
            print("Input tidak valid!")

def hapus_data(data):
    if not data:
        print("Daftar angka masih kosong.")
    else:
        tampilkan_data(data)
        try:
            indeks = int(input("Masukkan indeks angka yang ingin dihapus: "))
            if 0 <= indeks < len(data):
                data.pop(indeks)
                print("Data berhasil dihapus.")

        except ValueError:
            print("Input tidak valid!")

def menu():
    data = []
    while True:
        print("\nPROGRAM")
        print("1. Tambah")
        print("2. Tampilkan")
        print("3. Ubah")
        print("4. Hapus")
        print("5. Cek apakah bisa dibagi dua bagian dengan jumlah sama")
        print()
        print("0. Keluar")

        pilihan = input("Pilih menu:  ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            tampilkan_data(data)
        elif pilihan == "3":
            ubah_data(data)
        elif pilihan == "4":
            hapus_data(data)
        elif pilihan == "5":
            if not data:
                print("Daftar angka masih kosong.")
            else:
                tampilkan_data(data)
                if cekpembagian(data):
                    print("Deretan dapat dibagi menjadi dua bagian dengan jumlah yang sama ")
                else:
                    print("Deretan tidak dapat dibagi menjadi dua bagian dengan jumlah yang sama")
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak tersediqa")

menu()