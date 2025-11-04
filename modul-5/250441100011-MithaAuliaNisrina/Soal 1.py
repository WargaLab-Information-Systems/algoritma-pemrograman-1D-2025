print("Program Menghitung Faktorial dengan Fungsi Rekursif\n")

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

while True:
    try:
        n = int(input("Masukkan bilangan bulat non-negatif: "))

        if n < 0:
            print("Angka tidak boleh negatif! Bisa hanya untuk bilangan bulat positif.")
        else:
            hasil = faktorial(n)
            print("Hasil faktorial dari", n, "adalah", hasil)
            break

    except:
        print("Input tidak valid! Harap masukkan angka bilangan bulat positif, bukan huruf atau simbol.")