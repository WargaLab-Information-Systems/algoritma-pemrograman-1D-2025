n = int(input("Masukkan batas angka: "))

print("Bilangan prima dari 1 sampai", n, "adalah:")

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)