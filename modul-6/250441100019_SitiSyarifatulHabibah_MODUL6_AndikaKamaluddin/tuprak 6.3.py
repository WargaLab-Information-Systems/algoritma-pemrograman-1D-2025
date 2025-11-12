a_list = []
def cek_sama(daftar):
    total = 0
    for a in daftar:
        total = total + a

    if total % 2 != 0:
        return False
    
    setengah = total // 2
    jumlah = 0
    for a in daftar:
        jumlah += a
        if jumlah == setengah:
            return True
    return False

while True:
    print("========================================")
    print("============ PROGRAM CEK LIST ==========")
    print("1.Tambah angka (Create)")
    print("2.Tampilkan angka (Read)")
    print("3.Ubah angka (Update)")
    print("4.Hapus angka (Delete)")
    print("5.Cek apakah dua bagia sama")
    print("6.EXIT")
    
    pilihan = input("Pilih menu: ")

    if pilihan  == "1":
        angka = int(input("Masukkan angka: "))
        a_list.append(angka)
        print("Ok! Data sudah ditambah!")

    elif pilihan == "2":
        print("Daftar angka: ", a_list)

    elif pilihan == "3":
        print("Daftar angka: ", a_list)
        idx = int(input("Masukkan indeks mana yang mau diubah: "))
        if 0 <= idx < len(a_list):
            baru = int(input("Nilai barunya berapa: "))
            a_list[idx] = baru
            print("Sip, udah diganti")
        else:
            print("Indeks gak ada, coba cek lagi!")

    elif pilihan == "4":
        print("Daftar angka: ", a_list)
        idx = int(input("Masukkan indeks yang mau dibuang: "))
        if 0 <= idx < len(a_list):
            del a_list[idx]
            print("Sudah berhasil dihapus")
        else:
            print("Indeks kosong, tidak bisa dihapus")

    elif pilihan == "5":
        if len(a_list) == 0:
            print("List masih kosong, tambahin datanya dulu baru cek!")
        else:
            hasil = cek_sama(a_list)
            print("Bisa dibagi dua sama: ", hasil)

    elif pilihan == "6":
        print("Program ditutup zZz")
        break

    else:
        print("Tidak valid, pilih yang bener!")
