kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("Belum ada kontak tersimpan.")
    else:
        print("\n=== DAFTAR KONTAK ===")
        for nama, data in kontak.items():
            print(f"Nama: {nama}, Nomor: {data[0]}, Email: {data[1]}")

def cari_kontak():
    if not kontak:
        print("Belum ada kontak tersimpan.")
        lanjut = input("Apakah ingin lanjut mencari kontak? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    while True:
        nama = input("Masukkan nama kontak: ")

        if not nama.isalpha():
            print("Nama tidak boleh mengandung angka atau simbol!")
            continue

        if nama in kontak:
            print(f"{nama} ditemukan.")
            print(f"Nomor: {kontak[nama][0]}, Email: {kontak[nama][1]}")
            break
        else:
            print("Kontak tidak ditemukan.")
            lanjut = input("Ingin mencari lagi? (y/n): ").lower()
            if lanjut != "y":
                break

def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak baru: ")

        if nama.replace(" ", "").isdigit():
            print("Nama tidak boleh mengandung angka!")
            continue

        if nama in kontak:
            print("Kontak dengan nama ini sudah ada!")
            continue

        break

    while True:
        nomor = input("Masukkan nomor telepon: ")

        if not nomor.isdigit():
            print("Nomor telepon hanya boleh angka!")
            continue

        if len(nomor) > 12:
            print("Nomor telepon tidak boleh lebih dari 12 digit!")
            continue

        break

    valid_domain = ["@gmail.com", "@yahoo.com"]

    while True:
        email = input("Masukkan email: ")

        if not any(domain in email for domain in valid_domain):
            print("Domain email tidak valid! Gunakan @gmail.com, @yahoo.com")
            continue

        break

    kontak[nama] = [nomor, email]
    print("Kontak berhasil ditambahkan.")

def update_email():
    if not kontak:
        print("Belum ada kontak tersimpan.")
        lanjut = input("Apakah ingin lanjut update email? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    while True:
        nama = input("Masukkan nama kontak yang ingin diupdate emailnya: ")

        if not nama.isalpha():
            print("Nama tidak boleh mengandung angka atau simbol!")
            continue

        if nama not in kontak:
            print("Kontak tidak ditemukan.")
            continue

        break

    valid_domain = ["@gmail.com", "@yahoo.com"]

    while True:
        email_baru = input("Masukkan email baru: ")

        if not any(domain in email_baru for domain in valid_domain):
            print("Domain email tidak valid! Gunakan @gmail.com, @yahoo.com")
            continue

        break

    kontak[nama][1] = email_baru
    print("Email berhasil diperbarui.")

def update_nomor():
    if not kontak:
        print("Belum ada kontak tersimpan.")
        lanjut = input("Apakah ingin lanjut update nomor? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    while True:
        nama = input("Masukkan nama kontak yang ingin diupdate nomornya: ")

        if not nama.isalpha():
            print("Nama tidak boleh mengandung angka atau simbol!")
            continue

        if nama not in kontak:
            print("Kontak tidak ditemukan.")
            continue

        break

    while True:
        nomor_baru = input("Masukkan nomor telepon baru: ")

        if not nomor_baru.isdigit():
            print("Nomor telepon hanya boleh angka!")
            continue

        if len(nomor_baru) > 12:
            print("Nomor telepon tidak boleh lebih dari 12 digit!")
            continue

        break

    kontak[nama][0] = nomor_baru
    print("Nomor telepon berhasil diperbarui.")

def hapus_kontak():
    if not kontak:
        print("Belum ada kontak tersimpan.")
        lanjut = input("Apakah ingin lanjut menghapus kontak? (y/n): ").lower()
        if lanjut != "y":
            print("Kembali ke menu utama")
            return

    while True:
        nama = input("Masukkan nama kontak yang ingin dihapus: ")

        if not nama.isalpha():
            print("Nama tidak boleh mengandung angka atau simbol!")
            continue

        if nama not in kontak:
            print("Kontak tidak ditemukan.")
            continue

        break

    del kontak[nama]
    print("Kontak berhasil dihapus.")

def menu():
    while True:
        print("\n=== KONTAK ===")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak")
        print("4. Update Email Kontak")
        print("5. Update Nomor Telepon")
        print("6. Hapus Kontak")
        print("7. Keluar")

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
            update_nomor()
        elif pilihan == "6":
            hapus_kontak()
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            continue

menu()