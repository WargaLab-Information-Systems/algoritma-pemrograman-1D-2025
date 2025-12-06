def contact_book():   
    contacts = {}

    def validasi_nama(nama):
        if nama.strip() == "":
            return False
        return all(ch.isalpha() or ch == " " for ch in nama)

    while True:
        print("=== CONTACT BOOK - MENU UTAMA ===")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak berdasarkan Nama")
        print("3. Tambah Kontak Baru")
        print("4. Perbarui Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            if not contacts:
                print("\n Contact book kosong!")
            else:
                print("\n DAFTAR KONTAK:")
                print("-" * 50)
                for nama, info in contacts.items():
                    print(f"Nama : {nama}")
                    print(f"   Telepon: {info[0]}")
                    print(f"   Email  : {info[1]}")
                    print("-" * 50)

        elif pilihan == '2':
            nama = input("\nMasukkan nama yang dicari: ").strip()
            if nama in contacts:
                info = contacts[nama]
                print(f"\n Kontak ditemukan:")
                print(f"Nama    : {nama}")
                print(f"Telepon : {info[0]}")
                print(f"Email   : {info[1]}")
            else:
                print(f"\n Kontak dengan nama '{nama}' tidak ditemukan.")

        elif pilihan == '3':
            nama = input("\nMasukkan nama: ").strip()           
            if nama in contacts:
                print(f" Kontak dengan nama '{nama}' sudah ada!")
            else:
                telepon = input("Masukkan nomor telepon: ").strip()
                email = input("Masukkan email: ").strip()
                contacts[nama] = [telepon, email]
                print(f" Kontak '{nama}' berhasil ditambahkan!")

        elif pilihan == '4':
            nama = input("\nMasukkan nama kontak yang akan diperbarui: ").strip()
            if nama in contacts:
                email_baru = input("Masukkan email baru: ").strip()
                contacts[nama][1] = email_baru
                print(f" Email untuk '{nama}' berhasil diperbarui!")
            else:
                print(f" Kontak dengan nama '{nama}' tidak ditemukan.")

        elif pilihan == '5':
            nama = input("\nMasukkan nama kontak yang akan dihapus: ").strip()
            if nama in contacts:
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus '{nama}'? (y/t): ").strip().lower()
                if konfirmasi == 'y':
                    del contacts[nama]
                    print(f" Kontak '{nama}' berhasil dihapus!")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print(f" Kontak dengan nama '{nama}' tidak ditemukan.")

        elif pilihan == '6':
            print("\n Terima kasih! Program selesai.")
            break

        else:
            print("\n Pilihan tidak valid. Silakan pilih 1-6.")

        input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    contact_book()