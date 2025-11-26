def menu():
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak Berdasarkan Nama")
    print("3. Tambah Kontak Baru")
    print("4. Perbarui Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

def semua_kontak(contacts):
    if not contacts:
        print("\nBelum ada kontak.")
        return
    
    print("DAFTAR SEMUA KONTAK")
    for name, info in contacts.items():
        print(f"\nNama : {name}")
        print(f"Telepon: {info['phone']}")
        print(f"Email  : {info['email']}")
    print(f"Total kontak: {len(contacts)}")

def cari_kontak(contacts, name):
    if name not in contacts:
        print(f"\nKontak dengan nama '{name}' tidak ditemukan!")
        return False

    print("KONTAK DITEMUKAN")
    print(f"Nama   : {name}")
    print(f"Telepon: {contacts[name]['phone']}")
    print(f"Email  : {contacts[name]['email']}")
    return True

def tambah_kontak(contacts):
    print("TAMBAH KONTAK BARU")
    name = input("Masukkan nama kontak: ").strip()
    if not name:
        print("Nama kontak tidak boleh kosong!")
        return
    
    if name in contacts:
        print(f"Kontak dengan nama '{name}' sudah ada!")
        return
    
    phone = input("Masukkan nomor telepon: ").strip()
    email = input("Masukkan email: ").strip()
    
    contacts[name] = {'phone': phone,'email': email}
    
    print(f"\nKontak '{name}' berhasil ditambahkan!")

def perbarui_kontak(contacts):  
    name = input("Masukkan nama kontak yang ingin diperbarui: ").strip()
    if name not in contacts:
        print(f"\nKontak dengan nama '{name}' tidak ditemukan!")
        return
    
    print(f"\nEmail saat ini: {contacts[name]['email']}")
    email_baru = input("Masukkan email baru: ").strip()
    
    contacts[name]['email'] = email_baru
    print(f"\nEmail kontak '{name}' berhasil diperbarui!")

def delete_contact(contacts):
    name = input("Masukkan nama kontak yang ingin dihapus: ").strip()
    
    if name not in contacts:
        print(f"\nKontak dengan nama '{name}' tidak ditemukan!")
        return
    
    confirm = input(f"Apakah Anda yakin ingin menghapus kontak '{name}'? (y/n): ").lower()
    
    if confirm == 'y':
        del contacts[name]
        print(f"\nKontak '{name}' berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")

def main():
    contacts = {}
    
    while True:
        menu()
        pilih = input("\nPilih menu (1-6): ").strip()
        
        if pilih == '1':
            semua_kontak(contacts)
        
        elif pilih == '2':
            name = input("\nMasukkan nama kontak yang dicari: ").strip()
            cari_kontak(contacts, name)
        
        elif pilih == '3':
            tambah_kontak(contacts)
        
        elif pilih == '4':
            perbarui_kontak(contacts)
        
        elif pilih == '5':
            delete_contact(contacts)
        
        elif pilih == '6':
            print("\nTerima kasih telah menggunakan Contact Book!")
            print("Program selesai.\n")
            break
        
        else:
            print("\nPilihan tidak valid! Silakan pilih menu 1-6.")

        input("\nTekan ENTER untuk melanjutkan...")

if __name__ == "__main__":
    main()