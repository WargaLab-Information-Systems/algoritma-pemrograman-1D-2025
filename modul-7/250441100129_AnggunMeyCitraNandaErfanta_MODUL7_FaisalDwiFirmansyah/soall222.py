def tampilkan_menu():
    print("\n--- MANAJEMEN INVENTARIS GUDANG ---")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang (berdasarkan ID)")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

def tampilkan_semua_barang(inventaris):
    print("\n--- Daftar Semua Barang di Gudang ---")
    if not inventaris:
        print("Inventaris masih kosong.")
        return

    print(f"{'ID':<6} | {'Nama Barang':<20} | {'Harga':<10} | {'Stok':<5}")
    print("-" * 50)
    
    for id_barang, info_list in inventaris.items():
        print(f"{id_barang:<6} | {info_list[0]:<20} | {info_list[1]:<10} | {info_list[2]:<5}")

def cari_barang(inventaris):
    print("\n--- Cari Barang ---")
    id_cari = input("Masukkan ID barang yang dicari: ")
    
    if id_cari in inventaris:
        info_list = inventaris[id_cari]
        print("\n--- Barang Ditemukan ---")
        print(f"ID     : {id_cari}")
        print(f"Nama   : {info_list[0]}")
        print(f"Harga  : {info_list[1]}")
        print(f"Stok   : {info_list[2]}")
    else:
        print(f"Barang dengan ID '{id_cari}' tidak ditemukan.")

def tambah_barang(inventaris):
    print("\n--- Tambah Barang Baru ---")
    id_barang = input("Masukkan ID Barang (unik): ")
    
    if id_barang in inventaris:
        print(f"Error: ID Barang '{id_barang}' sudah ada. Gunakan ID lain.")
        return

    nama = input("Masukkan Nama Barang: ")
    
    try:
        harga = int(input("Masukkan Harga (angka): "))
        stok = int(input("Masukkan Stok Awal (angka): "))
        
        if harga < 0 or stok < 0:
            print("Error: Harga dan Stok tidak boleh negatif.")
            return
            
    except ValueError:
        print("Error: Harga dan Stok harus berupa angka yang valid.")
        return

    inventaris[id_barang] = [nama, harga, stok]
    print(f"Barang '{nama}' (ID: {id_barang}) berhasil ditambahkan.")

def update_stok(inventaris):
    print("\n--- Update Stok Barang ---")
    id_barang = input("Masukkan ID barang yang stoknya ingin diupdate: ")

    if id_barang not in inventaris:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
        return
        
    info_list = inventaris[id_barang]
    stok_sekarang = info_list[2]
    
    print(f"Stok saat ini untuk '{info_list[0]}': {stok_sekarang}")

    try:
        perubahan = int(input("Masukkan perubahan stok): "))
    except ValueError:
        print("Error: Perubahan harus berupa angka.")
        return

    stok_baru = stok_sekarang + perubahan

    if stok_baru < 0:
        print(f"Error: Update gagal. Stok tidak bisa menjadi negatif ({stok_baru}).")
        print(f"Stok barang '{info_list[0]}' tetap {stok_sekarang}.")
    else:
        inventaris[id_barang][2] = stok_baru
        print(f"Stok untuk '{info_list[0]}' berhasil diupdate menjadi {stok_baru}.")

def hapus_barang(inventaris):
    print("\n--- Hapus Barang ---")
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if id_barang not in inventaris:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
        return
    
    nama_barang = inventaris[id_barang][0]
    
    konfirmasi = input(f"Apakah Anda yakin ingin menghapus '{nama_barang}' (ID: {id_barang})? (y/n): ").lower()
    
    if konfirmasi == 'y':
        del inventaris[id_barang]
        print(f"Barang '{nama_barang}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def main():
    inventaris_gudang = {}

    while True:
        pilihan_user = tampilkan_menu()
        
        if pilihan_user == '1':
            tampilkan_semua_barang(inventaris_gudang)
        elif pilihan_user == '2':
            cari_barang(inventaris_gudang)
        elif pilihan_user == '3':
            tambah_barang(inventaris_gudang)
        elif pilihan_user == '4':
            update_stok(inventaris_gudang)
        elif pilihan_user == '5':
            hapus_barang(inventaris_gudang)
        elif pilihan_user == '6':
            print("Terima kasih telah menggunakan program inventaris.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-6.")


main()