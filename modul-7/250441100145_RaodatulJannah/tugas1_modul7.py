kontak = {}  

def tambah_kontak():
    while True:
        
        nama = input("Masukkan nama kontak: ")

        if nama == "":
            print("diisi ya namanya!")
            continue


        elif nama in kontak:
           print("Kontak dengan nama tersebut sudah ada!")
           continue
        else: 
            break
        

    while True:
        
        nohp = input("Masukkan nomor HP: ")
        noHP = nohp.replace(" ", "")
        
        if not noHP.isdigit():
            print("Nomor HP nya diisi angka yaa")
            continue

        if len(noHP) < 10 or len(noHP) > 12:
            print("Nomor HP min 10 max 12 digit yaa!")
            continue
        break
        
    while True:
        email = input("Masukkan email: ")
        if "@" not in email or "." not in email:
            print("Format email tidak valid!")
            continue
        if not email.endswith("@gmail.com"):
           print("Email harus menggunakan domain gmail.com ya!")
           continue
        break

    kontak[nama] = [noHP, email]
    print("Kontak berhasil ditambahkan!")


def tampilkan_kontak():
    print("\n=== DAFTAR KONTAK ===")
    if not kontak:
        print("Belum ada kontak.")
        return

    for nama, info in kontak.items():
        print(f"Nama : {nama}")
        print(f"No HP: {info[0]}")
        print(f"Email: {info[1]}")


def cari_kontak():
    while True:
        nama = input("Masukkan nama kontak yang dicari: ")

        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        break

    if nama in kontak:
        print("\nKontak ditemukan:")
        print(f"Nama : {nama}")
        print(f"No HP: {kontak[nama][0]}")
        print(f"Email: {kontak[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")


def perbarui_email():
    while True:
        nama = input("Masukkan nama kontak yang ingin diperbarui: ")

        if nama == "":
            print("Nama tidak boleh kosong!")
            continue

        if nama not in kontak:
            print("Kontak tidak ditemukan!")
            continue

        break

    while True:
        email_baru = input("Masukkan email baru: ")
        if "@" not in email_baru or "." not in email_baru:
            print("Format email tidak valid!")
            continue
        break

    kontak[nama][1] = email_baru
    print("Email berhasil diperbarui!")


def hapus_kontak():
    while True:
        nama = input("Masukkan nama kontak yang ingin dihapus: ")

        if nama == "":
            print("Nama tidak boleh kosong!")
            continue

        if nama not in kontak:
            print("Kontak tidak ditemukan!")
            continue

        break

    del kontak[nama]
    print("Kontak berhasil dihapus!")


while True:
    print("\n=== PROGRAM CONTACT BOOK ===")
    print("1. Tambah kontak (create)")
    print("2. Tampilkan kontak (read)")
    print("3. Cari kontak")
    print("4. Perbarui email (update)")
    print("5. Hapus kontak (delete)")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu not in {"1", "2", "3", "4", "5", "6"}:
        print("Pilihan tidak valid!")
        continue

    if menu == "1":
        tambah_kontak()
    elif menu == "2":
        tampilkan_kontak()
    elif menu == "3":
        cari_kontak()
    elif menu == "4":
        perbarui_email()
    elif menu == "5":
        hapus_kontak()
    elif menu == "6":
        print("Keluar dari program...")
        break