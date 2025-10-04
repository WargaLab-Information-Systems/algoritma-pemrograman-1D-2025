# Program menghitung volume dan luas permukaan balok

# input data
panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# hitung volume
volume = panjang * lebar * tinggi

# hitung luas permukaan
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# output hasil
print("Volume balok        =", volume, "cm³")
print("Luas Permukaan balok =", luas_permukaan, "cm²")