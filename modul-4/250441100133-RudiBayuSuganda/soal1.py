baris=int(input("Masukkan jumlah baris lampu:"))
for i in range(1,baris+1):
    n=int(input(f"Masukkan Jumlah lampu pada baris ke-{i}:"))
    for j in range(1,n+1):
        if j%3==0:
            print(f"lampu ke-{j} pada baris ke-{i}: rusak")
        else:
            print(f"lampu ke-{j} pada baris ke-{i}: menyala")
    if i==baris:
        print("---Periksa sambungan daya utama---")
    else:
        print("")
print("")