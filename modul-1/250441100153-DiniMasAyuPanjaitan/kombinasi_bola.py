import math

# Jumlah bola
bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru

# Banyak bola yang diambil
r = 3

# Hitung kombinasi
kombinasi = math.comb(total_bola, r)

print("Jumlah kemungkinan kombinasi pengambilan", r, "bola adalah:", kombinasi)
