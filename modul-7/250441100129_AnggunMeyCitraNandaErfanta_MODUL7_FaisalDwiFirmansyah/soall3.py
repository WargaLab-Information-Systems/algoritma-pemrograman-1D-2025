# Program Validasi Kupon Diskon Kasir dengan Nama Barang

def tampilkan_menu():
    print("\n--- SISTEM KASIR KUPON ---")
    print("1. Tampilkan Kupon Tersedia")
    print("2. Proses Transaksi")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")
    return pilihan

def tampilkan_kupon(kupon_dict):
    print("\n--- KUPON YANG TERSEDIA ---")
    
    if not kupon_dict:
        print("Tidak ada kupon yang tersedia.")
        return

    print("Kode Kupon     Diskon")
    print("---------------------")
    
    for kode, persen in kupon_dict.items():
        print(f"{kode}          {persen}%")

def proses_transaksi(kupon_dict):
    print("\n--- PROSES TRANSAKSI ---")

   
    nama_barang = input("Masukkan nama barang: ")
    
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        if jumlah <= 0:
            print("Error: Jumlah barang harus lebih dari 0.")
            return
    except:
        print("Error: Jumlah barang harus berupa angka.")
        return

    
    try:
        harga_satuan = float(input("Masukkan harga satuan: Rp "))
        if harga_satuan <= 0:
            print("Error: Harga satuan harus lebih dari 0.")
            return
    except:
        print("Error: Harga satuan harus berupa angka.")
        return

    
    total_belanja = jumlah * harga_satuan

    
    kode_kupon = input("Masukkan kode kupon: ")

    
    if kode_kupon in kupon_dict:
        diskon = kupon_dict[kode_kupon]
        jumlah_diskon = (diskon / 100) * total_belanja
        total_bayar = total_belanja - jumlah_diskon
        
        print("\n--- STRUK PEMBAYARAN ---")
        print(f"Nama Barang   : {nama_barang}")
        print(f"Jumlah        : {jumlah} buah")
        print(f"Harga Satuan  : Rp {harga_satuan:,.2f}")
        print(f"Total Belanja : Rp {total_belanja:,.2f}")
        print(f"Kode Kupon    : {kode_kupon}")
        print(f"Diskon        : {diskon}%")
        print(f"Potongan      : Rp {jumlah_diskon:,.2f}")
        print("------------------------")
        print(f"Total Bayar   : Rp {total_bayar:,.2f}")
        
        
        del kupon_dict[kode_kupon]
        print(f"\nKupon '{kode_kupon}' telah digunakan dan dihapus.")
        
    else:
        print("\n--- KUPON TIDAK VALID ---")
        print(f"Nama Barang   : {nama_barang}")
        print(f"Jumlah        : {jumlah} buah")
        print(f"Harga Satuan  : Rp {harga_satuan:,.2f}")
        print(f"Kode Kupon    : {kode_kupon} (TIDAK VALID)")
        print(f"Total Bayar   : Rp {total_belanja:,.2f}")

def main():
    kupon_tersedia = {
        "DISKON10": 10,
        "HEMAT25": 25,
        "SUPER50": 50,
        "NEW15": 15
    }

    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tampilkan_kupon(kupon_tersedia)
        elif pilihan == '2':
            proses_transaksi(kupon_tersedia)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem kasir!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-3.")


main()