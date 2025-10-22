print("soal no 3 : kemungkinan bola yang diambil")

bola_biru = int(input("jumlah bola_biru = "))
bola_merah = int(input("masukkan jumlah bola merah : "))
total_bola = bola_biru + bola_merah 

bola_diambil = int (input("masukkan jumlah bola yang diambil : "))
import math 
hasil = math.comb (total_bola , bola_diambil )
print ("jumlah kombinasi bola = " , hasil )
