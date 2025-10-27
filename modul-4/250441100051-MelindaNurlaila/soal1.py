n = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, n + 1):
    
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{i}: "))
    
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Lampu ke-{j} pada baris {i} rusak.")
        else:
            print(f"Lampu ke-{j} pada baris {i} menyala.")
    
    if i == n:
        print("Periksa sambungan daya utama.")