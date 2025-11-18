n1 = int(input("Masukkan jumlah elemen tuple pertama : "))
t1 = []
for i in range(n1):
    angka = int(input(f"Masukkan elemen ke-{i+1} untuk tuple pertama : "))
    t1.append(angka)
t1 = tuple(t1)



n2 = int(input("Masukkan jumlah elemen tuple kedua : "))
t2 = []
for i in range(n2):
    angka = int(input(f"Masukkan elemen ke-{i+1} untuk tuple kedua : "))
    t2.append(angka)
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

print("Hasilakhir:",hasil)











#int untuk validasi agar tidak bisa menggunakan huruf
#append untuk menambahkan anggka  di list
#if not in duplikat dan .append npt duplikat brrti tidak menambahkan angka duplikatj
#for j
  