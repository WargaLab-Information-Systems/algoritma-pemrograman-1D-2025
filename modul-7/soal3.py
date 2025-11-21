barang = {
    "A01": ["Indomie Goreng", 3500],
    "A02": ["Beras 5kg", 57000],
    "A03": ["Gula 1kg", 14000],
    "A04": ["Minyak Goreng 1L", 16000],
    "A05": ["Telur 1kg", 26000],
    "A06": ["Tepung terigu 1kg", 6000],
    "A07": ["Susu", 7000],
    "A08": ["Garam", 3000],
    "A09": ["Kecap", 2000],
    "A10": ["Sosis", 9000]
}

kupon = {
    "d4patd1sk0n": 10,
    "sUp3rHem4t": 20,
    "D1scSp3s14l": 30
}

keranjang = []


def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")
    for kode, data in barang.items():
        print(f"{kode} - {data[0]} : Rp{data[1]}")

def tambah_kupon():
    print("\n=== TAMBAH KUPON BARU ===")

    kode = input("Masukkan kode kupon baru: ")

    if kode.strip() == "":
        print("Kode kupon tidak boleh kosong!")
        return
    
    if kode in kupon:
        print("Kode kupon sudah ada!")
        return

    try:
        diskon = int(input("Masukkan persentase diskon (1-100): "))
    except:
        print("Diskon harus berupa angka!")
        return

    if diskon <= 0 or diskon > 100:
        print("Diskon harus antara 1 sampai 100!")
        return

    kupon[kode] = diskon
    print(f"Kupon '{kode}' berhasil ditambahkan dengan diskon {diskon}%!")


def tambah_ke_keranjang():
    tampilkan_barang()
    kode = input("\nMasukkan kode barang: ").capitalize()

    if kode not in barang:
        print("Kode barang tidak ditemukan!")
        return

    try:
        qty = int(input("Masukkan jumlah: "))
    except:
        print("Jumlah harus angka!")
        return

    nama, harga = barang[kode]
    keranjang.append([nama, harga, qty])
    print(f"{qty} x {nama} berhasil ditambahkan!")


def tampilkan_keranjang():
    if not keranjang:
        print("\nKeranjang masih kosong!")
        return

    print("\n=== KERANJANG BELANJA ===")
    total = 0
    nomor = 1   

    for item in keranjang:
        nama, harga, qty = item
        subtotal = harga * qty
        total += subtotal
        print(f"{nomor}. {nama} x {qty} = Rp{subtotal}")
        nomor += 1  

    print(f"\nTotal sebelum diskon: Rp{total}")
    return total

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon tersedia.")
        return

    print("\n=== DAFTAR KUPON TERSEDIA ===")
    for kode, diskon in kupon.items():
        print(f"{kode} : {diskon}%")


def proses_pembayaran():
    total = tampilkan_keranjang()
    if total is None:
        return

    pakai = input("\nPakai kupon? (y/n): ").lower()
    diskon = 0

    if pakai == "y":
        kode = input("Masukkan kode kupon: ")
        if kode in kupon:
            diskon = kupon[kode]
            print(f"Kupon valid! Diskon {diskon}%")
            del kupon[kode] 
        else:
            print("Kupon tidak valid!")

    total_diskon = total * diskon / 100
    total_bayar = total - total_diskon

    print("\n=== STRUK PEMBAYARAN ===")
    print(f"Total: Rp{total}")
    print(f"Diskon: {diskon}% (Rp{int(total_diskon)})")
    print(f"Total Bayar: Rp{int(total_bayar)}")
    print("========================")


while True:
    print("\n=== MENU KASIR ===")
    print("1. Lihat Daftar Barang")
    print("2. Tambah kupon")
    print("3. Tambah ke Keranjang")
    print("4. Lihat Keranjang")
    print("5. Proses Pembayaran")
    print("6. Kupon tersedia")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_barang()
    elif pilih == "2":
        tambah_kupon()
    elif pilih == "3":
        tambah_ke_keranjang()
    elif pilih == "4":
        tampilkan_keranjang()
    elif pilih == "5":
        proses_pembayaran()
    elif pilih == "6":
        tampilkan_kupon()
    elif pilih == "7":
        print("Terima kasih telah berbelanja!")
        break
    else:
        print("Pilihan tidak valid!")