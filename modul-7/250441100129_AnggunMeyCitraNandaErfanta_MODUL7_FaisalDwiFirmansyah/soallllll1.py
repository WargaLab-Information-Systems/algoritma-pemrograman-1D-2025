# Program Buku Kontak Sederhana (CRUD)

def tampilkan_menu():
    print("\n--- BUKU KONTAK ---")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak Baru")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

def validasi_nama(nama):
    """Validasi nama: tidak boleh kosong dan tidak boleh mengandung angka"""
    if not nama.strip():
        print("Error: Nama tidak boleh kosong!")
        return False
    if any(char.isdigit() for char in nama):
        print("Error: Nama tidak boleh mengandung angka!")
        return False
    return True

def validasi_telepon(telp):
    """Validasi telepon: harus angka dan maksimal 13 digit""" 
    if not telp.strip():
        print("Error: Nomor telepon tidak boleh kosong!")
        return False
    if not telp.isdigit():
        print("Error: Nomor telepon harus berupa angka!")
        return False
    if len(telp) > 13:
        print("Error: Nomor telepon maksimal 13 digit!")
        return False
    return True

def validasi_email(email):
    """Validasi email: harus mengandung @ dan domain @gmail.com"""
    if not email.strip():
        print("Error: Email tidak boleh kosong!")
        return False
    if "@gmail.com" not in email:
        print("Error: Email harus mengandung '@gmail.com'!")
        return False
    return True

def tampilkan_semua_kontak(kontak_dict):
    print("\n--- Daftar Semua Kontak ---")
    if not kontak_dict:
        print("Buku kontak masih kosong.")
        return

    for nama, info_list in kontak_dict.items():
        print(f"Nama  : {nama}")
        print(f"Telp  : {info_list[0]}")
        print(f"Email : {info_list[1]}")
        print("-" * 25)

def cari_kontak(kontak_dict):
    print("\n--- Cari Kontak ---")
    nama_cari = input("Masukkan nama yang dicari: ")
    
    if nama_cari in kontak_dict:
        info_list = kontak_dict[nama_cari]
        print("\n--- Kontak Ditemukan ---")
        print(f"Nama  : {nama_cari}")
        print(f"Telp  : {info_list[0]}")
        print(f"Email : {info_list[1]}")
    else:
        print(f"Kontak dengan nama '{nama_cari}' tidak ditemukan.")

def tambah_kontak(kontak_dict):
    print("\n--- Tambah Kontak Baru ---")
    

    while True:
        nama = input("Masukkan Nama: ")
        if validasi_nama(nama):
            break
    
    if nama in kontak_dict:
        print(f"Kontak dengan nama '{nama}' sudah ada. Gunakan menu Update jika ingin mengubah.")
        return

    
    while True:
        telp = input("Masukkan Nomor Telepon: ")
        if validasi_telepon(telp):
            break

    
    while True:
        email = input("Masukkan Email: ")
        if validasi_email(email):
            break
    
    kontak_dict[nama] = [telp, email]
    print(f"Kontak '{nama}' berhasil ditambahkan.")

def update_email(kontak_dict):
    print("\n--- Update Email Kontak ---")
    nama = input("Masukkan nama kontak yang emailnya ingin diupdate: ")

    if nama not in kontak_dict:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
        return
        
    print(f"Email lama untuk {nama}: {kontak_dict[nama][1]}")
    
    
    while True:
        email_baru = input("Masukkan email baru: ")
        if validasi_email(email_baru):
            break
    
    kontak_dict[nama][1] = email_baru
    print(f"Email untuk '{nama}' berhasil diupdate.")

def hapus_kontak(kontak_dict):
    print("\n--- Hapus Kontak ---")
    nama = input("Masukkan nama kontak yang ingin dihapus: ")

    if nama not in kontak_dict:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
        return
        
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus {nama}? (y/n): ").lower()
    
    if konfirmasi == 'y':
        del kontak_dict[nama]
        print(f"Kontak '{nama}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def main():
    buku_kontak_data = {}

    while True:
        pilihan_user = tampilkan_menu()
        
        if pilihan_user == '1':
            tampilkan_semua_kontak(buku_kontak_data)
        elif pilihan_user == '2':
            cari_kontak(buku_kontak_data)
        elif pilihan_user == '3':
            tambah_kontak(buku_kontak_data)
        elif pilihan_user == '4':
            update_email(buku_kontak_data)
        elif pilihan_user == '5':
            hapus_kontak(buku_kontak_data)
        elif pilihan_user == '6':
            print("Terima kasih telah menggunakan program Buku Kontak.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-6.")


main()