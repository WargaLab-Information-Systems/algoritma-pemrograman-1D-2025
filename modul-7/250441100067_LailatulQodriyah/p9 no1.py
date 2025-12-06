kontak = {}

def validasi_email(email):
    return ("@" in email) and (
        email.endswith("@gmail.com") or
        email.endswith("@yahoo.com") or
        email.endswith("@outlook.com") or
        email.endswith("@hotmail.com")
    )

def tampilkan_semua_kontak():
    if not kontak:
        print("Tidak ada kontak.")
    else:
        print("\n--- Daftar Kontak ---")
        for nama, info in kontak.items():
            print(f"Nama    : {nama}")
            print(f"Telepon : {info['telepon']}")
            print(f"Email   : {info['email']}")
            print("---------------------")

def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in kontak:
        print("Kontak ditemukan:")
        print(f"Nama    : {nama}")
        print(f"Telepon : {kontak[nama]['telepon']}")
        print(f"Email   : {kontak[nama]['email']}")
    else:
        print("Kontak tidak ditemukan.")

def tambah_kontak():
    nama = input("Nama kontak baru: ")

    
    if not nama.isalpha():
        print("Error: nama harus huruf saja.")
        return

    if nama in kontak:
        print("Kontak dengan nama ini sudah ada.")
        return

    telepon = input("Masukkan nomor telepon: ")

    
    if len(telepon) < 12 or len(telepon) > 13:
        print("Error: nomor telepon harus 12–13 digit.")
        return

    if not telepon.isdigit():
        print("Error: nomor telepon harus angka.")
        return


    for info in kontak.values():
        if info["telepon"] == telepon:
            print("Error: nomor telepon sudah terdaftar.")
            return

    email = input("Email: ")
    if not validasi_email(email):
        print("Error: email tidak valid.")
        return

    
    for info in kontak.values():
        if info["email"] == email:
            print("Error: email sudah terdaftar.")
            return

    kontak[nama] = {"telepon": telepon, "email": email}
    print("Kontak berhasil ditambahkan.")

def perbarui_kontak():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")

    if nama not in kontak:
        print("Kontak tidak ditemukan.")
        return

    print("Kosongkan jika tidak ingin diubah.")

    telp_baru = input(f"Telepon baru (lama: {kontak[nama]['telepon']}): ")
    email_baru = input(f"Email baru (lama: {kontak[nama]['email']}): ")

    if telp_baru:
        if not telp_baru.isdigit():
            print("Error: telepon harus angka.")
            return
        kontak[nama]["telepon"] = telp_baru

    if email_baru:
        if not validasi_email(email_baru):
            print("Error: email tidak valid.")
            return
        kontak[nama]["email"] = email_baru

    print("Kontak berhasil diperbarui.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Perbarui kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        perbarui_kontak()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
