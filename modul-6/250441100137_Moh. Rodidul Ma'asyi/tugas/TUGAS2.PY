tuple1 = tuple(map(int, input("Masukkan angka untuk tuple pertama (pisahkan dengan spasi): ").split()))
tuple2 = tuple(map(int, input("Masukkan angka untuk tuple kedua (pisahkan dengan spasi): ").split()))

gabung = tuple1 + tuple2

hasil_tanpa_duplikat = []
for angka in gabung:
    if angka not in hasil_tanpa_duplikat:
        hasil_tanpa_duplikat.append(angka)

for i in range(len(hasil_tanpa_duplikat)):
    for j in range(i + 1, len(hasil_tanpa_duplikat)):
        if hasil_tanpa_duplikat[i] < hasil_tanpa_duplikat[j]:
            hasil_tanpa_duplikat[i], hasil_tanpa_duplikat[j] = hasil_tanpa_duplikat[j], hasil_tanpa_duplikat[i]

hasil_akhir = tuple(hasil_tanpa_duplikat)

print("Tuple hasil akhir:", hasil_akhir)