# TUGAS PRAKTIKUM NO.2
print("MENGHITUNG VOLUME DAN LUAS PERMUIKAAN BALOK")

panjang = int(input("Masukkan panjang Balok: "))
lebar = int(input("Masukkan Lebar Balok: "))
tinggi = int(input("Masukkan Tinggi Balok: "))

volume = panjang * lebar * tinggi
luas_permukaan = 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))

print(f"Volume balok-nya adalah: {volume}, Luas permukaann-nya adalah: {luas_permukaan}")
print(" \n")