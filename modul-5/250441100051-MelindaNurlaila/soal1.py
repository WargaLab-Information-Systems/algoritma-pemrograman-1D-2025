def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    n = int(input("Masukkan bilangan bulat non-negatif : "))
    if n < 0:
        print("Faktorial tidak didefinisikan untuk bilangan negatif! Coba lagi.")
    else:
        break

hasil = faktorial(n)

if n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    proses = " x ".join(str(i) for i in range(n, 0, -1))
    print(f"{n}! = {proses} = {hasil}")