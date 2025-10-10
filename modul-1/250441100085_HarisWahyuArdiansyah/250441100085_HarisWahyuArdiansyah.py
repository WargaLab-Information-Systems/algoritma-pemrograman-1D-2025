# Tugas 1

bukutulis = int(input("Masukan jumlah buku tulis : "))
pensil = int(input("Masukan jumlah pensil : "))
pajak = 10 / 100

Thargabuku = bukutulis * 5000
Thargapensil = pensil * 4500
totalharga = Thargabuku + Thargapensil
totalpajak = totalharga * pajak
totalbayar = int(totalharga + totalpajak)

print("Total harga setelah pajak adalah : ", totalbayar,"\n")


# Tugas 2

panjang = int(input("masukan panjang : "))
lebar = int(input("masukan lebar : "))
tinggi = int(input("masukan tingi : "))

volume = panjang * lebar * tinggi  
luaspermukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print(f"volume balok adalah : {volume} and luas permukaan balok adalah : {luaspermukaan} \n")



# Tugas 3
from math import comb

bolamerah = int(input("Jumlah bola merah : "))
bolabiru = int(input("Jumlah bola biru : "))
totalbola = bolamerah + bolabiru
boladiambil = int(input("bola yang diambil : "))

jumlah_kombinasi = comb(totalbola, boladiambil)

print(f"Banyak kemungkinan kombinasi pengambilan {boladiambil} bola adalah: {jumlah_kombinasi}")
