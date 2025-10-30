import math

# Input jumlah bola
bola_merah = int(input("Masukkan jumlah bola merah : "))
bola_biru  = int(input("Masukkan jumlah bola biru  : "))

# Total bola
total_bola = bola_merah + bola_biru

# Input jumlah bola yang diambil
r = int(input("Masukkan jumlah bola yang diambil : "))

# Hitung kombinasi
kombinasi = math.comb(total_bola, r)

# Tampilkan hasil
print("=== HASIL PERHITUNGAN ===")
print("Jumlah bola merah :", bola_merah)
print("Jumlah bola biru  :", bola_biru)
print("Total bola        :", total_bola)
print("Jumlah kombinasi pengambilan", r, "bola :", kombinasi)
