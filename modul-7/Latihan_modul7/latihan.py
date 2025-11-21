kontak = {}
def validasi_nama(nama):
        if nama.strip() == "":
            return False
        return all(ch.isalpha() or ch == " " for ch in nama)
def validasi_telp(telp):
    return telp.isdigit() and 12 <= len(telp) <= 13
def validasi_email(email):
    return "@" in email and (
        email.endswith("@gmail.com") or
        email.endswith("@yahoo.com") or
        email.endswith("@outlook.com") or
        email.endswith("@hotmail.com")
    )
def tambah_kontak():
    print("\n=== Tambah Kontak ===")
    while True:
        nama = input("Masukkan nama kontak: ")
        if not validasi_nama(nama):
            print("Nama tidak boleh kosong dan hanya boleh huruf serta spasi!")
            continue
        if any(ch.isdigit() for ch in nama):
            print("Nama hanya bisa di input pakai huruf coba lagi!")
            continue
        if nama in kontak:
            print("Nama sudah ada! Gunakan nama lain.")
            continue
        break
  
    while True:
        telp = input("Masukkan nomor telepon (12 - 13 digit): ")
        if not validasi_telp(telp):
            print("Nomor telepon harus angka dan panjang 12 - 13 digit! Coba lagi.")
            continue  
        break
  
    while True:
        email = input("Masukkan email: ")
        if not validasi_email(email):
            print("Email tidak valid! Harus memiliki domain seperti: @gmail.com, @yahoo.com, dll.")
            continue
        break
  
    kontak[nama] = [telp, email]
    print("Kontak berhasil ditambahkan!")
def tampilkan_kontak():
    print("\n=== Daftar Kontak ===")
    if not kontak:
        print("Belum ada kontak.")
        return
    for nama, data in kontak.items():
        print(f"- {nama}: Telp {data[0]}, Email {data[1]}")
def cari_kontak():
    print("\n=== Cari Kontak ===")
    nama = input("Masukkan nama yang dicari: ")
    if nama in kontak:
        telp, email = kontak[nama]
        print(f"Nama: {nama} | Telp: {telp} | Email: {email}")
    else:
        print("Kontak tidak ditemukan.")
def update_kontak():
    print("\n=== Update Email Kontak ===")
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")
    if nama in kontak:
        email_baru = input("Masukkan email baru: ")
        if not validasi_email(email_baru):
            print("Email tidak valid!")
            return
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui!")
    else:
        print("Kontak tidak ditemukan.")
def hapus_kontak():
    print("\n=== Hapus Kontak ===")
    nama = input("Masukkan nama kontak: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Tambah Kontak")
    print("2. Tampilkan Semua Kontak")
    print("3. Cari Kontak")
    print("4. Update Kontak")
    print("5. Hapus Kontak")
    print("0. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        tampilkan_kontak()
    elif pilihan == "3":
        cari_kontak()
    elif pilihan == "4":
        update_kontak()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")