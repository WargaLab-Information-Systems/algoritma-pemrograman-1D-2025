def buat_struk():
    nama = input("Nama Pembeli: ")
    barang = []
    harga = []
    
    while True:
        b = input("Nama Barang (selesai): ")
        if b == "selesai":
            break
        h = float(input("Harga: "))
        barang.append(b)
        harga.append(h)

    total = sum(harga)
    print("\n Struk IndoMei ")
    print(f"Pembeli: {nama}")
    
    for i in range(len(barang)):
        print(f"{barang[i]}: Rp {harga[i]:.2f}")
    print(f"Total: Rp {total:.2f}")
    print("Terima kasih!\n")

while True:
    buat_struk()
    if input("Pembeli lain? (y/n): ") != "y":
        break
    