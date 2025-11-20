kontak = {}

def validasi_email(email):
    while True:
        if email == "":
            print("email tidak boleh kosong")
            return False
        
        if " " in email:
            print("email tidak boleh ada spasi")
            return False
        
        if not email[0].isalnum():
            print("awalan harus huruf atau angka")
            return False
        
        if email.count("@") != 1:
            print("hanya boleh ada satu '@' ")
            return False
        
        if "." not in email or ".." in email:
            print("email harus ada titik (.)")
            return False
        
        if not email[-1].isalpha():
            print("karakter terakhir harus huruf")
            return False
        
        for data in kontak.values():
            if email.lower() == data[1].lower():
                print("Email sudah digunakan oleh kontak lain. Gunakan email lain.")
                email = "" 
                break

        if email == "":
            return False
        
        break
    
    return True

def validasi_nohp(nohp):
    nohp = nohp.replace(" ", "")

    if nohp.startswith("+"):
        nohp = nohp[1:]

    if nohp.startswith("628"):
        nohp = "0" + nohp[2:]

    if not nohp.isdigit():
        return False, None

    if not nohp.startswith("08"):
        return False, None

    if not (12 <= len(nohp) <= 13):
        return False, None

    return True, nohp

def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak: ").strip()

        if nama == "":
            print("Namanya diisi yaa!")
            continue

        if nama in kontak:
            print("Nama kontak sudah ada!")
            continue

        break

    while True:
        nohp = input("Masukkan nomor HP: ").strip()
        valid, hasil = validasi_nohp(nohp)

        if not valid:
            print("Nomor HP tidak valid!")
            continue


        for data in kontak.values():
            if hasil == data[0]:
                print("Nomor HP sudah digunakan kontak lain!")
                valid = False
                break

        if not valid:
            continue

        break

    while True:
        email = input("Masukkan email: ").strip()

        if not validasi_email(email):
            print("Format email tidak valid!")
            continue

        for data in kontak.values():
            if email == data[1]:
                print("Email sudah digunakan kontak lain!")
                valid = False
                break
        else:
            valid = True

        if not valid:
            continue

        break

    kontak[nama] = [hasil, email]
    print("Kontak berhasil ditambahkan!\n")


def tampilkan_kontak():
    print("\n=== DAFTAR KONTAK ===")
    if not kontak:
        print("Belum ada kontak.")
        return

    for nama, info in kontak.items():
        print(f"Nama : {nama}")
        print(f"No HP: {info[0]}")
        print(f"Email: {info[1]}\n")


def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ").strip()

    if nama in kontak:
        print("\nKontak ditemukan:")
        print(f"Nama : {nama}")
        print(f"No HP: {kontak[nama][0]}")
        print(f"Email: {kontak[nama][1]}")
    else:
        print("Kontak tidak ditemukan.")


def perbarui_email():
    while True:
        nama = input("Masukkan nama kontak yang ingin diperbarui: ").strip()

        if nama not in kontak:
            print("Kontak tidak ditemukan!")
            continue
        break

    while True:
        email_baru = input("Masukkan email baru: ").strip()

        if not validasi_email(email_baru):
            print("Format email tidak valid!")
            continue

        for key, value in kontak.items():
            if key != nama and email_baru == value[1]:
                print("Email sudah digunakan kontak lain!")
                valid = False
                break
        else:
            valid = True

        if not valid:
            continue

        break

    kontak[nama][1] = email_baru
    print("Email berhasil diperbarui!")


def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").strip()

    if nama not in kontak:
        print("Kontak tidak ditemukan!")
        return

    del kontak[nama]
    print("Kontak berhasil dihapus!")


while True:
    print("\n=== PROGRAM CONTACT BOOK ===")
    print("1. Tambah kontak")
    print("2. Tampilkan kontak")
    print("3. Cari kontak")
    print("4. Perbarui email")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        tambah_kontak()
    elif pilih == "2":
        tampilkan_kontak()
    elif pilih == "3":
        cari_kontak()
    elif pilih == "4":
        perbarui_email()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid!")
