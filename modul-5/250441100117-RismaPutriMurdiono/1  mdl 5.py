def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
print("=== Program Faktorial ===")
while True:
    try:
        n = int(input("Masukkan bilangan bulat non-negatif: "))
        
        if n < 0:
            print("Bilangan tidak boleh negatif! Coba lagi.\n")
        else:
            break
    except ValueError:
        print(" Input tidak valid! Harap masukkan angka bulat.\n")

hasil = faktorial(n)
print(f"Hasil dari {n}! adalah: {hasil}")

