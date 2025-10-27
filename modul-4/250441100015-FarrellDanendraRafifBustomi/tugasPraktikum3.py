n = int(input("Masukkan angka: "))

for i in range(1, n + 1):
    # bagian kiri
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # bagian spasi di tengah
    for k in range(1, (n - i) * 2 + 1):
        print(" ", end=" ")
    
    # bagian kanan
    for l in range(i, 0, -1):
        print(l, end=" ")
    
    print()
    

