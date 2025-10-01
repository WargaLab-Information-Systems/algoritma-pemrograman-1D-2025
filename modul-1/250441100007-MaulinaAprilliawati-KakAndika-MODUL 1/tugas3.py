#soal no3
print("======================================")
import math

bola_merah = int(input("masukkan jumlah bola merah :"))
bola_biru = int(input("masukkan jumlah bola biru :"))
total_bola = bola_merah + bola_biru
ambil = int(input("masukkan jumlah bola yg diambil :"))

n = math.factorial(total_bola)
r = math.factorial(ambil)
sisa = math.factorial(total_bola - ambil)

kombinasi = int(n / (r * sisa))

print("kombinasi bola yang dapat diambil adalah:", kombinasi)
print("======================================")