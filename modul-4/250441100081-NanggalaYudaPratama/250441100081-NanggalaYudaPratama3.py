# SOAL 3
n = int(input("Masukkan nilai n: "))

width = len(str(n)) + 1  

for i in range(1, n + 1): # main
    # l
    for j in range(1, i + 1):
        print(f"{j:{width}}", end="")

    # m 
    space = (n - i) * width * 2 
    print(" " * space, end="")

    # r
    for j in range(i, 0, -1):
        print(f"{j:{width}}", end="")

    print()