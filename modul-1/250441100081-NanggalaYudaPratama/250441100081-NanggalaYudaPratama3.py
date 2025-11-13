# TUGAS PRAKTIKUM NO.3
from math import comb

merah =  int(input("Masukkan total bola merah: "))
biru  =  int(input("Masukkan total bola biru: "))
total = merah + biru
bolaDiambil =  int(input("Masukkan total bola diambil: "))

kombinasi = comb(total, bolaDiambil)

print("Jumlah kombinasi:", kombinasi)
print(" \n")





























# def faktorial(n):
#     hasil = 1
#     for i in range(1, n + 1):
#         hasil *= i
#     return hasil

# n! / (r! * (n - r)!)
# kombinasi = faktorial(total) // (faktorial(r) * faktorial(total - r))