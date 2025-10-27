print ("\n" + "="*60)
print ("Program menampilkan kondisi lampu di taman kota")
print ("="*60)

jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu di baris {i}: "))

    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0 or j % 5 == 0:
            print(f"Lampu ke-{j} pada baris {i} rusak.")
        else:
            print(f"Lampu ke-{j} pada baris {i} menyala.")

    print ()

    if i == jumlah_baris:
        print("Periksa sambungan daya utama.")


