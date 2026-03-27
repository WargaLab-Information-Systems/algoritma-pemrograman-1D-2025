kontak_saya = {} 

def validasi_nama_kontak(kontak_input):       
    if not kontak_input:
        return "Nama tidak boleh kosong."
    
    for data in kontak_saya.keys():
        if data == kontak_input:
            return "Nama sudah digunakan pada kontak lain."
    return None

def validasi_nomor_telepon(telp_input):
    if not telp_input:
        return "Nomor telepon tidak boleh kosong."

    if not telp_input.isdigit():
        return "Nomor telepon HANYA boleh mengandung angka (0-9)."

    if len(telp_input) <11 or len(telp_input) >12:
        return "Nomor telepon harus terdiri dari 11 atau 12 digit."

    for data in kontak_saya.values():
        if data[0] == telp_input:
            return "Nomor telepon sudah digunakan pada kontak lain."      
    return None 

def validasi_email(email_input):
    if not email_input:
        return "Email tidak boleh kosong."
    
    if "@gmail.com" not in email_input:
        return "Email tidak valid."
    
    for data in kontak_saya.values():
        if data[1] == email_input:
            return "Email   sudah digunakan pada kontak lain."
    return None

def tampilkan_semua_kontak():
    """1. Tampilkan semua kontak (Read)."""
    print("\n--- DAFTAR KONTAK ---")
    if not kontak_saya:
        print("Kontak masih kosong.")
        return
        
    print(f"{'Nama'} | {'Nomor Telepon'} | Email")
    print("-" * 50)
    
    for nama, data in kontak_saya.items():
        print(f"{nama.title()} | {data[0]} | {data[1]}")

def cari_kontak():
    """2. Mencari kontak berdasarkan nama (Read)."""
    nama_cari = input("Nama kontak yang dicari: ").replace(" ","").lower()
    
    if nama_cari in kontak_saya:
        data = kontak_saya[nama_cari]
        print("\n--- KONTAK DITEMUKAN ---")
        print(f"Nama: {nama_cari.title()}, Telp: {data[0]}, Email: {data[1]}")
    else:

        print(f" Kontak '{nama_cari.title()}' tidak ditemukan.")

def tambah_kontak_baru():

    while True:
        nama = input("Nama kontak: ").replace(" ","").lower()
        
        pesan_error = validasi_nama_kontak(nama) 
        try:
            if pesan_error is None:
                break
            else:
                print(f"Input salah: {pesan_error} Silakan coba lagi.")
        except Exception:
            print(".....")    

    while True:
        telp = input("Masukkan Nomor Telepon (11/12 digit): ").replace(" ","")
        
        pesan_error = validasi_nomor_telepon(telp) 
        
        try:
            if pesan_error is None:
                break
            else:
                print(f"Input salah: {pesan_error} Silakan coba lagi.")
        except Exception:
            print(".....")

    while True:
        email = input("Masukkan Email: ").replace(" ","")
        
        pesan_error = validasi_email(email) 
        try:
            if pesan_error is None:
                break
            else:
                print(f"Input salah: {pesan_error} Silakan coba lagi.")
        except Exception:
            print(".....") 

    kontak_saya[nama] = [telp, email]
    print(f"Kontak '{nama.title()}' berhasil ditambahkan!")

def perbarui_email():
    """4. Mengubah email kontak (UPDATE)."""
    nama_ubah = input("Nama kontak yang emailnya mau diubah: ").replace(" ","").lower()
    if not nama_ubah:
        print("Email tidak boleh kososng")
        return

    if nama_ubah in kontak_saya:
        email_baru = input("Masukkan Email BARU: ")

        kontak_saya[nama_ubah][1] = email_baru 
        print(f"Email '{nama_ubah.title()}' berhasil diperbarui menjadi: {email_baru}.")
    else:
        print(f"Kontak '{nama_ubah.title()}' tidak ditemukan. Tidak bisa diperbarui.")

def hapus_kontak():
    """5. Menghapus kontak (DELETE)."""
    nama_hapus = input("Nama kontak yang ingin dihapus: ").lower()
    
    if nama_hapus in kontak_saya:
        del kontak_saya[nama_hapus]
        print(f"Kontak '{nama_hapus.title()}' berhasil dihapus.")
    else:
        print(f"Kontak '{nama_hapus.title()}' tidak ditemukan. Tidak bisa dihapus.")


while True:
    print("\n=== BUKU KONTAK SEDERHANA & VALID ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak (Read)")
    print("3. Tambah Kontak (Create)")
    print("4. Perbarui Email (Update)")
    print("5. Hapus Kontak (Delete)")
    print("6. Keluar")
    print("---------------------------------------")
        
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        tampilkan_semua_kontak()
    elif pilihan == '2':
        cari_kontak()
    elif pilihan == '3':
        tambah_kontak_baru()
    elif pilihan == '4':
        perbarui_email()
    elif pilihan == '5':
        hapus_kontak()
    elif pilihan == '6':
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")