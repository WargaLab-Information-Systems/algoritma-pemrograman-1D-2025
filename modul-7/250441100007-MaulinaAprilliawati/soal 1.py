kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nBelum ada kontak.")
        return
    print("\n===== DAFTAR KONTAK =====")
    for nama, (telp, email) in kontak.items():
        print(f"{nama} | Telp: {telp} | Email: {email}")
    print("-------------------------")

def cari_kontak():
    nama = input("Nama kontak: ")
    if nama in kontak:
        telp, email = kontak[nama]
        print(f"\nDitemukan: {nama} | {telp} | {email}")
    else:
        print("\nKontak tidak ditemukan.")

def validasi_email(existing_name=None):
    while True:
        email = input("Email: ")

        if "@" not in email:
            print("Error: Email harus mengandung '@'.")
            continue

        pos_at = email.index("@")

        if pos_at == 0 or pos_at == len(email) - 1:
            print("Error: '@' tidak boleh di awal/akhir.")
            continue
        if "." not in email[pos_at:]:
            print("Error: Harus ada titik setelah '@'.")
            continue
        if "@." in email or ".@" in email:
            print("Error: Format email tidak valid.")
            continue

        # Cek email unik
        for nama, (telp, em) in kontak.items():
            if email == em and nama != existing_name:
                print("Error: Email sudah digunakan oleh kontak lain!")
                break
        else:
            return email

def validasi_telp(existing_name=None):
    while True:
        telp = input("Nomor telepon (11 - 13 digit): ")

        if not telp.isdigit():
            print("Error: Nomor telepon harus angka semua!")
            continue

        if len(telp) < 11 or len(telp) > 13:
            print("Error: Nomor telepon harus 11 - 13 digit!")
            continue

        # Cek nomor telepon unik
        for nama, (t, e) in kontak.items():
            if telp == t and nama != existing_name:
                print("Error: Nomor telepon sudah digunakan oleh kontak lain!")
                break
        else:
            return telp

def tambah_kontak():
    nama = input("Nama kontak baru: ")
    if nama in kontak:
        print("Kontak dengan nama ini sudah ada!")
        return
    
    telp = validasi_telp()
    email = validasi_email()
    kontak[nama] = [telp, email]
    print("\nKontak berhasil ditambahkan!")


def update_email():
    nama = input("Nama kontak: ")
    if nama not in kontak:
        print("Kontak tidak ditemukan.")
        return
    
    kontak[nama][1] = validasi_email(existing_name=nama)
    print("\nEmail berhasil diperbarui!")


def hapus_kontak():
    nama = input("Nama kontak: ")
    if nama in kontak:
        del kontak[nama]
        print("\nKontak berhasil dihapus!")
    else:
        print("\nKontak tidak ditemukan.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak baru")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if   pilihan == "1": tampilkan_kontak()
    elif pilihan == "2": cari_kontak()
    elif pilihan == "3": tambah_kontak()
    elif pilihan == "4": update_email()
    elif pilihan == "5": hapus_kontak()
    elif pilihan == "6":
        print("see u sayankk...")
        break
    else:
        print("jangan cari yang gadaa!!")
