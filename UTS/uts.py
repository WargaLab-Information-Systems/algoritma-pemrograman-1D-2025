while True:
    print("=== Rental Motor Aconk ===")
    print("1. Motor Matic  = Rp 50.000/hari")
    print("2. Motor Trail  = Rp 100.000/hari")
    print("3. Motor Sport  = Rp 75.000/hari")

    pilihan = input("Pilih jenis motor (1/2/3): ")
    hari = int(input("Masukkan lama sewa (hari): "))

    if pilihan == "1":
        harga = 50000
        jenis = "Matic"
    elif pilihan == "2":
        harga = 100000
        jenis = "Trail"
    elif pilihan == "3":
        harga = 75000
        jenis = "Sport"
    else:
        print("Pilihan tidak valid!")
        continue

    subtotal = harga * hari

    if hari > 3:
        asuransi = (hari / 3) * 15000
    else:
        asuransi = 0

    if subtotal > 150000:
        diskon = subtotal * 0.10
    else:
        diskon = 0

    total = subtotal - diskon + asuransi

    kupon = input("Masukkan kupon (jika ada): ")
    if kupon == "AconckGG":
        total * 0.05

    print("--- RINCIAN PEMBAYARAN ---")
    print(f"Jenis Motor   : {jenis}")
    print(f"Lama Sewa     : {hari} hari")
    print(f"Harga Sewa    : Rp {harga:,}")
    print(f"Subtotal      : Rp {subtotal:,}")
    print(f"Asuransi      : Rp {asuransi:,}")
    print(f"Diskon        : Rp {diskon:,}")
    print(f"Total Bayar   : Rp {total:,}")

    ulang = input("Apakah ingin sewa lagi? (ya/tidak): ")
    if ulang.lower() != "ya":
        print("Terima kasih telah menggunakan Rental Motor Aconk!")
        break
