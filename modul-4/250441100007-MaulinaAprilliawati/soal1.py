jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")

    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.\n")
    else:
        print()
