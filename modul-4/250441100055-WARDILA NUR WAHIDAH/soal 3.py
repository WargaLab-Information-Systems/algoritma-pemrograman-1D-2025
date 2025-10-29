# Program mencetak dua piramida angka berhadapan
n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
    # Piramida kiri
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Spasi tengah
    spasi = (n - i) * 2
    for s in range(spasi):
        print(" ", end=" ")
    
    # Piramida kanan (cermin)
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()