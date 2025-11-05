def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*  faktorial(n - 1)
    
N = int(input("Masukkan bilangan bulat non-negatif: "))
if N < 0:
    print("Angka harus non-negatif!")
else:
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah {hasil}")    
    # Faktorial dari 5 itu 5x4x3x2x1