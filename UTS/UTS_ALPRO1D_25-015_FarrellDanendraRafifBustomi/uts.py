while True:
    print("1. Motor Matic   - Rp 50.000")
    print("2. Motor Trail   - Rp 100.000")
    print("3. Motor Sport   - Rp 75.000")

    pilihan = input("Pilih jenis motor [1-3]: ")

    if pilihan == "1":
        jenis_motor = "Matic"
        harga = 50000
    elif pilihan == "2":
        jenis_motor = "Trail"
        harga = 100000
    elif pilihan == "3":
        jenis_motor = "Sport"
        harga = 75000
    else:
        print("Pilihan tidak valid!")
        continue

    lama_sewa = int(input("Masukkan lama sewa (hari): "))
    subtotal = harga * lama_sewa

    if lama_sewa > 3:
        asuransi = (lama_sewa // 3) * 15000
    else:
        asuransi = 0

    total = subtotal + asuransi

    if subtotal > 150000:
        diskon = total * 0.10
    else:
        diskon = 0

    total -= diskon

    kupon = input("Masukkan kupon (jika ada): ")
    if kupon == "AconkGG":
        diskon_kupon = total * 0.05
    else:
        diskon_kupon = 0

    total -= diskon_kupon

    print(f"Jenis Motor     : {jenis_motor}")
    print(f"Lama Sewa       : {lama_sewa} hari")
    print(f"Harga Sewa      : Rp {harga:,}")
    print(f"Subtotal        : Rp {subtotal:,}")
    print(f"Asuransi        : Rp {asuransi:,}")
    print(f"Diskon          : Rp {diskon:,}")
    print(f"Diskon Kupon    : Rp {diskon_kupon:,}")
    print(f"Total Bayar     : Rp {total:,}")

    ulang = input("Apakah ingin sewa lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih telah menggunakan Rental Motor Aconk!")
        break
