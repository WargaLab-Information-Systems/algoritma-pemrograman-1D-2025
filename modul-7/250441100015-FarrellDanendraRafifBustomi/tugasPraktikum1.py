contacts = {}

def valid_email(email):
    if "@" not in email:
        return False
    if " " in email:
        return False

    bagian = email.split("@")
    if len(bagian) != 2:
        return False  

    username, domain = bagian

    if not username:
        return False
    if not domain or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if set(domain) == {"."}:
        return False

    tld = domain.split(".")[-1]
    if not tld:
        return False

    return True

def show_contacts():
    if not contacts:
        print("\nKontak masih kosong.\n")
        return
    for nama, data in contacts.items():
        print(f"Nama : {nama}")
        print(f"Telp : {data[0]}")
        print(f"Email: {data[1]}\n")


def search_contact():
    if not contacts:
        print("\nKontak masih kosong.\n")
        return

    while True:
        nama = input("Masukkan nama kontak (ketik 'batal' jika ingin kembali): ")
        if nama.lower() == "batal":
            print("Pencarian dibatalkan.\n")
            return

        hasil = []
        for key, data in contacts.items():
            if nama.lower() in key.lower():
                hasil.append((key, data))

        if hasil:
            print("\nKontak ditemukan:")
            for key, data in hasil:
                print("Nama :", key)
                print("Telp :", data[0])
                print("Email:", data[1])
                print()
            return
        else:
            print("Kontak tidak ditemukan.\n")


def add_contact():
    print("\n--- Tambah Kontak ---")

    while True:
        nama = input("Nama (ketik 'batal' jika ingin kembali): ").lower()
        if nama.lower() == "batal":
            print("Tambah kontak dibatalkan.\n")
            return

        if nama in contacts:
            print("Nama kontak sudah ada! Gunakan nama lain.\n")
            continue

        break

    while True:
        telp = input("No telepon (ketik 'batal' jika ingin kembali): ")
        if telp.lower() == "batal":
            print("Tambah kontak dibatalkan.\n")
            return
        if not telp.isdigit():
            print("Input harus berupa angka!\n")
            continue
        if len(telp) > 13:
            print("Nomor telepon maksimal 13 digit!\n")
            continue
        if any(telp == data[0] for data in contacts.values()):
            print("Nomor telepon sudah dipakai kontak lain!\n")
            continue
        break

    while True:
        email = input("Email (ketik 'batal' jika ingin kembali): ")
        if email.lower() == "batal":
            print("Tambah kontak dibatalkan.\n")
            return

        email_lc = email.lower()  

        if not valid_email(email_lc):
            print("Format email tidak valid!\n")
            continue

        if any(email_lc == data[1].lower() for data in contacts.values()):
            print("Email sudah dipakai kontak lain!\n")
            continue

        break

    contacts[nama] = [telp, email_lc]
    print("Kontak berhasil ditambahkan.\n")

def update_contact():
    if not contacts:
        print("\nKontak masih kosong.\n")
        return

    print("\n--- Update Kontak ---")

    while True:
        nama = input("Masukkan nama kontak yang ingin diupdate (ketik 'batal'): ")
        if nama.lower() == "batal":
            print("Update kontak dibatalkan.\n")
            return

        if nama in contacts:
            break
        else:
            print("Kontak tidak ditemukan.\n")

    while True:
        pilihan = input("Update apa? (nama/nomor/email atau ketik 'batal' jika ingin kembali): ").lower()

        if pilihan == "batal":
            print("Update kontak dibatalkan.\n")
            return

        if pilihan == "nama":
            while True:
                nama_baru = input("Masukkan nama baru (ketik 'batal'): ").lower()
                if nama_baru.lower() == "batal":
                    print("Update dibatalkan.\n")
                    return
                if nama_baru in contacts:
                    print("Nama baru sudah dipakai! Gunakan nama lain.\n")
                    continue
                contacts[nama_baru] = contacts.pop(nama)
                print("Nama berhasil diperbarui.\n")
                return

        elif pilihan == "nomor":
            while True:
                nomor_baru = input("Masukkan nomor baru (ketik 'batal'): ")
                if nomor_baru.lower() == "batal":
                    print("Update dibatalkan.\n")
                    return
                if not nomor_baru.isdigit():
                    print("Nomor harus berupa angka!\n")
                    continue
                if len(nomor_baru) > 13:
                    print("Nomor telepon maksimal 13 digit!\n")
                    continue
                for key, data in contacts.items():
                    if key != nama and nomor_baru == data[0]:
                        print("Nomor ini sudah dipakai kontak lain!\n")
                        break
                else:
                    contacts[nama][0] = nomor_baru
                    print("Nomor berhasil diperbarui.\n")
                    return

        elif pilihan == "email":
            while True:
                email_baru = input("Masukkan email baru (ketik 'batal' jika ingin kembali): ")
                if email_baru.lower() == "batal":
                    print("Update dibatalkan.\n")
                    return

                email_baru_lc = email_baru.lower()

                if not valid_email(email_baru_lc):
                    print("Format email tidak valid!\n")
                    continue

                for key, data in contacts.items():
                    if key != nama and email_baru_lc == data[1].lower():
                        print("Email ini sudah dipakai kontak lain!\n")
                        break
                else:
                    contacts[nama][1] = email_baru_lc
                    print("Email berhasil diperbarui.\n")
                    return

        else:
            print("Pilihan hanya: nama/nomor/email/batal (jika ingin kembali)\n")

def delete_contact():
    if not contacts:
        print("\nKontak masih kosong.\n")
        return

    print("\n--- Hapus Kontak ---")

    while True:
        nama = input("Masukkan nama kontak (ketik 'batal' jika ingin kembali): ")
        if nama.lower() == "batal":
            print("Hapus kontak dibatalkan.\n")
            return

        if nama in contacts:
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus kontak '{nama}'? (y/n): ").lower()

            if konfirmasi == 'y':
                del contacts[nama]
                print("Kontak berhasil dihapus.\n")
                return 
            elif konfirmasi == 'n':
                print("Penghapusan dibatalkan.\n")
                continue 
            else:
                print("Input tidak valid. Penghapusan dibatalkan. Masukkan nama kontak lagi.\n")
                continue 

        else:
            print("Kontak tidak ditemukan.\n")

while True:
    print("\n====== MENU CONTACT BOOK ======")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update kontak")
    print("5. Hapus kontak")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        show_contacts()
    elif menu == "2":
        search_contact()
    elif menu == "3":
        add_contact()
    elif menu == "4":
        update_contact()
    elif menu == "5":
        delete_contact()
    elif menu == "0":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")