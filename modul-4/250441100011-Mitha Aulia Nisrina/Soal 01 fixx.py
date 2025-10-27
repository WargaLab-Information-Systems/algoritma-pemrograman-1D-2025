# Program Kondisi Lampu di Taman Kota

baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, baris + 1):
    jumlah_lampu = int(input("Masukkan jumlah lampu pada baris " + str(i) + ": "))
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0 or j % 5 == 0:
            print("Lampu ke-", j, "pada baris", i, "rusak.")

        else:
            print("Lampu ke-", j, "pada baris", i, "menyala.")
    if i == baris:
        print("Periksa sambungan daya utama.")