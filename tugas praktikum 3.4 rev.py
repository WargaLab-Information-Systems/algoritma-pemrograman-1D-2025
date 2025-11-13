# Program struk pembelian IndoMei

while True:
    print("\n=== INDoMEI ===")

    # Validasi nama pembeli tidak boleh ada angka
    while True:
        nama = input("Masukkan nama pembeli: ")
        if any(char.isdigit() for char in nama):
            print("Input berisikan angka, silahkan masukkan nama dengan benar!")
        else:
            break

    # Validasi jumlah barang harus angka
    while True:
        jumlah_input = input("Masukkan jumlah barang yang dibeli: ")
        if jumlah_input.isdigit():
            jumlah_barang = int(jumlah_input)
            break
        else:
            print("jumlah barang harus menggunakan angka, coba lagi.")

    daftar_barang = []
    total = 0

    for i in range(jumlah_barang):
        while True:
            nama_barang = input(f"Nama barang ke {i+1}: ")

            # Cek apakah nama barang hanya angka
            if nama_barang.isdigit():
                print("Nama barang tidak bisa dengan menggunakan angka, coba lagi.")
            else:
                break

        # Validasi harga: kalau mengandung huruf -> minta input ulang
        while True:
            harga_input = input(f"Harga {nama_barang}: Rp ")
            try:
                harga = float(harga_input)
                break
            except ValueError:
                print("harga barang mengandung huruf, silahkan coba lagi dengan memasukkan angka yang benar")

        daftar_barang.append((nama_barang, harga))
        total += harga

    print("\n----- STRUK PEMBELIAN -----")
    print("Nama pembeli:", nama)
    print("Daftar Barang:")
    for barang, harga in daftar_barang:
        print(f"- {barang} : Rp{harga:,.0f}")
    print("----------------------------")
    print(f"Total Harga: Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei!")

    lagi = input("\nApakah ada pembeli berikutnya? (y/n): ").lower()
    if lagi != 'y':
        print("Program selesai.")
        break
