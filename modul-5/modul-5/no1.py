def faktorial(n):
    
    if n < 0:
        return "Angka harus bilangan bulat non-negatif!"    
    
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
    
try:
    N = int(input("Masukkan bilangan bulat non-negatif: "))
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah: {hasil}")
except ValueError:
    print("Input harus berupa angka bulat!")