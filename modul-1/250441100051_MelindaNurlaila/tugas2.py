print("Menghitung volume balok dan luas permukaannya")

panjang = float(input("Masukkan Panjang (cm): "))
tinggi = float(input("Masukkan Tinggi (cm): "))
lebar = float(input("Masukkan Lebar (cm): "))

volume = panjang * lebar * tinggi
luas_permukaan = 2*(panjang*lebar)+(panjang*tinggi)+(lebar*tinggi)

print("Volumenya adalah : ", volume, "cm")
print("Luas permukaan baloknya adalah : ", luas_permukaan, "cm")