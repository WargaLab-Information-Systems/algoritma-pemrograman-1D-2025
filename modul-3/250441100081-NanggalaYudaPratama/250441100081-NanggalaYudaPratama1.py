n = int(input("Masukkan bilangan ke-n: "))

print(f"Bilangan prima dari 1 sampai {n}:")
for ang in range(2, n + 1):
    prima = True
    for i in range(2, int(ang**0.5) + 1): # faktor dr 2-akar^2 angka
        if ang % i == 0:
            prima = False
            break
    if prima:
        print(ang, end=" ")