bola_merah = int(input("masukkan jumlah bola merah :"))
bola_biru = int(input("masukkan jumlah bola biru : "))
total_bola = bola_merah + bola_biru

ambil = 3 # jumlah bola yang diambil

# c(14, 3) = 14 x 13 x 12) / (3 x 2 x 1)
pembilang = 14 * 13 * 12
penyebut = 3 * 2 * 1
kombinasi = pembilang // penyebut

print("jumlah bola:" , total_bola)
print("jumlah kombinasi mengambil 3 bola =", kombinasi)