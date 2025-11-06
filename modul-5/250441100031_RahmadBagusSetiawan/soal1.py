def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan bilangan bulat non-negatif: "))

hasil = faktorial(angka)
print("Faktorial dari", angka, "adalah", hasil)