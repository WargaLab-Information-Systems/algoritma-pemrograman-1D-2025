n = int(input("masukkan nilai n: "))

width = len(str(n)) + 1  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j:{width}}", end="")

    space = (n - i) * width * 2 
    print(" " * space, end="")

    for j in range(i, 0, -1):
        print(f"{j:{width}}", end="")

    print() 