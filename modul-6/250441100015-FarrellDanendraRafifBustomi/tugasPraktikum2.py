while True:
    try:
        angka1 = input("Masukkan angka-angka untuk tuple pertama: ")
        angka1 = tuple(int(x) for x in angka1.split())
        break
    except ValueError:
        print("Input tidak valid! Harap masukkan angka saja.\n")

while True:
    try:
        angka2 = input("Masukkan angka-angka untuk tuple kedua: ")
        angka2 = tuple(int(x) for x in angka2.split())
        break
    except ValueError:
        print("Input tidak valid! Harap masukkan angka saja.\n")

gabungan = angka1 + angka2
print("Gabungan kedua tuple:", gabungan)

duplikat = []
for angka in gabungan:
    if angka not in duplikat:
        duplikat.append(angka)

print("Angka tanpa duplikat:", duplikat)

for i in range(len(duplikat)):
    for j in range(0, len(duplikat) - i - 1):
        if duplikat[j] < duplikat[j + 1]:
            duplikat[j], duplikat[j + 1] = duplikat[j + 1], duplikat[j]

print("Angka urut-menurun:", duplikat)

hasilAkhir = tuple(duplikat)
print("Hasil akhir dalam bentuk tuple:", hasilAkhir)