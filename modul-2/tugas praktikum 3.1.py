# Program bilangan prima 1 sampai n

n = int(input("Masukkan angka batas: "))

print("Bilangan prima dari 1 sampai", n, "adalah:")

for i in range(2, n + 1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i)