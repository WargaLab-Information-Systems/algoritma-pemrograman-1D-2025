bola_merah = int(input("masukkan jumlah bola merah :"))
bola_biru = int(input("Masukkan jumlah bole biru : "))
total_bola = bola_merah + bola_biru

ambil = 3  # Jumlah bola yang diambil

# C(14, 3) = (14 × 13 × 12) / (3 × 2 × 1)
pembilang = 14 * 13 * 12
penyebut = 3 * 2 * 1
kombinasi = pembilang // penyebut

print("Jumlah bola:", total_bola)
print("Jumlah kombinasi mengambil 3 bola =", kombinasi)