def faktorial(n):
    if n == 0 or n == 1:
      return 1
    else:
      return n * faktorial(n - 1)
     
n = int(input("Masukkan bilangan bulat non-negatif:"))
if n < 0:
    print("harus bilangan bulat non-negatif")
else:
    hasil = faktorial(n)
    
    langkah = ""
    for i in range(n, 0, -1):
        langkah += str(i)
        if i != 1:
            langkah += " x "
    
    print(f"Hasil faktorial dari bilangan {n} adalah {langkah} = {hasil}")

