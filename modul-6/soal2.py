print("\n" + "="*60)
print("Program menggabungkan dua angka")
print("="*60)

def input_tuple(nama):
    while True:
        data = input(f"Masukkan angka untuk {nama} (pisahkan dengan spasi): ")
        data_split = data.split()
        angka = []

        for i in data_split:
            if i.isdigit():
                angka.append(int(i))
            else:
                print(f"'{i}' bukan angka, masukkan hanya angka!")
                break
        else:
            return tuple(angka)  

tuple1 = input_tuple("tuple 1")
tuple2 = input_tuple("tuple 2")

gabungan = list(tuple1 + tuple2)

gabung = []
for angka in gabungan:
    if angka not in gabung:
        gabung.append(angka)


for i in range(len(gabung)):
    for j in range(i + 1, len(gabung)):
        if gabung[i] < gabung[j]:
            gabung[i], gabung[j] = gabung[j], gabung[i]

hasil_akhir = tuple(gabung)
print("Tuple pertama :", tuple1)
print("Tuple kedua   :", tuple2)
print("Gabung data   :", tuple(gabungan))
print("Hasil akhir   :", hasil_akhir)
