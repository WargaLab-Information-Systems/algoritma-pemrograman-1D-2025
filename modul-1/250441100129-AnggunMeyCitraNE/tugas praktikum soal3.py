import math

bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru
jumlah_diambil = 3

def kombinasi(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

jumlah_kombinasi = kombinasi(total_bola, jumlah_diambil)

print(f"jumlah bola merah: {bola_merah}")
print(f"jumlah bola biru: {bola_biru}")
print(f"jumlah bola yang diambil sekaligus: {jumlah_diambil}")
print(f"banyak kemungkinan kombinasi: {jumlah_kombinasi}")

print("\nContoh kombinasi yang mungkin:")
print("1. 3 merah, 0 biru")
print("2. 2 merah, 1 biru")
print("3. 1 merah, 2 biru")
print("4. 0 merah, 3 biru")