def tampilkan_menu():
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

def tampilkan(inventory):
    if not inventory:
        print("\nBelum ada barang dalam inventaris.")
        return
    
    print(f"\n{'ID':<10} {'Nama Barang':<25} {'Harga':<15} {'Stok':<10} {'Total Nilai':<15}")
    
    total_value = 0
    for item_id, info in inventory.items():
        item_value = info['price'] * info['stock']
        total_value += item_value
        print(f"{item_id:<10} {info['name']:<25} Rp {info['price']:>10,} {info['stock']:>8} Rp {item_value:>12,}")
    print(f"Total Item: {len(inventory)}")
    print(f"Total Nilai Inventaris: Rp {total_value:,}")

def cari(inventory, item_id):
    if item_id not in inventory:
        print(f"\nBarang dengan ID '{item_id}' tidak ditemukan!")
        return False
    
    info = inventory[item_id]
    item_value = info['price'] * info['stock']

    print(f"   ID Barang    : {item_id}")
    print(f"   Nama Barang  : {info['name']}")
    print(f"   Harga        : Rp {info['price']:,}")
    print(f"   Stok         : {info['stock']}")
    print(f"   Total Nilai  : Rp {item_value:,}")
    return True

def tambah(inventory):
    item_id = input("Masukkan ID barang: ").strip()
    if not item_id:
        print("ID barang tidak boleh kosong!")
        return
    
    if item_id in inventory:
        print(f"Barang dengan ID '{item_id}' sudah ada!")
        return
    
    name = input("Masukkan nama barang: ").strip()
    if not name:
        print("Nama barang tidak boleh kosong!")
        return
    
    try:
        price = float(input("Masukkan harga barang: Rp "))
        if price < 0:
            print("Harga tidak boleh negatif!")
            return
    except ValueError:
        print("Harga harus berupa angka!")
        return
    
    try:
        stock = int(input("Masukkan jumlah stok: "))
        if stock < 0:
            print("Stok tidak boleh negatif!")
            return
    except ValueError:
        print("Stok harus berupa angka bulat!")
        return
    
    inventory[item_id] = {'name': name, 'price': price, 'stock': stock}
    
    print(f"\nBarang '{name}' dengan ID '{item_id}' berhasil ditambahkan!")

def perbarui(inventory):
    item_id = input("Masukkan ID barang yang ingin diperbarui: ").strip()
    
    if item_id not in inventory:
        print(f"\nBarang dengan ID '{item_id}' tidak ditemukan!")
        return
    
    print(f"\nNama Barang: {inventory[item_id]['name']}")
    print(f"Stok saat ini: {inventory[item_id]['stock']}")
    
    try:
        new_stock = int(input("Masukkan stok baru: "))
        if new_stock < 0:
            print("Stok tidak boleh negatif!")
            return
    except ValueError:
        print("Stok harus berupa angka bulat!")
        return
    
    inventory[item_id]['stock'] = new_stock
    print(f"\nStok barang '{inventory[item_id]['name']}' berhasil diperbarui menjadi {new_stock}!")

def hapus(inventory):
    item_id = input("Masukkan ID barang yang ingin dihapus: ").strip()
    
    if item_id not in inventory:
        print(f"\nBarang dengan ID '{item_id}' tidak ditemukan!")
        return
    
    item_name = inventory[item_id]['name']
    confirm = input(f"Apakah Anda yakin ingin menghapus barang '{item_name}'? (y/n): ").lower()
    
    if confirm == 'y':
        del inventory[item_id]
        print(f"\nBarang '{item_name}' berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")

def main():
    inventory = {}

    while True:
        tampilkan_menu()
        pilih = input("\nPilih menu (1-6): ").strip()
        
        if pilih == '1':
            tampilkan(inventory)
        
        elif pilih == '2':
            item_id = input("\nMasukkan ID barang yang dicari: ").strip()
            cari(inventory, item_id)
        
        elif pilih == '3':
            tambah(inventory)
        
        elif pilih == '4':
            perbarui(inventory)
        
        elif pilih == '5':
            hapus(inventory)
        
        elif pilih == '6':
            print("\nTerima kasih telah menggunakan sistem inventaris!")
            print("Program selesai.\n")
            break
        
        else:
            print("\nPilihan tidak valid! Silakan pilih menu 1-6.")
        
        input("\nTekan ENTER untuk melanjutkan...")

if __name__ == "__main__":
    main()