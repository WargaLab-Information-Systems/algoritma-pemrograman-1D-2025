kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nBelum ada data kontak.") 
        return

    print("\n=== Daftar Semua Kontak ===")
    for nama, info in kontak.items():
        print(f"- {nama}: Nomor = {info[0]}, Email = {info[1]}")
    print()


def cari_kontak():
    nama = input("Masukkan nama yang ingin dicari: ").capitalize()
    if nama in kontak:
        print(f"Kontak ditemukan!\nNama  : {nama}\nNomor : {kontak[nama][0]}\nEmail : {kontak[nama][1]}\n")
    else:
        print("Kontak tidak ditemukan.\n") 


def tambah_kontak():
    while True:
        try:
            nama = input("Masukkan nama: ")

            if all(char == " " for char in nama):
                print("Nama tidak boleh kosong")
                continue

            if not all(char.isalpha() or char == " " for char in nama):
                print("Nama harus berupa huruf")
                continue

            break

        except ValueError:
            print("Inputan tidak valid!")

    while True:
        nomor = input("Masukkan nomor telepon: ")

        try:
            int(nomor)
        except ValueError:
            print("Nomor telepon hanya boleh berisi angka!")
            continue

        if len(nomor) < 12:
            print("Nomor telepon minimal 12 digit!")
            continue

        if len(nomor) > 13:
            print("Nomor telepon maksimal 13 digit!")
            continue

        semua_nomor = []
        for info in kontak.values():
            semua_nomor.append(info[0])
            
        if nomor in semua_nomor:
            print("Nomor telepon sudah ada!")
            continue

        break

    while True:
        email = input("Masukkan email: ")
        if (
            "@gmail.com" not in email and
            "@yahoo.com" not in email and
            "@outlook.com" not in email and
            "@hotmail.com" not in email
        ):
            print("Email tidak valid!")
            continue

        semua_email = []
        for info in kontak.values():
            semua_email.append(info[1])

        if email in semua_email:
            print("Email sudah ada!")
            continue

        break

    kontak[nama] = [nomor, email]
    print("Kontak berhasil ditambahkan!\n")


def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ").capitalize()

    if nama not in kontak:
        print("Kontak tidak ditemukan.\n")
        return

    while True:
        email_baru = input("Masukkan email baru: ")
        if ("@gmail.com" not in email_baru and
            "@yahoo.com" not in email_baru and
            "@outlook.com" not in email_baru and
            "@hotmail.com" not in email_baru
        ):
            print("Format email tidak valid!")
            continue

        semua_email = []
        for nama_kontak, info in kontak.items():
            if nama_kontak != nama:
                semua_email.append(info[1])
                
        if email_baru in semua_email:
            print("Email sudah digunakan kontak lain!")
            continue

        break

    kontak[nama][1] = email_baru
    print("Email berhasil diperbarui!\n")


def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").capitalize()

    if nama not in kontak:
        print("Kontak tidak ditemukan.\n")
        return

    del kontak[nama]
    print("Kontak berhasil dihapus!\n")


while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak Baru")
    print("4. Update Email")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.\n")