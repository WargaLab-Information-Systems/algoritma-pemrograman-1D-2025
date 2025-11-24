data = [] 

def create():
    print("Tambah angka (pisahkan dengan spasi):")
    angka = input("Masukkan angka: ").split()
    for a in angka:
        if not a.isdigit():
            print("masukin angkaaa bukan huruf lohh!! ")
            return
    
    for a in angka:
        data.append(int(a))
    print("Data berhasil ditambah.")

def read():
    if not data:
        print("belom ada data")
    else :
        print("Data saat ini:", data)

def update():
    if not data:
        print("masukkan angkanya duluuu!!")
        return
    read()
    idx = int(input("Ubah data pada indeks ke berapa? "))

    if 0 <= idx < len(data):
        nilai_baru = int(input("Masukkan nilai baru: "))
        data[idx] = nilai_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")

def delete():
    if not data:
        print("masukkan angkanya duluuu!!")
        return
    read()
    try:
        idx = int(input("Hapus data pada indeks ke berapa? "))
        if 0 <= idx < len(data):
            del data[idx]
            print("Data berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("masukinnya angkaa")  

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

    pilih = input("Pilih menu: ")

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