panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# panjang = 10
# lebar = 6
# tinggi = 4

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("Volume balok:", volume ,"cm")
print("Luas permukaan balok:", luas_permukaan,"cm")