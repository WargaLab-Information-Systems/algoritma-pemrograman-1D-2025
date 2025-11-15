while True:
    try:
        n1 = int(input("Masukkan jumlah elemen tuple pertama : "))
        if n1 < 0:
            print("Jumlah elemen tidak boleh negatif!")
            continue
        break
    except ValueError:
        print("Input harus berupa angka!")

t1 = []
for i in range(n1):
    while True:
        try:
            angka = int(input(f"Masukkan elemen ke-{i+1} untuk tuple pertama : "))
            t1.append(angka)
            break
        except ValueError:
            print("Input harus berupa angka!")

t1 = tuple(t1)

while True:
    try:
        n2 = int(input("Masukkan jumlah elemen tuple kedua : "))
        if n2 < 0:
            print("Jumlah elemen tidak boleh negatif!")
            continue
        break
    except ValueError:
        print("Input harus berupa angka!")

t2 = []
for i in range(n2):
    while True:
        try:
            angka = int(input(f"Masukkan elemen ke-{i+1} untuk tuple kedua : "))
            t2.append(angka)
            break
        except ValueError:
            print("Input harus berupa angka!")

t2 = tuple(t2)

gabung = t1 + t2

tanpa_duplikat = []
for angka in gabung:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)

for i in range(len(tanpa_duplikat)):
    for j in range(i + 1, len(tanpa_duplikat)):
        if tanpa_duplikat[i] < tanpa_duplikat[j]:
            tanpa_duplikat[i], tanpa_duplikat[j] = tanpa_duplikat[j], tanpa_duplikat[i]

hasil = tuple(tanpa_duplikat)

print("Hasil akhir:", hasil)