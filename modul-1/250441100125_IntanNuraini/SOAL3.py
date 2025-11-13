import math

bola_merah = 8
bola_biru = 6
diambil_secara_acak = 3

total_bola = (bola_merah + bola_biru)

kombinasi = math.factorial(total_bola) // (math.factorial(diambil_secara_acak) * math.factorial(total_bola - diambil_secara_acak))

print ("total bola",total_bola)
print("Banyak kemungkinan kombinasi",kombinasi)