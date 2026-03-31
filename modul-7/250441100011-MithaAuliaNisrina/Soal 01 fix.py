print("\nPROGRAM CONTACT BOOK BERBASIS CRUD (CREATE, READ, UPDATE, DELETE)\n")

kontak = {
    "Rara": ["087832681956", "rara@gmail.com"],
    "Mitha": ["082220004944", "mitha@gmail.com"],
    "Dila": ["081927406671", "dila@gmail.com"]
}

while True:
    print("MENU UTAMA PROGRAM CONTACT BOOK")
    print("1. Tampilkan Semua Kontak (Read)")
    print("2. Cari Kontak Berdasarkan Nama")
    print("3. Tambah Kontak Baru (Create)")
    print("4. Perbarui Email Kontak (Update)")
    print("5. Hapus Kontak (Delete)")
    print("6. Selesai, Keluar dari Program")

    pilihan = input("\nSilakan pilih menu (Hanya di Nomor 1-6): ")

    try:
        pilihan = int(pilihan)
        if pilihan < 1 or pilihan > 6:
            print("Input tidak valid! Silakan pilih menu nomor 1 hingga 6.\n")
            continue
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka, bukan huruf atau simbol.\nSilakan coba lagi.\n")
        continue

    if pilihan == 1:
        print("\nTAMPILKAN SEMUA KONTAK")
        if len(kontak) == 0:
            print("Belum ada data kontak yang tersimpan.\n")
        else:
            for nama, info in kontak.items():
                print("Nama:", nama, "| Nomor Telepon:", info[0], "| Email:", info[1])
            print()

    elif pilihan == 2:
        print("\nCARI KONTAK BERDASARKAN NAMA")
        while True:
            while True:
                nama_cari = input("Masukkan nama kontak yang ingin dicari: ")
                if nama_cari == "":
                    print("Input tidak valid! Nama tidak boleh kosong. Silakan ulangi.")
                    continue
                if nama_cari == (" "):
                    print("Input tidak valid! Nama tidak boleh hanya spasi. Silakan ulangi.")
                    continue
                break

            nama_ditemukan = None

            for k in kontak:
                if k.lower() == nama_cari.lower():
                    nama_ditemukan = k
                    break

            if nama_ditemukan is None:
                print("Kontak tidak ditemukan. Silakan masukkan nama yang sesuai.\n")
                continue
            else:
                print("Kontak ditemukan!")
                print("Nomor Telepon:", kontak[nama_ditemukan][0])
                print("Email:", kontak[nama_ditemukan][1])
                print()
                break

    elif pilihan == 3:
        print("\nTAMBAH KONTAK BARU")
        while True:
            nama_baru = input("Masukkan nama kontak baru: ")
            if nama_baru == "":
                print("Input tidak valid! Nama tidak boleh kosong. Silakan ulangi.")
                continue
            if nama_baru == (" "):
                print("Input tidak valid! Nama tidak boleh hanya spasi. Silakan ulangi.")
                continue

            nama_sama = None
            for k in kontak:
                if k.lower() == nama_baru.lower():
                    nama_sama = k
                    break

            if nama_sama is not None:
                print("Kontak sudah ada. Silakan gunakan nama lain.")
                continue
            break

        while True:
            no_telp = input("Masukkan nomor telepon: ")
            if no_telp == "":
                print("Input tidak valid! Nomor telepon tidak boleh kosong. Silakan ulangi.")
                continue
            try:
                int(no_telp)
                if not (no_telp.startswith("08") or no_telp.startswith("628")):
                    print("Input tidak valid! Nomor telepon harus dimulai dengan '08' atau '628'. Silakan ulangi.")
                    continue
                if len(no_telp) < 12 or len(no_telp) > 13:
                    print("Input tidak valid! Nomor telepon harus 12-13 digit. Silakan ulangi.")
                    continue
                for k in kontak.values():
                    if no_telp == k[0]:
                        print("Nomor telepon sudah digunakan oleh kontak lain. Gunakan nomor lain.")
                        no_telp = "" 
                        break
                if no_telp == "":
                    continue
                break
            except:
                print("Input tidak valid! Nomor telepon hanya boleh berisi angka. Silakan ulangi.")
                continue

        while True:
            email = input("Masukkan email: ")
            if email == "":
                print("Input email tidak valid! Email tidak boleh kosong. Silakan ulangi.")
                continue
            if " " in email:
                print("Input email tidak valid! Email tidak boleh mengandung spasi. Silakan ulangi.")
                continue
            if email[0].isalnum() == False:
                print("Input email tidak valid! Karakter pertama harus huruf atau angka. Silakan ulangi.")
                continue
            if email.count("@") != 1:
                print("Input email tidak valid! Email harus mengandung tepat satu '@'. Silakan ulangi.")
                continue
            if "." not in email or ".." in email:
                print("Input email tidak valid! Email harus mengandung tanda titik ('.'). Silakan ulangi.")
                continue
            if email[-1].isalpha() == False:
                print("Input email tidak valid! Karakter terakhir harus huruf. Silakan ulangi.")
                continue
            for k in kontak.values():
                if email.lower() == k[1].lower():
                    print("Email sudah digunakan oleh kontak lain. Gunakan email lain.")
                    email = "" 
                    break
            if email == "":
                continue
            break

        kontak[nama_baru] = [no_telp, email]
        print("Kontak berhasil ditambahkan!\n")

    elif pilihan == 4:
        print("\nPERBARUI EMAIL / NOMOR TELEPON KONTAK")

        while True:
            nama_update = input("Masukkan nama kontak yang ingin diperbarui: ")
            if nama_update == "":
                print("Input tidak valid! Nama tidak boleh kosong. Silakan ulangi.")
                continue
            if nama_update == (" "):
                print("Input tidak valid! Nama tidak boleh hanya spasi. Silakan ulangi.")
                continue

            nama_ditemukan = None
            for k in kontak:
                if k.lower() == nama_update.lower():
                    nama_ditemukan = k
                    break

            if nama_ditemukan is None:
                print("Kontak tidak ditemukan. Silakan ulangi.\n")
                continue 
            break

        no_lama = kontak[nama_ditemukan][0]
        email_lama = kontak[nama_ditemukan][1]

        print("\nIni adalah data nomor telepon dan email yang lama.")
        print("Nomor telepon saat ini :", no_lama)
        print("Email saat ini         :", email_lama)
        print()

        while True:  
            while True:
                no_telp_baru = input("Masukkan nomor telepon baru (ENTER jika tidak ingin mengubah): ")

                if no_telp_baru == "":
                    no_telp_valid = None
                    break

                try:
                    int(no_telp_baru)
                    if not (no_telp_baru.startswith("08") or no_telp_baru.startswith("628")):
                        print("Input tidak valid! Nomor telepon harus dimulai dengan '08' atau '628'. Silakan ulangi.")
                        continue
                    if len(no_telp_baru) < 12 or len(no_telp_baru) > 13:
                        print("Input tidak valid! Nomor telepon harus 3-15 digit. Silakan ulangi.")
                        continue
                    if no_telp_baru == no_lama:
                        print("Nomor telepon baru tidak boleh sama dengan nomor sebelumnya.")
                        continue

                    no_telp_valid = no_telp_baru
                    break

                except:
                    print("Input tidak valid! Nomor telepon hanya boleh berisi angka. Silakan ulangi.")
                    continue

            while True:
                email_baru = input("Masukkan email baru (ENTER jika tidak ingin mengubah): ")

                if email_baru == "":
                    email_valid = None
                    break
                
                if " " in email_baru:
                    print("Input email tidak valid! Email tidak boleh mengandung spasi. Silakan ulangi.")
                    continue
                if email_baru[0].isalnum() == False:
                    print("Input email tidak valid! Karakter pertama harus huruf atau angka. Silakan ulangi.")
                    continue
                if email_baru.count("@") != 1:
                    print("Input email tidak valid! Email harus mengandung tepat satu '@'. Silakan ulangi.")
                    continue
                if "." not in email_baru or ".." in email_baru:
                    print("Input email tidak valid! Email harus mengandung tanda titik ('.'). Silakan ulangi.")
                    continue
                if email_baru[-1].isalpha() == False:
                    print("Input email tidak valid! Karakter terakhir harus huruf. Silakan ulangi.")
                    continue
                if email_baru == email_lama:
                    print("Email baru tidak boleh sama dengan email sebelumnya.")
                    continue

                email_valid = email_baru
                break

            if no_telp_valid is None and email_valid is None:
                print("Tidak ada data yang diperbarui. Minimal ubah salah satu.\n")
                continue 

            if no_telp_valid is not None:
                kontak[nama_ditemukan][0] = no_telp_valid
            if email_valid is not None:
                kontak[nama_ditemukan][1] = email_valid
            print("Data kontak berhasil diperbarui!\n")
            break

    elif pilihan == 5:
        print("\nHAPUS KONTAK")
        while True:
            while True:
                nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ")
                if nama_hapus == "":
                    print("Input tidak valid! Nama tidak boleh kosong. Silakan ulangi.")
                    continue
                if nama_hapus == (" "):
                    print("Input tidak valid! Nama tidak boleh hanya spasi. Silakan ulangi.")
                    continue
                break

            nama_ditemukan = None

            for k in kontak:
                if k.lower() == nama_hapus.lower():
                    nama_ditemukan = k
                    break

            if nama_ditemukan is not None:
                del kontak[nama_ditemukan]
                print("Kontak berhasil dihapus!\n")
                break
            else:
                print("Kontak tidak ditemukan.\n")
                continue

    elif pilihan == 6:
        print("\nSELESAI, KELUAR DARI PROGRAM")
        print("Terima kasih! Program Contact Book telah selesai dijalankan.\n")
        break