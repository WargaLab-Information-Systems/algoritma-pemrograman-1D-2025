def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
    
angka = int(input("Masukkan bilangan non-negatif: "))

if angka < 0:
    print("Tidak bisa menghitung faktorial dari bilangan negatif!")
else:
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")