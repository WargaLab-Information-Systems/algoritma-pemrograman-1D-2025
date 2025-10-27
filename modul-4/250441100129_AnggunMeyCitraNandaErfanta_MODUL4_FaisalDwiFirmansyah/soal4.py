n = int(input("Masukkan tinggi piramida : "))

for i in range(n, 0 ,- 1):
    # sisi kiri
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # spasi di tengah
    for k in range(n - i):
        print("    ", end="")  # spasi lebar agar simetris
    
    # sisi kanan (kebalikan)
    for l in range(i, 0, -1):
        print(l, end=" ")
    
    print()  # ganti baris






