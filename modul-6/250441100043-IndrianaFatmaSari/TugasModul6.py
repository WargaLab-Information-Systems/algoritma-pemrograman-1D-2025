# soal nomer 1
data_kunjungan = []
id_antrian = 1

def validasi_nama(nama):
    return nama.strip() != "" and all(h.isalpha() or h == " " for h in nama)


while True:
    print("===== SISTEM KUNJUNGAN SANTRI =====")
    print("1.  Tambah Pengunjung")
    print("2.  Tampilkan Daftar Pengunjung")
    print("3.  Hapus Pengunjung")
    print("4.  Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        print("=== Tambah Pengunjung ===")

        while True:
            nama_pengunjung = input("Nama pengunjung: ")
            if validasi_nama(nama_pengunjung):
                break
            print("Nama hanya boleh huruf dan spasi!")

        while True:
            nama_santri = input("Nama santri yang dijenguk: ")
            if validasi_nama(nama_santri):
                break
            print("Nama hanya boleh huruf dan spasi!")


        while True:
            daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").lower()
            if daerah in ["sumatra", "kalimantan", "jawa"]:
                daerah = daerah.capitalize()
                break
            print("Masukkan hanya Sumatra, Kalimantan, atau Jawa!")

        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID {id_antrian}")
        id_antrian += 1


    elif pilih == "2":
        if not data_kunjungan:
            print("Belum ada data kunjungan.")
            continue

        print("=== Daftar Pengunjung Berdasarkan Daerah ===")
        for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            print(f"-- Pengunjung dari {daerah} --")
            ada = False
            for d in data_kunjungan:
                if d[3] == daerah:
                    print(f"ID: {d[0]}, Pengunjung: {d[1]}, Santri: {d[2]}")
                    ada = True
            if not ada:
                print("Tidak ada pengunjung dari daerah ini.")

    elif pilih == "3":
        if not data_kunjungan:
            print("Tidak ada data untuk dihapus.")
            continue

        try:
            hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
            ditemukan = False

            for d in data_kunjungan:
                if d[0] == hapus:
                    data_kunjungan.remove(d)
                    ditemukan = True
                    print(f"Data dengan ID {hapus} berhasil dihapus.")
                    break

            if not ditemukan:
                print("ID tidak ditemukan.")
                continue

            id_baru = 1
            for d in data_kunjungan:
                d[0] = id_baru
                id_baru += 1

            id_antrian = id_baru

        except ValueError:
            print("ID harus berupa angka!")

    elif pilih == "4":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")



#soal nomor 2
angka1_input = input("masukan baris angka pertama : ")
angka1_list = angka1_input.split()
angka1 = tuple(int(i) for i in angka1_list)

angka2 = input("masukan angka baris kedua : ")
angka2_list = angka2.split()
angka2 = tuple(int(i) for i in angka2_list)


gabung_angka = angka1 + angka2

non_duplikat = []
for x in gabung_angka:
    if x not in non_duplikat:
        non_duplikat.append(x)

for i in range(len(non_duplikat)):
    for j in range(i + 1, len(non_duplikat)):
        if non_duplikat[i] < non_duplikat[j]:
            non_duplikat[i], non_duplikat[j] = non_duplikat[j], non_duplikat[i]

hasil = tuple(non_duplikat)
print("hasil urutan dari yang terbesar dan hapus data duplikat adalah:", hasil)



# soal no3
angka = []

def tambah():
    n = int(input("Masukkan angka: "))
    angka.append(n)

def tampilkan():
    print("Daftar angka:", angka)

def ubah():
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin diubah: "))
    if 0 <= idx < len(angka):
        angka[idx] = int(input("Masukkan angka baru: "))
    else:
        print("Indeks tidak valid.")

def hapus():
    tampilkan()
    idx = int(input("Masukkan indeks angka yang ingin dihapus: "))
    if 0 <= idx < len(angka):
        del angka[idx]
    else:
        print("Indeks tidak valid.")

def cek_bisa_dibagi():
    total = 0
    for i in angka:
        total = total + i

    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi sama)")
        return

    setengah = total // 2
    sum_kiri = 0
    for i in angka:
        sum_kiri += i
        if sum_kiri == setengah:
            print("True (dapat dibagi menjadi dua bagian sama besar)")
            return
    print("False (tidak dapat dibagi dua bagian sama besar)")

while True:
    print("=== PROGRAM PEMERIKSAAN ANGKA ===")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek pembagian sama besar")
    print("6. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        tambah()
    elif menu == "2":
        tampilkan()
    elif menu == "3":
        ubah()
    elif menu == "4":
        hapus()
    elif menu == "5":
        cek_bisa_dibagi()
    elif menu == "6":
        print("Terimakasih, program selesai!")
        break
    else:
        print("Pilihan tidak valid.")


while True :
    nilai = int(input("masukan nilai :"))

    if nilai <= 70 : 
        print("C")
    elif nilai < 85 :
        print("B")
    elif nilai <= 100 :
        print("A")
    else:
        print("tidak ada nilai segitu ka ")
