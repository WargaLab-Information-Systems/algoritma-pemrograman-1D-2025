# Fungsi untuk menghitung faktorial
def faktorial(n) :
    hasil = 1
    for i in range(1, n+ 1):
        hasil *= i
    return hasil

# Fungsi untuk menghitung kombinasi C(n, r)
def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Input 
bola_merah = int(input("Masukkan jumlah bola merah: "))
bola_biru = int(input("Masukkan jumlah bola biru: "))
ambil = int(input("Masukkan jumlah bola yang diambi: "))

# Hitung total bola
total_bola = bola_merah + bola_biru

# Hitung jumlah kombinasi 
if ambil <= total_bola:
    jumlah_kombinasi = kombinasi(total_bola, ambil)
    print("jumlah kemungkinan kombinasi bola yang dapat diambil:", jumlah_kombinasi)
else:
    print("jumlah bola yang diambil lebih banyak dari total bola!")
