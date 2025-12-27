data = [] 

def create():
    print("Tambah angka (tanpa ada tambahan apapun(spasi dll))")
    angka = input("Masukkan angka: ")
    for a in angka:
        if not a.isdigit():
            print("masukin angka, jangan ada tambahan apapun itu! ")
            return
    
    for a in angka:
        data.append(int(a))
    print("Data berhasil ditambah.")

def read():
    if not data:
       print("belum ada data")
    else:
        print("Data saat ini:", data)

def update():
    if not data:
        print("harus masukin angka yaa!")
        return
    read()
    try:
       indeks_update = int(input("Masukkan indeks data yang ingin diubah (mulai dari 0): "))
       if 0 <= indeks_update < len(data):
            nilai_baru = int(input("Masukkan nilai baru: "))
            data[indeks_update] = nilai_baru
            print("Data berhasil diubah.")
       else:
            print("Indeks tidak valid.")
    except ValueError:
        print("input harus berupa angka")

def delete():
    if not data:
        print("masukkan angkanya dulu!!")
        return
    read()
    try:
       indeks_hapus = int(input("Masukkan indeks data yang ingin dihapus: "))
       if 0 <= indeks_hapus < len(data):
            del data[indeks_hapus]
            print("Data berhasil dihapus.")
       else:
            print("Indeks tidak valid.")
    except ValueError:
        print("masukkan angka")

def cek_bisa_dibagi():
    if not data:
        print("masukkan angkanya duluuu!!")
        return
    total = 0
    for x in data:  
        total += x

    if total % 2 != 0:
        return False

    target = total // 2

    jumlah = 0
    for i in range(len(data)):
        jumlah += data[i]
        if jumlah == target:
            return True
    return False

while True:
    print("\n=== MENU ===")
    print("1. Tambah angka (Create)")
    print("2. Tampilkan angka (Read)")
    print("3. Ubah angka (Update)")
    print("4. Hapus angka (Delete)")
    print("5. Cek apakah bisa dibagi dua bagian")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        create()
    elif pilih == "2":
        read()
    elif pilih == "3":
        update()
    elif pilih == "4":
        delete()
    elif pilih == "5":
        hasil = cek_bisa_dibagi()
        print("Hasil:", hasil)
    elif pilih == "6":
        break
    else:
        print("Pilihan tidak valid.")