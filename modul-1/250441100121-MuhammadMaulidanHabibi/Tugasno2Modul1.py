print("Masukkan ukuran balok (dalam cm):")
p = float(input("Panjang: "))
l = float(input("Lebar: "))
t = float(input("Tinggi: "))
vol = p * l * t
lp = 2 * (p*l + p*t + l*t)
print("\nHasil Perhitungan:")
print(f"Volume Balok = {p} × {l} × {t} = {vol:.2f} cm³")
print(f"Luas Permukaan Balok = 2 × ({p}×{l} + {p}×{t} + {l}×{t}) = {lp:.2f} cm²")
