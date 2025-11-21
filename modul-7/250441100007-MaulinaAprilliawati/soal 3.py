kupon = {
    "LIAIMOETS": 10,
    "ASITENSIASSIK": 20,
    "KOPISUSUNUSANTARA": 5
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon yang tersedia.")
        return
    print("\n=== DAFTAR KUPON TERSEDIA ===")
    for kode, diskon in kupon.items():
        print(f"{kode} - Diskon {diskon}%")

def proses_transaksi():
    print("\n=== INPUT BARANG ===")
    total = 0

    while True:
        nama = input("Nama barang (atau ketik 'wes'): ")

        if nama.lower() == "wes":
            break

        try:
            harga = float(input("Harga barang: Rp "))
            jumlah = int(input("Jumlah barang: "))
        except ValueError:
            print("Input tidak valid, coba lagi!")
            continue

        total += harga * jumlah
        print(f"Subtotal sementara: Rp {total:.2f}\n")

    print(f"\nTotal belanja sebelum diskon: Rp {total:.2f}")

    kode = input("Masukkan kode kupon (atau ENTER jika tidak pakai): ").upper()

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total:.2f}")
        return

    if kode not in kupon:
        print("Kupon tidak valid atau sudah digunakan.")
        return

    diskon = kupon[kode]
    potongan = total * (diskon / 100)
    total_bayar = total - potongan

    print(f"\nKupon valid! Diskon {diskon}%")
    print(f"Total potongan: Rp{potongan:.2f}")
    print(f"Total yang harus dibayar: Rp{total_bayar:.2f}")

    del kupon[kode]

while True:
    print("\n===== SISTEM KASIR + KUPON =====")
    print("1. Tampilkan kupon tersedia")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("tengkiuu~~")
        break
    else:
        print("tidak valid bess")
