# Program menghitung volume dan luas permukaan balok

# Data ukuran balok (dalam cm)
panjang = 10
lebar = 6
tinggi = 4

# Hitung volume balok
volume = panjang * lebar * tinggi

# Hitung luas permukaan balok
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Output
print("=== Perhitungan Balok ===")
print(f"Panjang : {panjang} cm")
print(f"Lebar   : {lebar} cm")
print(f"Tinggi  : {tinggi} cm")
print(f"Volume balok : {volume} cm³")
print(f"Luas permukaan : {luas_permukaan} cm²")
