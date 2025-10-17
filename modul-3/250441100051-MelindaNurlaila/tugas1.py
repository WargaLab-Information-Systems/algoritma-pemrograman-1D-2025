n = int(input("Masukkan nilai n: "))

print("Bilangan prima dari 1 hingga", n, ":")

for i in range (2, n):
    n = n + 1
    prima = True

    for j in range (2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i)