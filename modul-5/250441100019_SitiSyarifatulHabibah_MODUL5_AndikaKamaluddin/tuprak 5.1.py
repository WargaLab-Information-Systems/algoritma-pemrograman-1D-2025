def faktorial(N):
    if N == 0 or N == 1:
        return 1
    else : 
        return N * faktorial(N - 1)

print("==== Menghitung Faktorial Dari N ====")

while True:
    try:
        N = int(input("Masukkan bilangan bulat non-negatif: "))

        if N < 0:
            print("Angka tidak boleh negatif! Bisa hanya untuk bilangan bulat positif.")
        else:
            hasil = faktorial(N)
            print("Hasil faktorial dari", N, "adalah", hasil)
            break

    except:
        print("Input tidak valid! Harap masukkan angka bilangan bulat positif, bukan huruf atau simbol.")