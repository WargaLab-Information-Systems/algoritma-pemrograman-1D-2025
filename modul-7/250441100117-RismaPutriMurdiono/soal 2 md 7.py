inventaris = {}

def menampilkan_barang ():
    print("=====NAMA NAMA BARANG=====")
    if not inventaris:
        print("maaf belum ada barang")
    else:
        for nama,data in inventaris.items():
            print(f"Id barang  : {nama}")
            print(f"Nama       : {data [0]}")
            print(f"Harga      : {data [1]}")
            print(f"Stok       : {data[2]}")
            print("****************************")

def mencari_barang():
    if not inventaris:
        print("maaf belum ada barang")
    else :
        id_barang = (input("masukkan id barang yang ingin di cari: "))

        print("=====BARANG YANG ANDA CARI DI TEMUKAN=====")
        print(f"Id barang  : {id_barang}")
        print(f"Nama       : {inventaris[id_barang][0]}")
        print(F"Harga      : {inventaris[id_barang][1]}")
        print(f"Stok       : {inventaris[id_barang][2]}")
        print("\n")

def menambahkan_barang():
    id_barang = (input("masukkan id barang yang ingin di tambahkan: "))
    if id_barang in inventaris:
        print("maaf id barang  yang anda masukkan sudah ada")
        return
    if not id_barang.isdigit():
        print("id itu angkaaa")
    while True:
        nama = (input("Masukkan nama barang: "))
        if not nama.isalpha():
            print("harus penamaan huruf ya")
        else:
            break
    while True:
        harga = float(input("Masukkan harga barang: "))
        if harga < 0:
            print("ga bisa hasil negatif")
        else:
            break

    while True:
        stok = int(input("masukkan stok:"))

        if stok < 0:
                print("maaf jumlah yang di kurangi tidak boleh negatif")
        else:
            break
    inventaris[id_barang]=[nama, harga, stok]
    print("=====ID BARANNG BARU BERHASIL DI TAMBAHKAN=====\n")

def memperbarui_stok():
    if inventaris:
        id_barang = (input("masukkan id barang yang ingin di ubah stoknya: "))

        if id_barang in inventaris:
            idb = id_barang
            nama = inventaris[id_barang][0]
            harga = inventaris[id_barang][1]
            stok = inventaris[id_barang][2]
            print("=====STOK BARANG SEMENTARA=====")
            print(f"Id barang   : {idb}")
            print(f"Nama barang : {nama}")
            print(F"Harga       : {harga}")
            print(f"Stok        : {stok}")
            print("")
            print("1.menambah stok")
            print("2.mengurangi stok")
            while True:
                pilihan = int(input("masukkan pilihan 1\ 2: "))
                
                if pilihan > 2:
                    print("1 dan 2 tok lohh yang disuruh, jangan lebih")
                else:
                    break
            if pilihan == 1:
                stok_tambah = int(input("masukkan berapa stok barang yang akan di tambah: "))
                inventaris[id_barang][2] += stok_tambah
                print("-----STOK BERHASIL DI TAMBAH-----")
                print("=====STOK BARAANG SEKARANG=====")
                print(f"Id barang  : {id_barang}")
                print(f"Nama       : {inventaris[id_barang][0]}")
                print(F"Harga      : {inventaris[id_barang][1]}")
                print(f"Stok       : {inventaris[id_barang][2]}")
                print("\n")
            elif pilihan == 2:
                while True:
                    stok_kurang = int(input("masukkan jumlah barang yaang akan di kurangi: "))
                    if stok_kurang < 0:
                     print("maaf jumlah yang di kurangi tidak boleh negatif")
                     continue
                    if stok - stok_kurang < 0:
                     print(f"maaf jumlah stok barang {stok} tidak bisa di kurangi dengan {stok_kurang}\n")
                     continue

                    inventaris[id_barang][2] -= stok_kurang
                    print("-----STOK BERHASIL DI KURANGI-----")
                    print("=====STOK BARANG SEKARANG=====")
                    print(f"Id barang  : {id_barang}")
                    print(f"Nama       : {inventaris[id_barang][0]}")
                    print(F"Harga      : {inventaris[id_barang][1]}")
                    print(f"Stok       : {inventaris[id_barang][2]}")
                    print("\n")
                    break     
    else:
        print("maaf id barang yang anda masukkan idak ada dalam data atau tidak di temukan\n")

def menghapus_barang():
    id_barang = (input("masukkan id barang  yang ingin di hapus")).lower()
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("=====BARANG BERHASIL DI HAPUS=====\n")
    if not inventaris:
        print("maaf belum ada barang")
    else:
        print("maaf id barang yang anda massukkan idak ada dalam data atau tidak di  temukan\n")

while True:
    print("=====DAFTAR MENU inventaris BARANG=====")
    print("1.Tampilkan semua barang")
    print("2.Mencari barang")
    print("3.Menambahkan barang baru")
    print("4.memperbarui stok barang")
    print("5.menghapus barang")
    print("6.keluar")

    pilih = int(input("pilih menu dari no 1/2/3/4/5/6: "))

    if pilih == 1:
        menampilkan_barang()
    elif pilih == 2:
        mencari_barang()
    elif pilih == 3:
        menambahkan_barang()
    elif pilih == 4:
        memperbarui_stok()
    elif pilih == 5:
        menghapus_barang()
    elif pilih == 6:
        print("program inventaris sudah selesai.terima kasih sampai jumpa")
        break
    else:
        print("kode yang anda masukkan tidak valid!!!!! masukkan antara angka 1 - 6")