#input dari pengguna
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

#hitung volume
volume = panjang * lebar * tinggi

#hitung luas permukaan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

#output hasil
print("\n=== Hasil Perhitungan Balok ===")
print(f"Volume balok       : {volume} cm³")
print(f"Luas permukaan balok : {luas_permukaan} cm²")