def faktorial (n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

def kombinasi(n,k):
    return faktorial(n)//(faktorial(k)*faktorial(n-k))

merah = 8
biru = 6
total_bola = merah + biru
bola_diambil = 3

hasil = kombinasi(total_bola,bola_diambil)

print(f"Banyak kemungkinan kombinasi bola yang dapat diambil : {hasil}")