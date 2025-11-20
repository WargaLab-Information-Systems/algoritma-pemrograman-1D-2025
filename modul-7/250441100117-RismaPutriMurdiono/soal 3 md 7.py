kupon = {
    "Dis111".lower() : 10,
    "Promo222".lower() : 25,
    "Sale333".lower() : 50
}

def tampilkan_kupon():
    if not kupon:
        print("MAAF BELUM ADA KUPON YANG TERSEDIA\n")
    else:
        for kode, diskon in kupon.items():
            ("=====DAFTAR KUPON YAANG TERSEDIA=====")
            print(f"Kode voucer   : {kode}")
            print(f"Diskon voucer : {diskon}%")
            print("**********************")

def transaksi():
    total_belanja = float(input("masukkan total belanjaan anda:RP."))
    print("1.Mengggunakan kupon")
    print("2.Tidak menggunakn kupon")
    pilihan = int(input("pilih 1/2: "))
    kode = (input("masukkan kode kuponya: "))

    if pilihan == 1:
        if kode in kupon:
            print("KODE BERHASSIL DI GUNAKAN")
            diskon = kupon[kode]
            potongan = total_belanja * (diskon / 100)
            total_belanja = total_belanja - potongan          
            print("\n=== Transaksi Berhasil ===")
            print(f"Total Belanja : Rp.{total_belanja}")
            print(f"Diskon        : {diskon}%")
            print(f"Potongan      : Rp.{potongan}")
            print(f"Total Bayar   : Rp.{total_belanja}\n")
        else:
            print("MAAF KODE YANG ANDA MASUKKAN TIDAK VALID ATAU SUDAH DI GUNAKAN")
            print(f"Total yang harus di bayar adalah:Rp.{total_belanja}")
            return

    if pilihan == 2:
        print("\n=== Transaksi Berhasil ===")
        print(f"Total Belanja : Rp {total_belanja:.2f}")
        print(f"Diskon        : - ")
        print(f"Potongan      : - ")
        print(f"Total Bayar   : Rp {total_belanja:.2f}\n")
        return

    del kupon[kode]

while True:
    print("=== MENU SISTEM KASIR ===")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        transaksi()
    elif pilihan == "3":
        print("\nProgram selesai. Terima kasih atas belanjanya hari ini!\n")
        break
    else:
        print("\nPilihan tidak valid masukkan angka 1\2\3\n")

daftar_barang = []   # list untuk menyimpan barang yang dibeli

def tambah_barang():
    print("\n=== INPUT DATA BARANG YANG DIBELI ===")
    nama = input("Masukkan nama barang        : ")
    harga = float(input("Masukkan harga satuan (Rp) : "))
    jumlah = int(input("Masukkan jumlah barang     : "))
    
    total = harga * jumlah
    daftar_barang.append([nama, harga, jumlah, total])
    
    print("Barang berhasil ditambahkan!\n")

def tampilkan_barang():
    if not daftar_barang:
        print("\nBelum ada data barang yang dibeli.\n")
        return
    
    print("\n=== DAFTAR BARANG YANG DIBELI ===")
    grand_total = 0
    for i, barang in enumerate(daftar_barang, start=1):
        nama, harga, jumlah, total = barang
        print(f"{i}. {nama}")
        print(f"   Harga  : Rp {harga:.2f}")
        print(f"   Jumlah : {jumlah}")
        print(f"   Total  : Rp {total:.2f}")
        print("-----------------------------")
        grand_total += total
    
    print(f"TOTAL SEMUA BARANG (sebelum diskon kupon): Rp {grand_total:.2f}\n")

while True:
    print("=== MENU DATA BARANG YANG DIBELI ===")
    print("1. Tambah Barang yang Dibeli")
    print("2. Tampilkan Daftar Barang yang Dibeli")
    print("3. Keluar dari Menu Barang")
    pilihan_barang = input("Pilih menu (1/2/3): ")

    if pilihan_barang == "1":
        tambah_barang()
    elif pilihan_barang == "2":
        tampilkan_barang()
    elif pilihan_barang == "3":
        print("\nKeluar dari menu barang.\n")
        break
    else:
        print("\nPilihan tidak valid, masukkan angka 1/2/3\n")