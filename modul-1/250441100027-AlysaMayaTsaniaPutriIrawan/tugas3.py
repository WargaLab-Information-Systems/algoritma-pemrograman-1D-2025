# menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil
print ("===jawaban===")

import math
bola_merah = int(input("masukkan bola merah: "))
bola_biru = int(input("masukkan bola biru: "))
jumlah_bola = bola_merah + bola_biru
bola_diambil = int(input("masukkan bola yang akan diambil: "))

kombinasi = math.comb(jumlah_bola, bola_diambil)
print ("kemungkinan kombinasi bola yang dapat diambil =", kombinasi)