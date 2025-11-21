contacts = {}

def validasi_nama(nama):
    if nama == "":
        print("Nama tidak boleh kosong!")
        return False
    if not nama.replace(" ", "").isalpha():
        print("Nama hanya boleh huruf dan spasi!")
        return False
    return True

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
        print("Nomor telepon tidak boleh lebih dari 13 angka!")
        return False
    return True

def validasi_gmail(email):
    if email == "":
        print("Email tidak boleh kosong!")
        return False
    if "@gmail.com" not in email:
        print("Email harus menggunakan @gmail.com!")
        return False
    return True

def tampilkan_kontak():
    print("\n=== DAFTAR KONTAK ===")
    if len(contacts) == 0:
        print("Belum ada kontak.")
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
        if not validasi_nama(nama):
            print("Silakan coba lagi.\n")
            continue
        if nama in contacts:
            print("Kontak dengan nama tersebut sudah ada! Silakan coba lagi.")
            continue
        break

    while True:
        nomor = input("Masukkan nomor telepon: ").strip()
        if not validasi_nomor(nomor):
            print("Silakan coba lagi.\n")
            continue

        for info in contacts.values():
            if info[0] == nomor:
                print("Nomor telepon sudah digunakan oleh kontak lain! Silakan coba lagi.\n")
                break
        else:
            break

    while True:
        email = input("Masukkan email (harus gmail): ").strip()
        if not validasi_gmail(email):
            print("Silakan coba lagi.\n")
            continue

        for info in contacts.values():
            if info[1].lower() == email.lower():
                print("Email sudah digunakan oleh kontak lain! Silakan coba lagi.\n")
                break
        else:
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
        email_baru = input("Masukkan email baru (harus gmail): ").strip()
        if not validasi_gmail(email_baru):
            print("Silakan coba lagi.\n")
            continue

        for nama_k, info in contacts.items():
            if nama_k != nama and info[1].lower() == email_baru.lower():
                print("Email sudah digunakan oleh kontak lain! Silakan coba lagi.\n")
                break
        else:
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