# Fungsi rekursif untuk menghitung faktorial
def faktorial(n):
    # Basis: jika n adalah 0 atau 1, kembalikan 1
    if n == 0 or n == 1:
        return 1
    else:
        # Rekursi: n * faktorial(n-1)
        return n * faktorial(n - 1)

# Program utama
try:
    n = int(input("Masukkan bilangan bulat non-negatif: "))
    if n < 0:
        print("Maaf, bilangan harus non-negatif.")
    else:
        hasil = faktorial(n)
        print(f"Faktorial dari {n} adalah: {hasil}")
except ValueError:
    print("Input tidak valid! Harus berupa bilangan bulat.")
