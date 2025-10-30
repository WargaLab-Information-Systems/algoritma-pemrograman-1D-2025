# Program menampilkan bilangan prima dari 1 sampai n

n = int(input("Masukkan batas bilangan (n): "))

print("Bilangan prima dari 1 sampai", n, "adalah:", end=' ')

for angka in range(2, n + 1):
    prima = True
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break
    if prima:
        print(angka, end=' ')

print("\n")

print("Bilangan bukan prima dari 1 sampai", n, "adalah: 1", end=' ')

for angka in range(2, n + 1):
    bukan_prima = False
    for i in range(2, angka):
        if angka % i == 0:
            bukan_prima = True
            break
    if bukan_prima:
        print(angka, end=' ') 