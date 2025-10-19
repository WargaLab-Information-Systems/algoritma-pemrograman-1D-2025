#tugas Praktikum soal 2
panjang = int(input("masukkan panjang balok: ") or "10")
lebar = int(input("masukkan lebar balok: ") or "6")
tinggi = int(input("masukkan tinggi balok: ") or "4")

volume = panjang * lebar * tinggi

luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

print(f"Hasil hitung:")
print(f"panjang balok : {panjang}cm")
print(f"lebar balok : {lebar}cm")
print(f"tinggi balok : {tinggi}cm")
print(f"volume balok : {volume}cm³")
print(f"luas permukaan balok : {luas_permukaan}cm²")