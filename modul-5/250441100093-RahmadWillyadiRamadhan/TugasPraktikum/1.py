def hitung_faktorial(n):
    if n < 0:
        return "Bilangan harus non negatif"
    if n == 0:
        return 1
    return n * hitung_faktorial(n - 1)

while True:
    n = int(input("Masukkan nilai N untuk faktorial: "))
    if n < 0:
        print("Bilangan harus positif")
        continue
    else :
        hasil = hitung_faktorial(n)
        print(f"Faktorial dari {n} adalah {hasil}")

    if input("Apa ada perhitungan lagi? (y/n): ") != "y":
        break