print("\nPROGRAM DERETAN ANGKA BERBASIS CRUD (CREATE, READ, UPDATE, DELETE)")

daftar_angka = []

while True:
    print("\nMENU UTAMA PROGRAM DERET ANGKA")
    print("1. Tambah Angka ke Dalam Daftar (Create)")
    print("2. Tampilkan Seluruh Daftar Angka (Read)")
    print("3. Ubah atau Perbarui Angka Berdasarkan Indeks (Update)")
    print("4. Hapus Angka dari Daftar Berdasarkan Indeks (Delete)")
    print("5. Cek Daftar Dapat Dibagi Menjadi Dua Bagian dengan Jumlah Sama")
    print("6. Selesai, Keluar dari Program")

    pilihan = input("\nSilakan pilih menu (Hanya di Nomor 1-6): ")

    if pilihan == "1":
        print("\nTAMBAH ANGKA KE DALAM DAFTAR")
        while True:
            try:
                angka_baru = int(input("Masukkan angka yang ingin ditambahkan ke dalam daftar: "))
                daftar_angka.append(angka_baru)
                print("Angka", angka_baru, "berhasil ditambahkan ke dalam daftar angka.")
                break
            except:
                print("Input tidak valid! Pastikan hanya memasukkan angka, bukan huruf atau simbol.\nSilakan coba lagi.\n")

    elif pilihan == "2":
        print("\nTAMPILKAN SELURUH DAFTAR ANGKA")
        if len(daftar_angka) == 0:
            print("Belum ada data angka yang tersimpan di dalam daftar. Harap masukkan angka terlebih dahulu pada menu 1.")
        else:
            print("Daftar angka saat ini adalah:", daftar_angka)

    elif pilihan == "3":
        print("\nUBAH ATAU PERBARUI ANGKA BERDASARKAN INDEKS")
        if len(daftar_angka) == 0:
            print("Belum ada data angka yang dapat diubah. Silakan tambahkan data terlebih dahulu.")
        else:
            while True:
                try:
                    indeks = int(input("Masukkan posisi (indeks) angka yang ingin diubah, dimulai dari indeks 0: "))
                    if indeks < 0 or indeks >= len(daftar_angka):
                        print("Indeks yang dimasukkan tidak ditemukan. Silakan masukkan indeks yang benar.\n")
                    else:
                        try:
                            nilai_baru = int(input("Masukkan nilai angka baru yang akan menggantikan nilai sebelumnya: "))
                            daftar_angka[indeks] = nilai_baru
                            print("Nilai pada indeks", indeks, "berhasil diubah menjadi", nilai_baru)
                            break
                        except:
                            print("Input tidak valid! Nilai baru harus berupa angka.\nSilakan coba lagi.\n")
                except:
                    print("Input tidak valid! Indeks harus berupa bilangan bulat.\nSilakan masukkan ulang.\n")

    elif pilihan == "4":
        print("\nHAPUS ANGKA DARI DAFTAR BERDASARKAN INDEKS")
        if len(daftar_angka) == 0:
            print("Tidak ada data angka yang dapat dihapus. Silakan tambahkan data terlebih dahulu.")
        else:
            while True:
                try:
                    indeks_hapus = int(input("Masukkan posisi (indeks) angka yang ingin dihapus, dimulai dari indeks 0: "))
                    if indeks_hapus < 0 or indeks_hapus >= len(daftar_angka):
                        print("Indeks yang dimasukkan tidak ditemukan. Silakan coba lagi.\n")
                    else:
                        angka_dihapus = daftar_angka[indeks_hapus]
                        daftar_angka.pop(indeks_hapus)
                        print("Angka", angka_dihapus, "pada indeks", indeks_hapus, "berhasil dihapus dari daftar.")
                        break
                except:
                    print("Input tidak valid! Indeks harus berupa bilangan bulat.\nSilakan masukkan ulang.\n")

    elif pilihan == "5":
        print("\nPEMERIKSAAN PEMBAGIAN DUA BAGIAN DENGAN JUMLAH SAMA")
        if len(daftar_angka) == 0:
            print("Daftar angka masih kosong. Silakan tambahkan data terlebih dahulu sebelum melakukan pemeriksaan.")
        else:
            total = 0
            for angka in daftar_angka:
                total = total + angka

            if total % 2 != 0:
                print("Jumlah keseluruhan angka dalam daftar adalah", total, "yang merupakan bilangan ganjil.")
                print("Karena jumlahnya ganjil, daftar tidak dapat dibagi menjadi dua bagian dengan jumlah yang sama.")
                print("Hasil akhir pemeriksaan: False")
            else:
                separuh = total // 2
                jumlah = 0
                dapat_dibagi = False

                for angka in daftar_angka:
                    jumlah = jumlah + angka
                    if jumlah == separuh:
                        dapat_dibagi = True
                        break

                if dapat_dibagi:
                    print("Daftar angka", daftar_angka, "dapat dibagi menjadi dua bagian dengan jumlah total yang sama.")
                    print("Hasil akhir pemeriksaan: True")
                else:
                    print("Daftar angka", daftar_angka, "tidak dapat dibagi menjadi dua bagian dengan jumlah total yang sama.")
                    print("Hasil akhir pemeriksaan: False")

    elif pilihan == "6":
        print("\nSELESAI, KELUAR DARI PROGRAM")
        print("\nTerima kasih! Program Deretan Angka Berbasis CRUD telah selesai dijalankan.\n")
        break

    else:
        print("\nPilihan menu tidak valid! Silakan pilih menu di nomor antara 1 hingga 6.")