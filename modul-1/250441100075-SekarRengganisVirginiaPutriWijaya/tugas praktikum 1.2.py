# Program menghitung volume dan luas permukaan balok

# Input
panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

print("Diketahui panjang: ",panjang,"cm")
print("Diketahui lebar: ",lebar,"cm")
print("Diketahui tinggi: ",tinggi,"cm")

# Rumus volume dan luas permukaan
volume = panjang * lebar * tinggi
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

print("Volume balok =", volume, "cm³")
print("Luas permukaan balok = ", luas_permukaan, "cm²")
