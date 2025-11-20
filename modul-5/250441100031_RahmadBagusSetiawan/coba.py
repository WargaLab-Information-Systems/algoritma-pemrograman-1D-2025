# # FUNGSI (Function)

# def ucapan():
#     print("Selamat Malam")

# ucapan()

# contoh
# Luas Persegi panjang

# # Tanpa fungsi
# p = 5
# l = 3
# luas1 = p * l

# panjang = 8
# lebar = 2
# luas2 = panjang * lebar
# print(luas1, luas2)

# # dengan fungsi
# def hitungluas(panjang, lebar):
#     luas = panjang * lebar
#     print("Luas persegi panjang : ", luas)

# hitungluas(10, 6)
# hitungluas(3, 7)

# # RETURN

# def perkalian(a, b):
#     c = a * b
#     return c

# print(perkalian(3,5))

# # LAMBDA

# tambah = lambda a,b : a+b
# print(tambah(1, 2))

# def tambah2 (a, b,): # Tambah LAMBDA
#     return a+b
# print(tambah2(1,2))

# # Fungsi Rekursif

# def spillAngka(n):
#     if n == 0:
#         print("SELESAI")
#     else:
#         print(n)
#         spillAngka(n - 1)
# spillAngka(5)

# # scope variable

x = 10 #Global

def rubah():
    x = 5 #Local
    return x + 3
print("Nilai x di dalam : ", rubah)

print("Nilai x diluar :", x)

# def perkalian(a,):
#     c = a * a
#     return c

# print(perkalian(int(input("masukkan angka "))))