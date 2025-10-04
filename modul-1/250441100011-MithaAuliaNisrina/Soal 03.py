import math

# Input soal yang sudah diketahui 
print("Pengambilan beberapa bola sekaligus dari total beberapa bola")
bola_merah = int(input("Masukkan jumlah bola merah: "))
bola_biru = int(input("Masukkan jumlah bola biru: "))
jumlah_bola = bola_merah + bola_biru
bola_diambil = int(input("Masukkan bola yang akan diambil: "))

# Rumus kombinasi
print("Kombinasi = n! / (r! * (n-r)!)")

# Hitung kemungkinan kombinasi
n = math.factorial(jumlah_bola)
r = math.factorial(bola_diambil)
sisa = math.factorial(jumlah_bola - bola_diambil)

kombinasi = int(n / (r * sisa))

# Tampilkan hasil
print("Kemungkinan kombinasi bola yang dapat diambil adalah:", kombinasi)
