data_inventaris = {}

def tambah_barang():
    while True:
        id = input("Masukkan id barang: ")
        if not id.isdigit():
            print("Input tidak valid")
            continue
        if id in data_inventaris:
            print("Id  sudah ada dalam data")
            print("")
            return
        break
    while True:
        nama = input("Masukkan nama barang: ")
        if nama.isalpha():
            break
        print("input salahh!!")
    while True:
        harga = input("Masukkan harga barang: ")
        if harga.isdigit():
            harga = int(harga)
            break
        print("Inputmu Salah")
    while True:
        stok = input("Masukkan Stok barang: ")
        if stok.isdigit():
            stok = int(stok)
            break
        print("inputmu salah lagiii")
    data_inventaris  [id] = [nama,harga,stok]
    print("----- Berhasil ditambahkan -----")
    print("")
        
def tampilkan_barang():
    if not data_inventaris:
        print("Belum ada barang")
        return
    print("====== Daftar Barang =====")
    for i,j in data_inventaris.items():
        print(f"Id barang: {i}, nama: {j[0]}, harga: {j[1]}, stok barang: {j[2]}")
    print("")
    
def perbarui_stok():
    while True:
        if not data_inventaris:
            print("Belum ada barang ")
            return
        id = input("Masukkan Id stok barang yang mau diubah: ")
        if id in data_inventaris:
            stok_baru = input("Masukkan stok baru pada barang: ")    
            data_inventaris [id] [2] = int(stok_baru)
            print("Stok barang berhasil di perbarui")
            print("")
            break
        print("Input salah ulang dari awal")
        print("")
        return
def hapus_barang():
    if not data_inventaris:
        print("Belum ada barang dalam data inventaris")
        return
    id = input("Masukkan Id barang yang mau di hapus: ")
    if id in data_inventaris:
        del data_inventaris[id]
        print("Barang Berhasil Dihapus")
    else:
        print("Data tidak di temukan")
            
def cari_barang():
    if not data_inventaris:
        print("Belum ada barang di dalam data inventaris")
        return
    id = input("Masukkan Id barang yang mau dicari: ")
    if id in data_inventaris:
        barang = data_inventaris[id]
        print(f"Nama Barang pada id {id} adalah {barang[0]}")
        print("")
    else:
        print("Barang Tidak Ada")
        print("")
def menu():
    print("")
    while True:
        print("1.Tambahkan barang baru")
        print("2.Tampilkan barang")
        print("3.Perbarui stok barang")
        print("4.Hapus barang")
        print("5.Cari data barang berdasarkan ID")
        print("6.Keluar")
        print("")
        pilih = input("Pilih menu: ")
        if pilih =='1':
            tambah_barang()
        elif pilih =='2':
            tampilkan_barang()
        elif pilih =='3':
            perbarui_stok()
        elif pilih =='4':
            hapus_barang()
        elif pilih =='5':
            cari_barang()
        elif pilih =='6':
            print("Selesai")
            break
        else:
            print("Input Salah")
            print("")
menu()