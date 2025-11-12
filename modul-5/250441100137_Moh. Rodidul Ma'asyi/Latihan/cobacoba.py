# def morning () :
#     print("selamat malam")

# morning()

# HITUNG LUAS PERSEGI PANJANG (NON-FUNCTION)

# panjang = 5
# lebar = 3
# luas = panjang * lebar
# print(luas)

# panjang2 = 8
# lebar = 2
# luas2 = panjang2 * lebar
# print(luas2)

# HITUNG LUAS PERSEGI PANJANG (FUNCTION)

# def hitungan (panjang, lebar) :
#     luas = panjang * lebar
#     print("Luas persegi panjang adalah : ", luas)

# hitungan(10,6)
# hitungan(12,9)

# FUNCTION DENGAN RETURN
# def perkalian (a,b) :
#     c = a*b
#     return c
# print(perkalian(3,5))

# def perkalian (a) :
#     c = a*a
#     return c
# print(perkalian(int(input("masukkan angka : "))))

# LAMBDA
# tambah = lambda a,b: a+b or b*a
# print(tambah(4,5))


# def tambahh(a,b):
#     return a+b

# c = tambahh(5,5)

# hasil = c + c

# FUNGSI REKURSIF

# def spillangka(n):
#     if n == 0 :
#         print("Selesai")
#     else :
#         print(n)
#         spillangka(n-1)
# spillangka(8)

# SCOPE VARIABEL

# x = 10         # global

# def ubah_x() :
#     x = 5      # lokal
#     print("nilai x di dalam fungsi : ", x)

# c = x + 3
# print(c)

# ubah_x()
# print("nilai x di luar fungsi : ", x)

# def sapa_nama(nama):
#     print(nama, "Ojo lali mangan rek!")

# sapa_nama("Radit, ")
