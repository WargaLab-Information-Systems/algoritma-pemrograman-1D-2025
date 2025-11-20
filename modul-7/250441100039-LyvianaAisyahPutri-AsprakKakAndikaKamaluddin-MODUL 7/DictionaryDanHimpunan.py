contacts = {}

def validasi_nomor(nomor):
    if nomor == "":
        print("Nomor tidak boleh kosong!")
        return False
    if not nomor.isdigit():
        print("Nomor telepon harus berupa angka!")
        return False
    if len(nomor) < 10:
        print("Nomor telepon terlalu pendek!")
        return False
    if len(nomor) > 13:          
        print("Nomor telepon terlalu panjang!")
        return False
    return True

def validasi_gmail(email):
    if email == "":
        print("Email tidak boleh kosong!")
        return False

    email_lower = email.lower()
    if not (email_lower.endswith("@gmail.com") or
            email_lower.endswith("@yahoo.com") or
            email_lower.endswith("@outlook.com")):
        print("Email harus gmail.com, yahoo.com, atau outlook.com!")
        return False
    return True

def tampilkan_kontak():
    print("\n=== DAFTAR KONTAK ===")
    if len(contacts) == 0:
        print("Tidak ada kontak")
    else:
        for nama, info in contacts.items():
            print(f"Nama: {nama}, Nomor: {info[0]}, Email: {info[1]}")

def cari_kontak():
    nama = input("Masukkan nama kontak: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    if nama in contacts:
        print(f"Nama: {nama}")
        print(f"Nomor: {contacts[nama][0]}")
        print(f"Email: {contacts[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")

def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak: ").strip()
        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        break

    while True:
        nomor = input("Masukkan nomor telepon: ").strip()
        if not validasi_nomor(nomor):
            print("Silakan coba lagi")
            continue

        duplicate_nomor = False
        for info in contacts.values():
            if info[0] == nomor:
                duplicate_nomor = True
                break
        if duplicate_nomor:
            print("Nomor telepon sudah digunakan oleh kontak lain!\n")
            continue
        break

    while True:
        email = input("Masukkan email (gmail/yahoo/outlook): ").strip()
        if not validasi_gmail(email):
            print("Silakan coba lagi.\n")
            continue

        duplicate_email = False
        for info in contacts.values():
            if info[1].lower() == email.lower():
                duplicate_email = True
                break

        if duplicate_email:
            print("Email sudah digunakan oleh kontak lain! Silakan coba lagi.\n")
            continue
        break

    contacts[nama] = [nomor, email]
    print("Kontak berhasil ditambahkan!")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    if nama not in contacts:
        print("Kontak tidak ditemukan.")
        return

    while True:
        email_baru = input("Masukkan email baru (gmail/yahoo/outlook): ").strip()
        if not validasi_gmail(email_baru):
            print("Silakan coba lagi.\n")
            continue

        duplicate = False
        for nama_kontak, info in contacts.items():
            if nama_kontak != nama and info[1].lower() == email_baru.lower():
                duplicate = True
                break

        if duplicate:
            print("Email sudah digunakan oleh kontak lain! Silakan coba lagi.\n")
            continue

        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui!")
        break

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

# Menu utama
while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu: ").strip()

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
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Pilih 1-6.")