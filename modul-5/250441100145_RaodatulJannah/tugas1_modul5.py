def faktorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
    
while True:
    n = int(input("masukkan bilangan bulat non-negatif: "))
    if n < 0:
        print("harus bilangan bulat non-negatif!")
    else:
        break

hasil = faktorial(n)
print(f"faktorial dari {n} adalah {hasil}")