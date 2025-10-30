P = int(input("Masukkan Panjang : "))
L = int(input("Masukkan Lebar : "))
T = int(input("Masukkan Tinggi : "))

V = P * L * T # Rumus Volume Balok
luas = 2*(P*L + P*T + L*T)

print("volume balok : ", V )
print("Luas Permukaan : ", luas)
