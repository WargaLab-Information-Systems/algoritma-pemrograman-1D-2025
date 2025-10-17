# Program menampilkan bilangan prima dari 1 sampai n

# Meminta input batas angka
n = int(input("Masukkan batas bilangan: "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

# Perulangan dari 2 sampai n
for i in range(2, n + 1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=' ')