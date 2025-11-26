def display_menu():
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi dengan Kupon")
    print("3. Tambah Kupon Baru")
    print("4. Hapus Kupon")
    print("5. Keluar")

def display_all_coupons(coupons):
    if not coupons:
        print("\nBelum ada kupon dalam sistem.")
        return
    
    available = [code for code, used in coupons.items() if not used]
    used = [code for code, used in coupons.items() if used]

    if available:
        print("\nKUPON YANG MASIH TERSEDIA:")
        for code in available:
            print(f"{code} - Diskon {coupons[code]['discount']}%")
    
    if used:
        print("\nKUPON YANG SUDAH DIPAKAI:")
        for code in used:
            print(f"{code} - Diskon {coupons[code]['discount']}% (sudah digunakan)")

def process_transaction(coupons):
    try:
        total_amount = float(input("Masukkan total belanja: Rp "))
        if total_amount <= 0:
            print("Total belanja harus lebih dari 0!")
            return
    except ValueError:
        print("Total belanja harus berupa angka!")
        return
    
    coupon_code = input("Masukkan kode kupon: ").strip().upper()
    
    if not coupon_code:
        print("Kode kupon tidak boleh kosong!")
        return

    if coupon_code not in coupons:
        print(f"\nKUPON TIDAK VALID!")
        print(f"Kode kupon '{coupon_code}' tidak ditemukan dalam sistem.")
        return
    
    if coupons[coupon_code]['used']:
        print(f"\nKUPON SUDAH DIPAKAI!")
        print(f"Kupon '{coupon_code}' sudah pernah digunakan dan tidak dapat dipakai lagi.")
        return

    discount_percent = coupons[coupon_code]['discount']
    discount_amount = total_amount * (discount_percent / 100)
    final_amount = total_amount - discount_amount

    print(f"Kode Kupon         : {coupon_code}")
    print(f"Diskon             : {discount_percent}%")
    print(f"Total Belanja      : Rp {total_amount:,.2f}")
    print(f"Potongan Diskon    : Rp {discount_amount:,.2f}")

    coupons[coupon_code]['used'] = True
    print(f"\nKupon '{coupon_code}' telah digunakan dan dihapus dari sistem.")

def add_coupon(coupons):
    code = input("Masukkan kode kupon (huruf kapital): ").strip().upper()
    if not code:
        print("Kode kupon tidak boleh kosong!")
        return
    
    if code in coupons:
        print(f"Kupon dengan kode '{code}' sudah ada!")
        return
    
    try:
        discount = float(input("Masukkan persentase diskon (0-100): "))
        if discount < 0 or discount > 100:
            print("Persentase diskon harus antara 0-100!")
            return
    except ValueError:
        print("Persentase diskon harus berupa angka!")
        return
    
    coupons[code] = {'discount': discount,'used': False}
    
    print(f"\nKupon '{code}' dengan diskon {discount}% berhasil ditambahkan!")

def delete_coupon(coupons):  
    code = input("Masukkan kode kupon yang ingin dihapus: ").strip().upper()
    
    if code not in coupons:
        print(f"\nKupon dengan kode '{code}' tidak ditemukan!")
        return
    
    confirm = input(f"Apakah Anda yakin ingin menghapus kupon '{code}'? (y/n): ").lower()
    
    if confirm == 'y':
        del coupons[code]
        print(f"\nKupon '{code}' berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")

def main():
    coupons = {}
    
    while True:
        display_menu()
        choice = input("\nPilih menu (1-5): ").strip()
        
        if choice == '1':
            display_all_coupons(coupons)
        
        elif choice == '2':
            process_transaction(coupons)
        
        elif choice == '3':
            add_coupon(coupons)
        
        elif choice == '4':
            delete_coupon(coupons)
        
        elif choice == '5':
            print("\nTerima kasih telah menggunakan sistem kupon!")
            print("Program selesai.\n")
            break
        
        else:
            print("\nPilihan tidak valid! Silakan pilih menu 1-5.")
        
        input("\nTekan ENTER untuk melanjutkan...")
if __name__ == "__main__":
    main()