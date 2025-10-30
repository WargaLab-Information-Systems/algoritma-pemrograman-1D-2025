n = int(input("Masukkan jumlah baris (n): "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(f"{j:2}", end="")


    for k in range((n - i) * 2):
        print("  ", end="")


    for j in range(i, 0, -1):
        print(f"{j:2}", end="")

    print()