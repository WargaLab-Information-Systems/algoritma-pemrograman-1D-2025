import math

merah = int(input("Masukkan jumlah bola merah: "))
biru = int(input("Masukkan jumlah bola biru: "))


# merah = 8
# biru = 6

total_bolah = merah + biru

ambil = int(input("Masukkan jumlah bola yang diambil: "))

# ambil = 3
kombinasi = math.comb(total_bolah, ambil)
print("Jumlah kemungkinan yang diambil oleh anak adalah :", kombinasi)