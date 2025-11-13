import math

# Jumlah bola merah dan biru
bola_merah = int(input("Masukkan jumlah bola merah: "))
bola_biru = int(input("Masukkan jumlah bola biru: "))
total_bola = bola_merah + bola_biru


# Jumlah bola yang akan diambil 
bola_diambil = int(input("Masukkan jumlah bola yang akan diambil: "))

# Menghitung total kombinasi langsung dengan math.comb 
total_kombinasi = math.comb(total_bola, bola_diambil)

print(f"Jumlah total kemungkinan kombinasi bola yang akan diambil adalah: {total_kombinasi}")
