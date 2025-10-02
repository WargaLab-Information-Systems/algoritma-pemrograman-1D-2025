#soal no2
print("======================================")

# input ukuran balok
panjang = int(input("masukkan panjang balok (cm): "))
lebar = int(input("masukkan lebar balok (cm): "))
tinggi = int(input("masukkan tinggi balok (cm): "))

# hitung volume dan luas permukaan
volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("panjang =", panjang,"cm")
print("lebar =", lebar, "cm")
print("tinggi =", tinggi, "cm")
print("volume balok =",volume ,"cm^3")
print("luas permukaan balok =", luas_permukaan, "cm^2")