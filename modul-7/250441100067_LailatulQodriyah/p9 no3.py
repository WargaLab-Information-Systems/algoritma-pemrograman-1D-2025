kupon = {} 

def tampilkan_semua_kupon():
    if not kupon:
        print("Tidak ada kupon.")
    else:
        print("\n--- Daftar Kupon ---")
        for code, disc in kupon.items():
            print(f"Kode Kupon : {code}")
            print(f"Diskon     : {disc}%")
            print("-----------------------")

def tambah_kupon():
    code = input("Masukkan kode kupon baru: ")
    if code in kupon:
        print("Kode kupon sudah ada.")
        return

    disc = int(input("Masukkan persentase diskon: "))
    if disc <= 0 or disc >= 100:
        print("Diskon harus 1-99%.")
        return

    kupon[code] = disc
    print("Kupon berhasil ditambahkan.")

def hapus_kupon():
    code = input("Masukkan kode kupon yang ingin dihapus: ")
    if code in kupon:
        del kupon[code]
        print("Kupon berhasil dihapus.")
    else:
        print("Kupon tidak ditemukan.")

def proses_transaksi():
    items = []
    while True:
        name = input("Masukkan nama barang (atau 'selesai'): ")
        if name.lower() == "selesai":
            break
        price = int(input(f"Masukkan harga barang '{name}': "))
        items.append((name, price))
    
    if not items:
        print("Tidak ada barang.")
        return

    total = sum(price for _, price in items)
    print("\n--- Daftar Barang ---")
    for name, price in items:
        print(f"{name}: Rp {price}")
    print(f"Total Belanja: Rp {total}")

    
    pakai_kupon = input("Apakah ingin menggunakan kupon? (y/n): ").lower()
    if pakai_kupon == "y":
        code = input("Masukkan kode kupon: ")
        if code not in kupon:
            print("Kupon tidak valid.")
        else:
            discount_percent = kupon[code]
            discount_amount = total * (discount_percent / 100)
            total -= discount_amount
            del kupon[code]
            print(f"Diskon {discount_percent}% diterapkan. Potongan: Rp {discount_amount:.2f}")
            print("Kupon dihapus setelah penggunaan.")
    
    print(f"Total Akhir: Rp {total:.2f}")

while True:
    print("\n====== SISTEM KUPON & KASIR ======")
    print("1. Tampilkan semua kupon")
    print("2. Tambah kupon")
    print("3. Hapus kupon")
    print("4. Mode kasir (transaksi)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_semua_kupon()
    elif pilihan == "2":
        tambah_kupon()
    elif pilihan == "3":
        hapus_kupon()
    elif pilihan == "4":
        proses_transaksi()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")

