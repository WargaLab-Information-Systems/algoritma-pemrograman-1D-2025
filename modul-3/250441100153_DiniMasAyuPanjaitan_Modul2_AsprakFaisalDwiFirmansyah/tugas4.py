while True:
    nama = input("\nNama pembeli: ")
    n = int(input("Jumlah barang: "))
    total = 0
    print("\n--- Struk Pembelian IndoMei ---")
    print("Nama:", nama)
    for i in range(n):
        barang = input(f"Nama barang ke-{i+1}: ")
        harga = float(input("Harga: "))
        total += harga
        print(f"- {barang} = Rp{harga:.0f}")
    print("Total harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!")
    if input("Ada pembeli berikutnya? (y/n): ").lower() != 'y':
        break