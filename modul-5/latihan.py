# def morning():
#     print("selamat pagi")


# morning()


# #hitung luas persegi panjang(non-function)
# panjang = 5
# lebar = 3
# luas1 = panjang * lebar

# panjang2 = 8
# lebar2 = 2
# luas2 = panjang2 * lebar2
# print(luas1, luas2)

# #menghitung luas persegi panjang(function)
# def hitung (panjang, lebar):
#     luas = panjang * lebar
#     print("luas persegi panjang adalah:", luas)

# hitung luas(10, 6)
# hitung luas (5, 2)

# #function dengan return
# def perkalian(a):
#     c = a * a
#     return c
# print(perkalian(perkalian(angka)))

#lambda
# tambah = lambda a,b: a+b 
# print(tambah(1, 2))

# def tambahh(a,b):
#     return a+b
# print(tambahh(1,2))

# #fungsi rekursif
# def spillangka(n):
#     if n == 0:
#         print("SELESAI WES!")
#     else:
#         print(n)
#         spillangka(n-1)
# spillangka(20)

# #escape variabel
# x = 10 #global

# def ubah_x():
#     x = 5 #lokal
#     print("nilai x di dalam fungsi:", x)

# ubah_x()
# print("nilai x di dalam fungsi:", x)