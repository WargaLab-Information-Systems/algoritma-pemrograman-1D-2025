# Program menghitung volume dan luas permukaan balok (dinamis)
# Input ukuran balok dari pengguna
panjang = float(input("Masukkan panjang balok (cm): "))
lebar   = float(input("Masukkan lebar balok (cm)  : "))
tinggi  = float(input("Masukkan tinggi balok (cm) : "))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Tampilkan hasil
print("=== HASIL PERHITUNGAN BALOK ===")
print("Panjang balok        :", panjang, "cm")
print("Lebar balok          :", lebar, "cm")
print("Tinggi balok         :", tinggi, "cm")
print("Volume balok         :", volume, "cm³")
print("Luas permukaan balok :", luas_permukaan, "cm²")
