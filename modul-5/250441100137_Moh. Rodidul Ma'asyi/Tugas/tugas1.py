def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan bulat non-negatif: "))

if n < 0:
    print("Bilangan harus non-negatif!")
else:
    print(f"Faktorial dari {n} adalah {faktorial(n)}")