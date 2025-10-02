# Fungsi faktorial manual
def faktorial(n):
    hasil = 1
    for i in range(2, n+1):
        hasil *= i
    return hasil

# Fungsi kombinasi manual menggunakan faktorial manual
def kombinasi(n, k):
    if k > n or k < 0:
        return 0
    return faktorial(n) // (faktorial(k) * faktorial(n - k))

# Jumlah bola merah dan biru
merah = 8
biru = 6

# Hitung kemungkinan kombinasi berdasarkan jumlah bola merah dan biru yang diambil
k1 = kombinasi(merah, 3) * kombinasi(biru, 0)  # 3 merah, 0 biru
k2 = kombinasi(merah, 2) * kombinasi(biru, 1)  # 2 merah, 1 biru
k3 = kombinasi(merah, 1) * kombinasi(biru, 2)  # 1 merah, 2 biru
k4 = kombinasi(merah, 0) * kombinasi(biru, 3)  # 0 merah, 3 biru

total_kombinasi = k1 + k2 + k3 + k4

print("3 merah, 0 biru:", (k1))
print("2 merah, 1 biru:", (k2))
print("1 merah, 2 biru:", (k3))
print("0 merah, 3 biru:", (k4))
print("Total kemungkinan kombinasi:", (total_kombinasi))
