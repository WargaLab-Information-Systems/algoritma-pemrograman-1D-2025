n = int(input("Masukkan batas akhir (n): "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")
for i in range(2, n + 1):
    prima = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")