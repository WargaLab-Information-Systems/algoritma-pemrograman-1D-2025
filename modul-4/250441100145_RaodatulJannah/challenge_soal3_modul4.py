n = int(input("Masukkan jumlah baris (n): "))

for i in range(n, 0, - 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    spasi = 2 * (n - i)
    for k in range(spasi):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()