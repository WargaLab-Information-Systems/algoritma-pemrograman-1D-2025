contacts = {}


def input_nama():
    while True:
        name = input("Masukkan nama: ").strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Nama hanya boleh mengandung huruf! Coba lagi.\n")

def input_phone():
    while True:
        phone = input("Masukkan nomor telepon (12–13 angka): ").strip()
        
        if not phone.isdigit():
            print("Nomor telepon hanya boleh angka! Coba lagi.\n")
        
        elif len(phone) < 12:
            print("Nomor telepon minimal 12 angka! Coba lagi.\n")
        
        elif len(phone) > 13:
            print("Nomor telepon maksimal 13 angka! Coba lagi.\n")
        
        else:
            return phone

def input_email():
    while True:
        email = input("Masukkan email (@gmail.com, tanpa spasi): ").strip()

        if " " in email:
            print("Email tidak boleh mengandung spasi! Coba lagi.\n")

        elif not email.endswith("@gmail.com"):
            print("Email harus menggunakan @gmail.com! Coba lagi.\n")
        
        else:
            return email


def check_empty():
    if not contacts:
        print("\nBelum ada kontak, silakan tambahkan kontak terlebih dahulu!\n")
        return True
    return False

def show_all_contacts():
    if check_empty():
        return
    print("\n--- Daftar Kontak ---")
    for name, info in contacts.items():
        print(f"Nama : {name}")
        print(f"Telepon : {info[0]}")
        print(f"Email   : {info[1]}\n")

def search_contact():
    if check_empty():
        return
    name = input("Masukkan nama kontak yang dicari: ").strip()
    if name in contacts:
        print("\nKontak ditemukan:")
        print(f"Nama    : {name}")
        print(f"Telepon : {contacts[name][0]}")
        print(f"Email   : {contacts[name][1]}")
    else:
        print("Kontak tidak ditemukan.")

def add_contact():
    print("=== Tambah Kontak Baru ===")
    name = input_nama()

    if name in contacts:
        print("Kontak sudah ada!\n")
        return

    phone = input_phone()
    email = input_email()
    contacts[name] = [phone, email]
    print("Kontak berhasil ditambahkan!\n")

def update_email():
    if check_empty():
        return
    name = input("Masukkan nama kontak yang ingin diperbarui emailnya: ").strip()
    if name in contacts:
        contacts[name][1] = input_email()
        print("Email berhasil diperbarui!\n")
    else:
        print("Kontak tidak ditemukan.")

def delete_contact():
    if check_empty():
        return
    name = input("Masukkan nama kontak yang ingin dihapus: ").strip()
    if name in contacts:
        del contacts[name]
        print("Kontak berhasil dihapus!\n")
    else:
        print("Kontak tidak ditemukan.")


def menu():
    while True:
        print("\n=== Contact Book ===")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak")
        print("3. Tambah kontak")
        print("4. Perbarui email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")

        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            add_contact()
        elif choice == "4":
            update_email()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()
