# Meminta input dari pengguna
panjang = input(float("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Menghitung volume balok
volume = panjang * lebar * tinggi

# Menghitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Menampilkan hasil
print("Volume balok adalah:",int (volume))
print("Luas permukaan balok adalah:", int (luas_permukaan))

