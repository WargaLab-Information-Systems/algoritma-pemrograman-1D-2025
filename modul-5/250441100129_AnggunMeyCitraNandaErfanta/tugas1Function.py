def faktorial (n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * faktorial(n-1)
    
print("=== PROGRAM MENGHITUNG FAKTORIAL ===")
print("==============================================")
print()

N = int (input( "input angka : "))

if N < 0:
    print (" maaf , bilangan harus non- negatif!")
else:
    hasil = faktorial(N)
    print (f"hasil faktorial dari {N}! adalah: {hasil}")

