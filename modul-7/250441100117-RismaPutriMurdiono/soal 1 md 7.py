contacts = {}

def input_nama(pesan):
    while True:
        nama = input(pesan)
        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        elif not nama.isalpha():
            print("Nama tidak boleh mengandung angka! Silakan masukkan nama yang valid.")
        else:
            return nama
        
def input_telepon():
    while True:
        telepon = input("Masukkan nomor telepon: ")
        if telepon .isdigit() and len(telepon) == 12:
            return telepon
        else:
           print("nomor harus 12 angka ")
def input_email():
    while True:
        email = input("Masukkan email: ")
        if email == "":
            print("Email tidak boleh kosong!")
        elif "@gmail.com" in email:
            return email
        else:
            print("Email tidak valid! Harus ada '@gmail.com'")

def tampilkan_semua():
    if len(contacts) == 0:
        print("\nBelum ada kontak yang tersimpan.\n")
    else:
        print("\n==== Daftar Semua Kontak ====")
        for nama in contacts:
            print(f"Nama     : {nama}")
            print(f"Telepon  : {contacts[nama][0]}")
            print(f"Email    : {contacts[nama][1]}")
            print("---------------------------")
        print()

def cari_kontak():
    if len(contacts) == 0:
        print("\nBelum ada kontak yang tersimpan.\n")
    else:
        nama = input_nama("Masukkan nama yang ingin dicari: ")
        print("\nKontak ditemukan!")
        print(f"Nama    : {nama}")
        print(f"Telepon : {contacts[nama][0]}")
        print(f"Email   : {contacts[nama][1]}\n")

def tambah_kontak():
    nama = input_nama("Masukkan nama: ")
    if nama in contacts:
        print("Kontak dengan nama tersebut sudah ada!\n")
    else:
        telepon = input_telepon()
        email = input_email()
        contacts[nama] = [telepon, email]
        print("\nKontak berhasil ditambahkan!\n")

def update_email():
    if len(contacts) == 0:
        print("\nBelum ada kontak yang tersimpan.\n")
    else : 
        nama = input_nama("Masukkan nama yang ingin diupdate emailnya: ")
        email_baru = input_email()
        contacts[nama][1] = email_baru
        print("\nEmail berhasil diperbarui!\n")
    

def hapus_kontak():
    nama = input_nama("Masukkan nama kontak yang ingin dihapus: ")
    if nama in contacts:
        del contacts[nama]
        print("\nKontak berhasil dihapus!\n")
    else:
        print("\nKontak tidak ditemukan.\n")

while True:
    print("====== CONTACT BOOK ======")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak Baru")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid! Masukkan angka 1-6.\n")