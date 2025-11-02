n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    
    spasi = (n - i) * 2
    for s in range(spasi):
        print(" ", end="")
    
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()