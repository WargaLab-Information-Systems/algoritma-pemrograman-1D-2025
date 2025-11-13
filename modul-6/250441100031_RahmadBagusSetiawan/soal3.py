
def tambah_data(data):
    print("\n=== TAMBAH DATA ===")
    jumlah = int(input("Masukkan jumlah angka yang ingin ditambahkan: "))
    for i in range(jumlah):
        angka = int(input("Masukkan angka ke-" + str(i + 1) + ": "))
        data.append(angka)
    print("Data berhasil ditambahkan!")


def tampil_data(data):
    print("\n=== TAMPIL DATA ===")
    if len(data) == 0:
        print("Belum ada data.")
    else:
        print("Isi data saat ini:", data)


def ubah_data(data):
    print("\n=== UBAH DATA ===")
    if len(data) == 0:
        print("Belum ada data untuk diubah.")
    else:
        tampil_data(data)
        indeks = int(input("Masukkan indeks data yang ingin diubah (mulai dari 0): "))
        if indeks >= 0:
            if indeks < len(data):
                angka_baru = int(input("Masukkan angka baru: "))
                data[indeks] = angka_baru
                print("Data berhasil diubah!")
            else:
                print("Indeks tidak ditemukan!")
        else:
            print("Indeks harus lebih besar atau sama dengan 0.")


def hapus_data(data):
    print("\n=== HAPUS DATA ===")
    if len(data) == 0:
        print("Belum ada data untuk dihapus.")
    else:
        tampil_data(data)
        indeks = int(input("Masukkan indeks data yang ingin dihapus (mulai dari 0): "))
        if indeks >= 0:
            if indeks < len(data):
                data.pop(indeks)
                print("Data berhasil dihapus!")
            else:
                print("Indeks tidak ditemukan!")
        else:
            print("Indeks harus lebih besar atau sama dengan 0.")



def cek_pembagian(data):
    print("\n=== CEK PEMBAGIAN ===")

    if len(data) == 0:
        print("Belum ada data.")
        return


    total = 0
    for angka in data:
        total = total + angka

    if total % 2 != 0:
        print("False -> Tidak bisa dibagi dua bagian sama besar (jumlah ganjil).")
        return


    setengah = total // 2
    jumlah = 0
    print(setengah)

    for angka in data:
        jumlah = jumlah + angka
        if jumlah == setengah:
            print("True -> Bisa dibagi dua bagian dengan jumlah sama.")
            return

    print("False -> Tidak bisa dibagi dua bagian dengan jumlah sama.")



data = []

while True:
    print("\n===== MENU DOMINIC =====")
    print("1. Tambah Data")
    print("2. Tampil Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cek Pembagian Sama Besar")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_data(data)
    elif pilihan == "2":
        tampil_data(data)
    elif pilihan == "3":
        ubah_data(data)
    elif pilihan == "4":
        hapus_data(data)
    elif pilihan == "5":
        cek_pembagian(data)
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")